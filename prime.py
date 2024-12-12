from tools import *

def is_prime(n):
    key = 37
    return moduler(key,n-1,n) == 1


def random_primes(bytes:int=4, count:int=1):
    # if bytes>64:
    #     print("너무 큰 크기의 랜덤 소수는 못 굴립니다...")
    #     return tuple([0 for i in range(count)])
    
    primes = []
    while len(primes) < count:
        odd = random_bit(bytes*8-1)*2 +1
        found_prime = False
        
        while not found_prime:
            if is_prime(odd):
                primes.append(odd)
                found_prime = True
            else:
                odd += 2

    return tuple(primes)

def __test():
    a = random_primes(bytes=64)
    print(a)

if __name__ == "__main__":
    check_times(__test)