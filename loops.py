# 1. loop control statment

#break 
# for i in range(1,10):
#         if i == 5:
#             break
#         print(i)


# 2. continue

# for i in range(1,6):
#     if i == 3:
#         continue 
#     print(i)

# # 3. print number for 1 to 10 using for loop 

# for i in range(1, 11):
#     print(i)

# 4. print even numbers from 1 to 20

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i, end='') 
# for i in range(2, 21, 2):
#         print(i,end='')

# # 5.print odd number is 1 to 15
# for i in range(1, 16 ,2):
#         print(i)


# #6.print each character of using string 
# text = "krishna"
# for ch in text:
#     print(ch)


# #7.print all item in this list 
# my_list = [10, 20, 30, 40, 50]

# for i in range(len(my_list)):
#     print(my_list[i])


# # 8. print number is reverse order from 10 to 1
# for i in range(10, 0, -1):
#     print(i)

#what is function?
#A function is a block of code that runs only when it is called

# syntax
#def function_name():
    # code

#why we use function 
#1, Avoid reapeting code

# #example
# def greet():
#     print("Hello students")

# greet()

# #function with paramaters
# #used for pass values

# def greet(name="student"):
#     print("hello", (name))
# greet()
# greet("shreyarth")

# def add(a,b):
#     return a + b
# result = add(2,3)
# print(result)

loop.py file name