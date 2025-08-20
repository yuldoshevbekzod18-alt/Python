#Write a Python script to sort (ascending and descending) a dictionary by value.
date=[12,15,6,22,28,31,4,10]
date.sort()
print(f'tartib boyicha {date}')
date.sort(reverse=True)
print(f'kamayish tartibda{date}')


#Write a Python script to add a key to a dictionary.
key={0: 10, 1: 20}
key[2]=30
key


#Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)


#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n=int(input('n sonini kiriting:'))
kvadratlar={}
for x in range(1, n + 1):
    kvadratlar[x]=x*x
print(kvadratlar)



#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
kvadrat={}
for x in range(1,16):
    kvadrat[x]=x*x
print(kvadrat)


#Write a Python program to create a set.
list={1,4,5,6,7,'Oybek'}
list



#Write a Python program to iterate over sets.
list={'ummon','kebyo','zuhra','Oybek'}
for list1 in (list):
    print(list1)



#Write a Python program to add member(s) to a set.
list={'ummon','kebyo','zuhra','Oybek'}
list.add('izmailov')
list


#Write a Python program to remove item(s) from a given set.
num={4, 6, 10, 12, 15, 22, 28, 31}
num.remove(10)
num


#Write a Python program to remove an item from a set if it is present in the set.
fruit={'gilos','olma','behi','qulupnay','nok','anjir','shaftoli','xurmo','uzum'}
select=input('sevgan mevangizni kiriting:')
if select in fruit:
    fruit.remove(select)
    print(f'ochirildi:{select}')
else:
    fruit.add(select)
    print(f'qoshildi:{select}')

print(fruit)
