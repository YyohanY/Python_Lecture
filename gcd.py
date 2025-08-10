def gcd_sub(a, b) :
    while a != 0 and b != 0 :
        print ('a = ', a, '','b = ', b, '')
        if a > b :
            a = a - b
            print('a = ', a)
        else :
            b = b - a
            print('b = ', b)
    return a+b

def gcd_mod(a, b) :
    while a != 0 and b != 0 :
        print ('a = ', a, '','b = ', b, '')
        if a > b :
            a = a % b
            print('a = ', a)
        else :
            b = b % a
            print('b = ', b)
    return a+b

k = gcd_sub(2, 100)
print(k)