
#FOR

for element in range(20):
 print(element)

for element in range(1, 20):
 print(element)

 my_list = [23, 56, 78, 99, 136]
 for element in my_list:
  print(element)

  my_tuple = ("lili", "pepe", "lulo")
  for element in my_tuple:
   print(element)

   product = { 

    "name": "shoes",
    "price": 100,
    "stok": 6

   }

   for key in product:
    print(key, "=>", product[key])

    for key, value in product.items():
     print(key, "=>", value)

people = [
 {
  "name": "Diana",
  "age": 32
 },
 {
  "name": "James",
  "age": 34
 },
 {
  "name":"Emili",
  "age": 55
 }
]

for person in people:
 print(person)


