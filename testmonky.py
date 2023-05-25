# m2 = ((81 * m2) mod 89) * 11) mod 89

for i in range(89):
    if i == (((81 * i) % 89) * 11) % 89 :
        print(i)