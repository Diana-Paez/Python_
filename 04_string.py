from pipes import Template


quote = "I'm Nicolas"
print(quote)

quote2 = 'she said "Hello!"'
print(quote2)

#format

name = input("What is your name")
last_name = input("what is your last name")
age = input("What is your age")

#format string
template = "Hello, my name is " + name + ", my last name is " + last_name + " and my age is" + age

print("Version1", template)


template = "hello, my names is {}, my last name is {} and my age is {} ". format(name, last_name, age)
print("version2", template)

template = f"Hello, my name is {name}, my last name is {last_name} and my age is {age}"
print("Version 3", template)
