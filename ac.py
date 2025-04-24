num = int(input("Enter a number: "))

count = 0

while num > 0:
    dig = num%10
    count = count + 1
    num//= 10

print( "The number of digits is ",count)
