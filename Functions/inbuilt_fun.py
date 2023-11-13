#to find max number with in given 2 numbers
Max = lambda a, b: a if (a > b) else b
print(Max(1, 2))

#multiply 2 numbersw using lambda function
a = lambda x, y : (x * y)
print(a(4, 5))

#adding 3 numbers
a = lambda x, y, z : (x + y + z)
print(a(4, 5, 5))


#filter function to print filtered values
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)#it takes each value from list for each iteration

for x in adults:#if condition true then only x value prints
  print(x)


# it produces odd values by using lambda and filter functions
list_ = [35, 12, 69, 55, 75, 14, 73]
odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ))
print('The list of odd number is:',odd_list) # [35, 69, 55, 75, 73]


#using filter and lambda
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
print(adults)

def addition(n):
    return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result)) #[2,4,6,8]

#map with lambda function
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(final_list)

numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]
squared_list = list(map( lambda num: num ** 2 , numbers_list ))
print( 'Square of each number in the given list:' ,squared_list )

#for reduce function we need import functools
from functools import reduce
nums = [1, 2, 3, 4]
ans = reduce(lambda x, y: x + y, nums) #(((1+2)+3)+4).
print(ans) #10


#reduce function including lambda
import functools
# initializing list
lis = [1, 3, 5, 6, 2, ]
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))



#generator function
def my_generator(n):
    value = 0  # initialize counter
    while value < n: # loop until counter is less than n
        yield value  # produce the current value of the counter
        value += 1  # increment the counter

# iterate over the generator object produced by my_generator
for value in my_generator(3):
    print(value)  # print each value produced by generator


