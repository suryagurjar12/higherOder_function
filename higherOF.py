# my_list=[10,20,30,40,]
# def sqr(n):
#     return n*n
# x=map(sqr,my_list)
# print(x)
# print(list(x)

# -------------------------------- tuple-------------


# my_tuple=[10,20,30,40,]
# def sqr(n):
#     return n*n
# x=map(sqr,my_tuple)
# print(x)
# print(list(x))


# -----------------------------string----------------
# my_str="neeraj"
# def add(n):
#     x=ord(n)
#     return x
# x=map(add,my_str)
# print(x)
# print(list(x))

# ----------------------------------------charater--------

# my_str="neeraj"
# def add(n):
#      x=ord(n)
#      return chr(x+5)
# x=map(add,my_str)
# print(x)
# print(list(x))


# ------------------------------------------------------------------------------------
# --------------------Filter--------------------------
# my_list=[60,10,70,90,55,75,10,20,40]
# def fun(n):
#      if n>=60:
#           return True
# x=filter(fun,my_list)
# print(x)
# print(list(x))



# 

    
    

# -------------------------even numbers--------
# def check_even(numbers):
#      if numbers% 2 == 0:
#           return True
#      return False
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_numbers_iterator=filter(check_even,numbers)
# even_numbers=list(even_numbers_iterator)
# print(even_numbers)

# ------------------------------------------------------------------------------

# --------------lambda funcation----------------

# print hello surya
# user=lambda name:print('hello',name)
# user('surya')
# y=lambda x,y:x*y
# print(y(20,30))


# user=lambda name:print('goodmornnig',name)
# user('surya')


# x=lambda p,q,r: 3*p+4*q+5*r+10
# print(x(10,20,30))
my_list=[3,4,5,6,7,6,5,]

x=filter(lambda e: e>=4,my_list )
print(list(x))

# sqr=lambda n,m: 2*n+2*m
# print(sqr(8,7))

# ---------------------------------------------------------------------------

# -----------------Reduce-----------------------

# import functools
# my_list=(10,20,60,30,40)
# def greater(a,b):
#      if a>b:
#           return a
#      else:
#           return b
# x=functools.reduce(greater,my_list)
# print(x)

# import functools
# my_list="surya"
# def lowest_digit(a,b):
#      if a>b:
#           return a
#      else:
#           return b
# x=functools.reduce(lowest_digit,my_list)
# print(x)

# import functools
# my_list="surya"
# def greater(a,b):
#      if a>b:
#           return a
#      else:
#           return b
     
# x=functools.reduce(greater,my_list)
# print("the char have greater asci value of",x)

# -----------------------------Decorater-------------------

# def decorater(fun):
#     def website():
#         print("welcome to my webside")
#         fun()
#         print("thank you for vist")
#     return website
# @decorater
# def original_fun():
#     print("this is my website")
# original_fun()


# def decorater (fun):
#     def house():
#         print("shri ram gurjar")
#         fun()
#         print("shri sitaram gurjar")
#     return house
# @decorater
# def original_fun():
#     print("aanand bhavan")
# original_fun()

# ------------------------------------------------------------------------------------------------

# -------------------Generators------------------

# def my_fun(x,y):
#     while x<=y:
#         yield x
#         x+=1
# var=my_fun(5,10)
# print("first object generator:",next(var))
# print("first object generator:",next(var))
# print("first object generator:",list(var))


# def my_fun(x,y):
#     while x<=y:
#         yield x
#         x +=1
        
# var=my_fun(1,100)
# print("first object generatoer:",next(var))
# print("first object generatoer:",next(var))
# print("first object generatoer:",list(var))