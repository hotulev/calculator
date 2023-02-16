print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
i = 0
oper = float(input("кол-во операций:"))
x = float(input("x="))
while i != oper:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        y = float(input("y="))
        if s == '+':
            result = x+y
            print ("%.2f" % (result))
            x = result
        elif s == '-':
            result = x - y
            print("%.2f" % (result))
            x = result
        elif s == '*':
            result = x * y
            print("%.2f" % (result))
            x = result
        elif s == '/':
            if y != 0:
                result = x / y
                print("%.2f" % (result))
                x = result
            else:
                print("Деление на ноль!")
        i+=1
    else:
        print("Неверный знак операции!")