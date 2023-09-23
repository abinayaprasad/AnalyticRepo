#
# Write a python program to find the sum of two numbers
import pandas as pd
a = 12
b = 14
c = a+b
print(c)


# Write a python program to find the maximum of three numbers

a = 12

b = 14

c = 15

if a > b and a > c:
    print(a)

elif b > a and b > c:
    print(b)

else:
    print(c)


# to read a CSV file
df = pd.read_excel(r'C:\Users\Abinaya\Downloads\Amazon Sales.xlsx')
print(df.head(10))
# sum of the sales

sum = df['Sales'].sum()
print("********Sum of Sales**********")
print(sum)

# average of the sales

avg = df['Sales'].mean()
print("********Average of Sales**********")
print(avg)

# count of the sales

count = df['Sales'].count()
print("********Count of Sales**********")
print(count)

# maximum of the sales

max = df['Sales'].max()
print("********Maximum of Sales**********")
print(max)

# minimum of the sales

min = df['Sales'].min()
print("********Minimum of Sales**********")
print(min)

# median of the sales

median = df['Sales'].median()
print("********Median of Sales**********")
print(median)

# mode of the sales

mode = df['Sales'].mode()
print("********Mode of Sales**********")
print(mode)

# standard deviation of the sales

std = df['Sales'].std()
print("********Standard Deviation of Sales**********")
print(std)

# variance of the sales

var = df['Sales'].var()
print("********Variance of Sales**********")
print(var)
