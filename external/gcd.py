def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"GCD of {num1} and {num2} is {gcd(num1, num2)}")
    print(f"LCM of {num1} and {num2} is {lcm(num1, num2)}")