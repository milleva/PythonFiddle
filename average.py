summa = 0
lkm = 0

while 1:

        try:
                 x = int(input('number: '))
        except:
                break
        summa += x
        lkm += 1

print(summa/lkm)

