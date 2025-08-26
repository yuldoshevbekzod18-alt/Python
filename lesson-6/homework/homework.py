#The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
#The first and only line contains the integer, n.
#1 <= n <= 20
#Print n lines, one corresponding to each i^2 where 0 <= i < n.
def my_func(n):
    for i in range(n):
        print(i**2)
my_func(6)


#Print first 10 natural numbers using a while loop
n=1
while n<=10:
    print(f'sonlar {n}')
    n+=1


#Print the following pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()


#Calculate sum of all numbers from 1 to a given number
n=1
yegindi=0
while n<=10:
    yegindi+=n
    n+=1
print(yegindi)

#Print multiplication table of a given number
n=1
while n*2<=20:
    print(n*2)
    n+=1



#5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    else:
        print(num)



#Count the total number of digits in a number
num=int(input('Son kiriting:'))
ye=0
while num>0:
    ye+=1
    num//=10
print(ye)



# Print reverse number pattern
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()


#Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in range(50,0,-10):
    print(i,end='\n')
print()

#Display numbers from -10 to -1 using a for loop
for i in range(-10,0,1):
    print(i,end='\n')
print()

#Display message “Done” after successful loop execution
n=5
for i in range(0,n,1):
    print(i,end='\n')
print('Done')

#Print all prime numbers within a range
#Prime numbers between 25 and 50:
for i in range(25, 51):
    for num in range(2, i):
        if i % num == 0:
            break
    else:   # agar break ishlamasa (bo‘luvchi topilmasa)
        print(i)

#Display Fibonacci series up to 10 terms
num=int(input('Son kiriting:'))
a,b=0,1
print(a,b,end=' ')
for _ in range(0,num):
    c=a+b
    print(c,end=' ')
    a,b=b,c

#Find the factorial of a given number
def factorial(n):
    if n in[0,1]:
        return 1
    else:
        return n*factorial(n-1)
factorial(8)

#Return the elements that are not common between two lists. The order of elements does not matter.
list1 = [1, 1, 2]
list2 = [2, 3, 4]
set1=set(list1)
set2=set(list2)
result=set1.intersection(set2)
print(result)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
set1=set(list1)
set2=set(list2)
result=set1.union(set2)
print(result)

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
result=[]
for x in list1:
    if x not in list2:
        result.append(x)
for x in list2:
    if x not in list1:
        result.append(x)
print(result)
