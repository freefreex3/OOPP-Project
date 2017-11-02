def is_prime(s):
    valid=True
    if s.isdigit():
        val = int(s)
        for i in range(2,val):
            if val % i ==0: #no remainder means not a primee number
                valid=False
    return valid







for i in range(1, 20):
    print(i, is_prime(str(i)))


