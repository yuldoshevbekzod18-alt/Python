
#def is_leap(year): """ Determines whether a given year is a leap year.
year=int(input('Enter year:'))
if  year % 4==0:
    if year % 100==0:
        if year % 400==0:
            print('leap year')
        else:
            print('not leap year')
    else:
        print('leap year')
else:
    print('Not leap year')


#If n is odd, print Weird
num=int(input('Son kiritng:'))
if num%2 !=0:
    print('Weird')
else:
    print('not weird')



#If n is even and in the inclusive range of 2 to 5, print Not Weird
num=int(input("Son kiriting:"))

if num%2==0 and 2<=num<=5:
       print('Not Weird')
else:
       print('Weird')


#If n is even and in the inclusive range of 6 to 20, print Weird
num=int(input("Son kiriting:"))
if  num%2==0 and 6<=num<=20:
    print('Weird')
else:
    print('Not Weird')



#Print Weird if the number is weird. Otherwise, print Not Weird.
num=int(input("Son kiriting:"))
if  num%2==0 :
    print('Weird')
else:
    print('Not Weird')



#If n is even and greater than 20, print Not Weird
num=int(input("Son kiriting:"))
if num%2==0 and num>20:
    print("Not Weird")
else:
    print('Weird')


#Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
a=int(input('a sonini kiriting:'))
b=int(input('b sonini kiriting:'))
if a%2!=0:
    a+=1
even_num=list(range(a,b+1,2))
print(even_num)



