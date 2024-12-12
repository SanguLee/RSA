def check_bit(n):
   return len(format(n,'#b')[2:])

def random_bit(bits:int):
    import random
    b = ['0b1']
    for i in range(bits-1):
        odd = random.random()>0.5
        b.append(str(int(odd)))
    return int(''.join(b),2)


def moduler(x, d, n):
    y = x % n
    r = 1
    while d > 0:
        if d % 2 == 1:
            r = (r * y) % n
        y = (y * y) % n
        d = d // 2
    return r

def check_times(call:callable):
    import time
    s = time.time()
    call()
    e = time.time()
    print("%.5f" %(e-s))

def __test():
    for i in range(1000):
        random_bit(64)

if __name__ == "__main__":
    check_times(__test)

