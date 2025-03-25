def insformat(num):
    integer, decimal = map(int,str(num).split('.'))
    op = "."+str(decimal)
    if integer < 1000:
        op = str(integer) + op
    else:
        temp = integer%1000
        if temp == 0:
            op = "000" + op
        elif temp < 10:
            op = "00" + str(temp) + op
        elif temp < 100:
            op = "0" + str(temp) + op
        else:
            op = str(temp) + op
        integer = integer//1000
        while integer > 0:
            temp = integer%100
            if temp<10 and integer > 10:
                op = "0" + str(temp) + "," + op
            else:
                op = str(temp) + "," + op
            integer = integer//100

    return op

num = float(input("Enter the number: "))
print(insformat(num))