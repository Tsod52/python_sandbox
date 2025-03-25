# A List is a collection which is ordered and changeable. Allows duplicate members.

# create a list 
num = [1,2,4,5,6,1,43]
fruits = ['apples', 'oranges', 'Grapes', 'Papers']

#use a constructor
num2 = list((1,2,4,5,6,1,43))

print(num,num2)

#Get a value 
print(fruits[1])

#get length 
print(len(fruits))

#Append to list 
fruits.append('Mangos')

#Remove from list 
fruits.remove('Grapes')

#Insert into position
fruits.insert(2,'Straberries')

#remove with pop
fruits.pop(2)

#reverse List
fruits.reverse()

#Sort List 
fruits.sort()

print(fruits)



