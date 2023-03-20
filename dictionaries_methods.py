#metodos de los diccionarios
person = {
    "name" : "Diana",
    "last_name" : "Paez",
    "lenguages" : ["python", "swift", "C"],
    "age" : 33

}

print(person)

#reemplazar
person["name"] = "Mercedes"
person["age"] -= 10
#agregar
person["lenguages"].append("dart")
print(person)

#eliminar
del person["last_name"]
person.pop("age")
print(person)

print("items")
print(person.items())

print("keys")
print(person.keys())


print("values")
print(person.values())