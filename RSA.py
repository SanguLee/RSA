import math
from prime import random_primes
from tools import *
from tqdm import tqdm

def __extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def __get_e() -> int:
    return 65537  # 2^16 + 1


def __get_d(e, phi):
    gcd, x, _ = __extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("e is not coprime to phi")
    return x % phi


def make_rsa_key(bytes:int=4) -> tuple[int, int, int]:
    r = random_primes(bytes, count=2)
    __p, __q = r
    n = __p * __q
    __phi = (__p - 1) * (__q - 1)
    e = __get_e()
    d = __get_d(e, __phi)
    return (e, d, n)


def encrpyt(x: int, e: int, n: int) -> int:
    return moduler(x, e, n)


def decrypt(x: int, d: int, n: int) -> int:
    return moduler(x, d, n)


def check_rsa_accuracy(e, d, n, bytes:int=4, test:int=100):
    success_count = 0

    for a in tqdm([random_bit(bytes*8) for i in range(test)]):
        __e = encrpyt(a, e, n)
        __d = decrypt(__e, d, n)
        if a == __d:
            success_count += 1

    # print success rate
    print("This RSA key's accuracy : %.4f" % (success_count / test))

def __test():
    bytes = 128
    e,d,n = make_rsa_key(bytes)
    check_rsa_accuracy(e,d,n,bytes,test=1000)

if __name__ == "__main__":
    check_times(__test)
