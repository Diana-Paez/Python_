#diccionarios

my_dict = {}
print(type(my_dict))

my_dict = {
    "dart" :  "flutter",
    "swift" : "swiftUI",
    "name" : "Luisa",
    "last_name" : "Guti",
    "age" : 7
}

print(my_dict)
print(len(my_dict))

print(my_dict["age"])
#print(my_dict["gggg"]) #aqui me salta error porque ese string no esta en el diccionario, bueno manejarlo con el .get
print(my_dict.get("U")) # con el get puedo darle manejo a los errores cuando no se encuentra

print("name" in my_dict)
print("fff" in my_dict)