# function with 2 keyword arguments grade and school
# default arguments example
# def student(name, age, grade="Five", school="ABC School"):
#     print('Student Details:', name, age, grade, school)
#
# # not passing a school value (default value is used)
# student('Kelly', 12, 'Six') # six is assigned to grade
# student('Jessa', 12, 'Seven', 'XYZ School') # passign all arguments

#keyword arguments

#Positional arguments
# def student(name,age):
#     print(name, age)
#
# student('kavya',30)
# student('sai',20,36) #TypeError: student() takes 2 positional arguments but 3 were given



#Variable-length arguments
# def percentage(*args): #it will take inputs aa tuple
#     sum = 0
#     for i in args:
#         sum = sum + i
#     avg = sum / len(args)
#     print('Average =', avg)
#
# percentage(56, 61, 73)
# percentage(34,67)


#arbitrary keyword arguments
def percentage(**kwargs): #it takes input as dictionary
    sum = 0
    for sub in kwargs:
        sub_name = sub  # get argument name
        sub_marks = kwargs[sub] # get argument value
        print(sub_name, "=", sub_marks)
        sum = sum + sub_marks
    avg = sum / len(kwargs)
    print('Average =', avg)

# pass multiple keyword arguments
percentage(math=56, english=61, science=73)


