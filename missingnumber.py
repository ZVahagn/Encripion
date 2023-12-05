def find_missing_number(array, n):
    sum = (n + 1) * (n + 2) // 2

    actual_sum = 0
    for i in range(n):
        actual_sum += array[i]
        
    return sum - actual_sum

n = int(input("Enter the value of n: "))

if n < 1:
    print("Invalid input. 'n' should be a positive integer.")
    
array = []
for i in range(n):
    array.append(int(input("Enter a number: ")))

missing_number = find_missing_number(array, n)

print("The missing number is: {}".format(missing_number))