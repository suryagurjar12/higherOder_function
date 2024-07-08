from functools import reduce

# reduce se totel sum 

# my_list=[13,20,35,47,47,87,65]
# x=reduce(lambda a,b: a+b,my_list)
# print(x)

# -------------------
# grater and lass. 
# my_list=[13,20,35,47,47,87,65]
# x=reduce(lambda a,b: a if a>b else b ,my_list)  # graterden >
# print(x)

# my_list=[13,20,35,47,47,87,65]
# x=reduce(lambda a,b: a if a<b else b,my_list) #lass <
# print(x)


#--------------filter---se even odd 

# my_list=[13,20,35,47,47,87,65]
# x=list(filter(lambda a: a%2==0 ,my_list))  #even
# print(x)


# my_list=[13,20,35,47,47,87,65]
# x=list(filter(lambda a: a%2!=0 ,my_list))  #odd
# print(x)


#-----map ---- add
# my_list=[13,20,35,47,47,87,65]
# x=list(map(lambda a:a+10,my_list)) #add
# print(x)

my_list=[13,20,35,47,47,87,65]
x=list(map(lambda a: a-5,my_list)) #sub -
print(x)