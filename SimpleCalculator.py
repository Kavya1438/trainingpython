class SimpleCalculator():
    @staticmethod
    def add(a: float, b:float) -> float:
        return a+b


    @staticmethod
    def sub(a:float, b:float) ->float:
        return a-b


    @staticmethod
    def multiply(a:float, b:float) ->float:
        return a*b


    @staticmethod
    def divide(a:float, b:float) ->float:
        if b==0:
            raise ZeroDivisionError("Divison by zero is undefined")
        return a/b

def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")


    arith_operations = {

                   "1":SimpleCalculator.add,
                   "2":SimpleCalculator.sub,
                   "3":SimpleCalculator.multiply,
                   "4":SimpleCalculator.divide


}
    option=input("1-addition/2-Subtract/3-multiply/4-divide: ")

    if option not in arith_operations:
      print("Invalid option entered")
      return

    try:
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number"))


        arith_op=arith_operations[option]
        result=arith_op(num1,num2)
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()