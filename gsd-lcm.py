def gcd(a, b):
  a = abs(a)
  b = abs(b)

  while a != b:
    if a > b:
      a -= b
    else:
      b -= a
  return a

def lcm(a, b):
  a = abs(a)
  b = abs(b)

  gcdResult = gcd(a, b)
  return (a * b) // gcdResult


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)
print("The greatest common divisor of {} and {} is {}".format(num1, num2, result))

result = lcm(num1, num2)
print("The least common multiple of {} and {} is {}".format(num1, num2, result))