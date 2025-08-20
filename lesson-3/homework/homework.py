#Create a list containing five different fruits and print the third fruit.
fruits=['olma','behi','gilos','nol','shaftoli']
print(fruits[2])


#Create two lists of numbers and concatenate them into a single list.
list1={1,2,33,66,22,666}
list2={100,1,55,2,777}
list2.union(list1)


#Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
list1=[1, 2, 22, 33, 55, 66, 100, 666, 777]
first = list1[0]
middle = list1[4]
last = list1[8]
list2=[first,middle,last]
print(list2)


#Create a list of your five favorite movies and convert it into a tuple.
movies=['Titanik','hobbit','dragon','Lord of ring','Drakula']
tuple=(type(movies))
print(f'Kinolar:{movies}')
print('tuple',tuple)



#Given a list of cities, check if "Paris" is in the list and print the result.
city=['Moskov','London','Tashkent','Bishkek','Paris']
if 'Paris' in city:
    print('result')
else:
    print('no result')

#Create a list of numbers and duplicate it without using loops.
num=[1,2,3,4,5,6,6,7,33,2]
number=list(set(num))
print(number)


#Given a list of numbers, swap the first and last elements.
num=[1,2,3,4,5,6,6,7,33,2]
num[0],num[9]=num[9],num[0]
print(num)



#Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
num=[1,2,3,4,5,6,7,8,9,10]
print(num[3:7])


#Create a list of colors and count how many times "blue" appears in the list
color=['blue','Red','purple','green','black','blue']
print(color.count('blue'))



#Given a tuple of animals, find the index of "lion".
animal=['tiger','graph','lion','snake','mpnkey','elephant']
print(animal.index('lion'))


#Create two tuples of numbers and merge them into a single tuple.
num1={1,2,3,55,77,245}
num2={11,22,66,431,657}
num1.union(num2)



#Given a list and a tuple, find and print their lengths.
num={1, 2, 3, 11, 22, 55, 66, 77, 245, 431, 657}
print(len(num))



#Given a tuple of numbers, find and print the maximum and minimum values.
num={1,2,3,4,5,6,7,8,9,10}
print(max(num))
print(min(num))


#Create a tuple of words and print it in reverse order.
word=('Izmailov Oybek')
print(word[::-1])



