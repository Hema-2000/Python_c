#accessing items in list using for loop
Animals = ['Cat','Dog','Tiger','Cow']
for x in Animals:
    print(x)

#accessing items in dictionary using for loop
Languages = {'J':'Java','P':'Python'}
for key,value in Languages.items():
    print(key,value)

#using zip function loop iteration
a = ['Python','Java','CSharp']
b = [1,2,3]
for i,j in zip(a,b):
    print(i,j)

#nested for loops
list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']
for x in list1:
    for y in list2:
        print(x,y)

#find sum of elements in list
numbers = [12,3,56,67,89,90]
sum = 0
for n in numbers:
    sum += n
print(sum)

#print triangle
for i in range(1,5):
    for j in range(i):
        print('*',end='')
    print()

#sort the numbers(descending order)
numbers = [1,4,50,80,12]

for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if(numbers[i] < numbers[j]):
            temp = numbers[i]
            numbers[i] = numbers[j];
            numbers[j] = temp
print(numbers)


#print reverse order
for i in range(10,0,-1):
  print(i)