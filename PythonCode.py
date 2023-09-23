def multi(a, b):
    product = a*b
    if product <= 1000:
        return product
    else:
        return a+b


result = multi(50, 20)
print(result)
result1 = multi(500, 200)
print(result1)
print("********************")
print("Current and Previous Number for the Range of 10")
previous_num = 0
for i in range(0, 11):
    current_num = i
    sum1 = current_num+previous_num
    print("Current Number", current_num,
          "Previous Number", previous_num, "Sum:", sum1)
    previous_num = current_num
print("********************")

print("Fibonacci Series")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))


n = int(input("Enter the number of terms:"))

if n <= 0:
    print("Enter a positive number")

else:
    print("Fibonacci Series:")
    for i in range(n):
        print(fibonacci(i))

print("********************")

print("Prime Numbers")


def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
            break
        else:
            return True


n = int(input("Enter the number of terms:"))

if n <= 0:
    print("Enter a positive number")

else:
    print("Prime Numbers:")
    for i in range(n):
        if prime_num(i):
            print(i)

print("********************")

print("Factors of a number")


def factors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)


n = int(input("Enter the number:"))

if n <= 0:
    print("Enter a positive number")

else:
    print("Factors of a number:")
    factors(n)

print("********************")
print("Amstrong Number")


def amstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit**3
        temp //= 10
    if n == sum:
        return True
    else:
        return False


n = int(input("Enter the number:"))

if n <= 0:
    print("Enter a positive number")

else:
    print("Amstrong Number:")
    if amstrong(n):
        print(n, "is an Amstrong Number")
    else:
        print(n, "is not an Amstrong Number")

print("********************")

print("Palindrome Number")


def palindrome(n):
    temp = n
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev*10+digit
        temp //= 10

    if n == rev:
        return True
    else:
        return False


n = int(input("Enter the number:"))

if n <= 0:
    print("Enter a positive number")

else:
    print("Palindrome Number:")
    if palindrome(n):
        print(n, "is a Palindrome Number")
    else:
        print(n, "is not a Palindrome Number")

print("********************")
print("Celcious to Fahrenheit")


def cel_to_fahr(cel):
    fahrenheit = n*1.8+32
    return fahrenheit


n = int(input("Enter the Celcious:"))

if n <= 0:
    print("Enter a positive number")

else:
    print("Celcious to Fahrenheit:")
    print(n, "Celcious is", cel_to_fahr(n), "Fahrenheit")

print("********************")

print("Fahrenheit to Celcious")


def fahr_to_cel(fahr):
    celcious = n-32/1.8
    return celcious


n = int(input("Enter the Fahrenheit:"))

if n <= 0:
    print("Enter a positive number")

else:
    print("Fahrenheit to Celcious:")
    print(n, "Fahrenheit is", fahr_to_cel(n), "Celcious")

print("********************")
print("Characters from a string that are present at an even index number")
print("Accepet the Input from the string")
word = input("Enter the string:")
size = len(word)
for i in range(0, size-1, 2):
    print("index[", i, "]", word[i])

print("*************************")
print("Generate an infinite fibonacci series using generator")


def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


for i in fibonacci_gen():
    print(i)
    if i > 100:
        break

print("*************************")

print("Generate an infinite prime number series using generator")


def prime_gen():
    n = 2
    while True:
        if prime_num(n):
            yield n
        n += 1


for i in prime_gen():
    print(i)
    if i > 100:
        break

print("*************************")
print("Sort Without Using Sort Keywor")
list1 = [41, 2, 5, 6, 19, 1, 0, 20, 30, 12, 10, 80]
n = len(list1)

for i in range(n):
    for j in range(i+1, n):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

print(list1)

print("*************************")

print("Whether a string is palindrom or not")
S = input("Enter the string:")
if S == S[::-1]:
    print("Its a Palindrome")
else:
    print("Not Palindrome")

print("*************************")
# print("Print the ASCII value of the character")

# S=input("Enter the character:")
# print(ord(S))

# print("*************************")
print("Find all the pairs of integers whose sum is equal to a given number")


def pairs(list1, n):
    k = len(list1)
    for i in range(k):
        for j in range(i+1, k):
            if list1[i]+list1[j] == n:
                return list1[i], list1[j]


n = int(input("Enter the number:"))
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("**********************")
print("Find the MAx and Min value of a list without using any predefined functions")
l = [9, 1, 10, 20, 100, 0]
maximum = l[0]
minimum = l[0]
for i in l:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
    print("Maximum:", maximum)
    print("Minimum:", minimum)

print("**********************")

print("Find the sum of all the elements of a list without using any predefined functions")
l = [9, 1, 10, 20, 100, 0]

sum = 0

for i in l:
    sum += i

print("Sum:", sum)

print("**********************")

print("Find the MAx and Min value of a list  using any predefined functions")

l = [9, 1, 10, 20, 100, 0]

print("Maximum:", max(l))

print("Minimum:", min(l))

print("**********************")
