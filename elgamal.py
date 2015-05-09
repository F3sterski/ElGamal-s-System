import sys
import random
from fractions import gcd


def extended_gcd(aa, bb):
    last_remainder, remainder = abs(aa), abs(bb)
    x, last_x, y, last_y = 0, 1, 1, 0
    while remainder:
        last_remainder, (quotient, remainder) = remainder, divmod(last_remainder, remainder)
        x, last_x = last_x - quotient*x, x
        y, last_y = last_y - quotient*y, y
    return last_remainder, last_x * (-1 if aa < 0 else 1), last_y * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        print "can't inverse"
        exit()
    return x % m


if len(sys.argv) > 1:
    if sys.argv[1] == "-g":
        elgamal_file = open("elgamal.txt", "w")
        elgamal_file.write("1665997633093155705263923663680487185948531888850484859473375695734301776192932338784530163\n"
                           + "170057347237941209366519667629336535698946063913573988287540019819022183488419112350737049")
        exit()
    elif sys.argv[1] == "-k":
        numbers_file = open("elgamal.txt", "r")
        private_file = open("private.txt", "w")
        public_file = open("public.txt", "w")
        number1 = numbers_file.readline()
        number2 = numbers_file.readline()
        if number1 != "":
            p = long(number1)
        if number2 != "":
            g = long(number2)
        if not p or not g:
            print "file elgamal doesn't contains numbers"
            exit()
        b = random.randint(1, p-1)
        Beta = pow(g, b, p)
        private_file.write(str(p) + "\n" + str(g) + "\n" + str(b))
        public_file.write(str(p) + "\n" + str(g) + "\n" + str(Beta))
        exit()
    elif sys.argv[1] == "-e":
        public_file = open("public.txt", "r")
        plain_file = open("plain.txt", "r")
        crypto_file = open("crytpo.txt", "w")
        number1 = public_file.readline()
        number2 = public_file.readline()
        number3 = public_file.readline()
        number4 = plain_file.readline()
        if number1 != "":
            p = long(number1)
        if number2 != "":
            g = long(number2)
        if number3 != "":
            Beta = long(number3)
        if number4 != "":
            m = long(number4)
        if not p or not g or not Beta or not m:
            print "file public or plain doesn't contains numbers"
            exit()
        if m > p:
            print "message is bigger than prime"
            exit()
        k = random.randint(2, p-1)
        while gcd(k, p) != 1:
            k = random.randint(2, p-1)
        r = pow(g, k, p)
        t = (m * pow(Beta, k, p)) % p
        crypto_file.write(str(r) + "\n" + str(t))
        exit()
    elif sys.argv[1] == "-d":
        private_file = open("private.txt", "r")
        crypto_file = open("crytpo.txt", "r")
        decrypt_file = open("decrypt.txt", "w")
        number1 = private_file.readline()
        number2 = private_file.readline()
        number3 = private_file.readline()
        number4 = crypto_file.readline()
        number5 = crypto_file.readline()
        if number1 != "":
            p = long(number1)
        if number2 != "":
            g = long(number2)
        if number3 != "":
            b = long(number3)
        if number4 != "":
            r = long(number4)
        if number5 != "":
            t = long(number5)
        if not p or not g or not b or not r or not t:
            print "file private or crypto doesn't contains numbers"
            exit()
        wsp = pow(r, b, p)
        m = (modinv(wsp, p)*t) % p
        decrypt_file.write(str(m))
        exit()
    elif sys.argv[1] == "-s":
        private_file = open("private.txt", "r")
        message_file = open("message.txt", "r")
        signature_file = open("signature.txt", "w")
        number1 = private_file.readline()
        number2 = private_file.readline()
        number3 = private_file.readline()
        number4 = message_file.readline()
        if number1 != "":
            p = long(number1)
        if number2 != "":
            g = long(number2)
        if number3 != "":
            b = long(number3)
        if number4 != "":
            m = long(number4)
        if m > p:
            print "message is bigger than prime"
            exit()
        k = random.randint(2, p-1)
        while gcd(k, p-1) != 1:
            k = random.randint(2, p-1)
        r = pow(g, k, p)
        x = ((m-b*r)*modinv(k, p-1)) % (p-1)
        signature_file.write(str(r) + "\n" + str(x))
        exit()
    elif sys.argv[1] == "-v":
        public_file = open("public.txt", "r")
        message_file = open("message.txt", "r")
        signature_file = open("signature.txt", "r")
        valid_file = open("valid.txt", "w")
        number1 = public_file.readline()
        number2 = public_file.readline()
        number3 = public_file.readline()
        number4 = message_file.readline()
        number5 = signature_file.readline()
        number6 = signature_file.readline()
        if number1 != "":
            p = long(number1)
        if number2 != "":
            g = long(number2)
        if number3 != "":
            Beta = long(number3)
        if number4 != "":
            m = long(number4)
        if number5 != "":
            r = long(number5)
        if number6 != "":
            x = long(number6)
        a = pow(g, m, p)
        b = (pow(r, x, p) * pow(Beta, r, p)) % p
        if a == b:
            print "valid"
            valid_file.write("valid")
        else:
            print "invalid"
            valid_file.write("invalid")
        exit()
    else:
        print "invalid parameter"
else:
    print "no parameter"