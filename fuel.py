r = True
while r == True:
    try:
        frac = input('Дробь: ')
        s = frac.split('/')
        X = int(s[0])
        Y = int(s[1])
        f = X/Y * 100
        f //= 1
        r = False
    except ValueError:
        continue
    except ZeroDivisionError:
        continue

if f >= 99:
    print('F')
elif f <= 1:
    print('E')
else:
    print(str(int(f)) + '%')