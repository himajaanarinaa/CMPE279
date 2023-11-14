import time
import timeit
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def measure_time(func):
    start_time = time.perf_counter()
    func()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")

def measure_cpu_cycles(func, number=1000000):
    cpu_cycles = timeit.timeit(func, number=number)
    print(f"CPU cycles: {cpu_cycles:.6f}")

def aes_encrypt():
    key = b'0123456789abcdef'
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    plaintext = b'This is a test message for AES encryption.'
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

def aes_decrypt():
    key = b'0123456789abcdef'
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    ciphertext = b'\x8f\x1e+\xa0iP\r\x82\xcd\x9d\x1b\x8e\x0f\xda\xc3l'
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

if __name__ == "__main__":
    print("AES Encryption:")
    measure_time(aes_encrypt)
    measure_cpu_cycles(lambda: aes_encrypt(), number=100000)

    print("\nAES Decryption:")
    measure_time(aes_decrypt)
    measure_cpu_cycles(lambda: aes_decrypt(), number=100000)
