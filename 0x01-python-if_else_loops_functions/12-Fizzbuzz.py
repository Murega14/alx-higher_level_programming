#1/usr/bin/python3
def Fizzbuzz():
    for num in range(1, 100):
        result = ""
        if(num % 3 == 0):
            result += "Fizz"
        if(num % 5 ==0):
            result += "Buzz"
        print("{}".format(result) or "{}".format(num), end='')
        print(" ", end='')
