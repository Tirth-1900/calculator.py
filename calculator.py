def sum(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

def main():
    print("Welcome to calculator")
    print("Select the operation you want to perform")
    print("1.Addition")
    print("2.subraction")
    print("3.Multiplaction")
    print("4.Division")
    choise = float(input("Enter your choise :"))
    a = float(input("Enter first no: "))
    b = float(input("Enter second no: "))
    if choise == 1:
        print("the sum of",a,"and",b,"is",sum(a,b))
    elif choise == 2:
        print("The subtration of",a,"and",b, "is", sub(a,b))
    elif choise == 3:
        print("The multiplaction of",a,"and",b, "is", mul(a,b))
    elif choise == 4:
        print("The dividion of",a,"and",b, "is", div(a,b))

    else:
        print("Invalid OPerator")

if __name__ == "__main__":
  main()