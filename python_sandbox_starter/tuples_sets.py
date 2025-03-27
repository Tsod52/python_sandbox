# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
 #Create a tuple 
fruits =('apples', 'oranges', 'grapes')

print(fruits)

#Single value needs a trailing comma
fruits2 = ('Apples',)
print(fruits2)

#get value
print(fruits[1])

#Can't change a value 
#fruits[0] = 'Pears'

# Delete a tuple
del fruits2
#print(fruits2)

# A Set is a collection which is unordered and unindexed. No duplicate members.

#Create a set 
fruits_set = {'Apples', 'Oranges', 'Mango'}

#Check if in set 
print('Apples' in fruits_set)