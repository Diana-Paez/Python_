#tuplas
numbers = (1, 2, 3, 5)
strings = ("Luis", "Martha", "Cecilia", "Luis")
print(numbers)
print("0 =>", numbers[0])
print("-1 =>", numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

#las tuplas son in mutables en python, no se pueden modificar, si lo quiero hacer debo de comvertilas a listas

#CRUD
#numbers.append(10)
print(numbers)
#numbers[1] = "change"

print(strings)
print(strings.index("Martha"))
print(strings.count("Martha"))

my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = "Dana"
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)


