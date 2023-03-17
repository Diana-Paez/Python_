# CRUD Create, Read, Update, and Delete

from asyncio import tasks


numbers = [1,2,3,4,5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

#append
numbers.append(888)
print(numbers)

#insert
numbers.insert(0, "Hello")

numbers.insert(3, "change")
print(numbers)

tasks = ["todo 1", "todo 2", "todo3"]
new_list = numbers + tasks
print(new_list)

#index

index = new_list.index("todo 2")
new_list[index] = "todo chanded"

#pop
new_list.pop(0)
print(new_list)

#reverse
new_list.reverse()
print(new_list)

#short
numbers_a = [1,4,6,3]
numbers_a.sort()
print(numbers_a)