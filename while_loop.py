'''Write a program that asks a user to enter a number and print out how many numbers from 1 to N (including N) are divisible by 5 or 7 and the list of the numbers using while loop.

Example:
>>>
40                                                                  
There are 12 numbers divisible by 5 and 7.
5,7,10,14,15,20,21,25,28,30,35,40,       '''

#code:
'''
def divisible(num):
    if int(num):
        if (int(num)/5).is_integer() or (int(num)/7).is_integer():
            return True
        return False

num = input()

numbers = []
thisNum = 1

while thisNum != int(num)+1:
    if divisible(int(thisNum)):
        numbers.append(int(thisNum))
    thisNum += 1

print(numbers)
print("There are", len(numbers), "numbers divisible by 5 or 7")

'''

'''Write a program that prints out the multiplication table of the entered number by the user by using whileloop.

Example 1:
>>>
5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

'''
#code:
'''
num = int(input())

i = 1
while i <= 10:
    num = num * 1
    print(num, "x", i, "=", num*i)
    i += 1

'''

'''Write a program that asks a user to enter a number and print out the sum of the powers of 2 from 0 to N using while loop.

SUM = 20 + 21+22+...+2N

Example:
>>>
4
The sum is 31.
>>>
2
The sum is 7.
'''

#code:

num = input()

result = 0
thisNum = 0

while thisNum != int(num)+1:
    result = result + (2**thisNum)
    thisNum += 1

print('The sum is', result)