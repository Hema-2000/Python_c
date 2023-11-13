#Arithmetic operator using pedmas
print( 5 + (4 - 2) * 2 + 4 % 2 - 4 // 3 - (5 - 3) / 1) #6.0

print(10-7//2*3+1) #2

print(0.2 * ( 0.6 // 0.2 ) + 0.6 % 0.2)#0.6

print(30 / 2 * 5 + (10 + 5) - 3)#87.0

print(2 ** 4 + 11 % 5 - (20 / 2) + 13 // 2 * 3)#25.0

print(((27 * 2) + 46) ** 0.5)#10.0

#example for membership operator

x = 'Hello world'
y = {1:'a', 2:'b'}

# check if 'H' is present in x string
print('H' in x)  # prints True

# check if 'hello' is present in x string
print('hello' not in x)  # prints True

# check if '1' key is present in y
print(1 in y)  # prints True

# check if 'a' key is present in y
print('a' in y)  # prints False


#example for identity operator

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False

x = 10
y = 50


#example programs for bit wise operators
# Swapping using xor
x = x ^ y
y = x ^ y
x = x ^ y

print("Value of x:", x)
print("Value of y:", y)

         #(or)
a = 5
b = 1
a = (a & b) + (a | b)
b = a + (~b) + 1
a = a + (~b) + 1
print("a after swapping: ", a)
print("b after swapping: ", b)



