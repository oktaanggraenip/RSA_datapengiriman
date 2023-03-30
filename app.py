import random
import string
from flask import Flask, request, render_template

app = Flask(__name__)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    prime = random.randint(100, 1000)
    while not is_prime(prime):
        prime = random.randint(100, 1000)
    return prime

def generate_key_pair():
    p = generate_prime()
    q = generate_prime()
    while p == q:
        q = generate_prime()

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randint(2, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n)

    d = pow(e, -1, phi_n)

    return ((e, n), (d, n))

def pad_message(message):
    block_size = 2
    message_length = len(message)
    num_blocks = (message_length + block_size - 1) // block_size
    padded_message_length = num_blocks * block_size
    padding_length = padded_message_length - message_length
    padding = bytes([padding_length]) * padding_length
    return message + padding

def unpad_message(message):
    padding_length = message[-1]
    return message[:-padding_length]

def encrypt(message, public_key):
    e, n = public_key
    padded_message = pad_message(message.encode())
    ciphertext_blocks = []
    for i in range(0, len(padded_message), 2):
        block = padded_message[i:i+2]
        num = int.from_bytes(block, byteorder='big')
        ciphertext_blocks.append(pow(num, e, n))
    return ','.join(map(str, ciphertext_blocks))

def decrypt(ciphertext, private_key):
    d, n = private_key
    ciphertext_blocks = ciphertext.split(',')
    plaintext_blocks = []
    for block in ciphertext_blocks:
        num = int(block)
        decrypted_num = pow(num, d, n)
        decrypted_block = decrypted_num.to_bytes(2, byteorder='big')
        plaintext_blocks.append(decrypted_block)
    plaintext = b''.join(plaintext_blocks)
    unpadded_plaintext = unpad_message(plaintext)
    return unpadded_plaintext.decode()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def encrypt_decrypt():
    public_key, private_key = generate_key_pair()
    data = {}
    for key in request.form:
        message = request.form[key]
        ciphertext = encrypt(message, public_key)
        decrypted_message = decrypt(ciphertext, private_key)
        data[key] = {
            'plaintext': message,
            'ciphertext': ciphertext,
            'decrypted': decrypted_message
        }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
