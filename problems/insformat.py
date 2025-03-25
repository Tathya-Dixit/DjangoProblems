def insformat(num):
    integer, decimal = str(num).split('.')
    op = "."+decimal
    if int(integer) < 1000:
        op = integer + op
    else:
        integer = int(integer)
        temp = integer%1000
        if temp < 10:
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

if __name__ == "__main__":
    num = float(input("Enter the number: "))
    print(insformat(num))