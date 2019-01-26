students = ["ali", "veli", "ahmet"]

students.append("ayse")
students.remove("ahmet")

print(students[1])
print(students)

# lists constructor
cities = list(("istanbul", "Rio", "ankara", "Rio"))
print(str(len(cities)) + " " + str(cities))

# other functions

# print(students.clear()) tüm diziyi siler

print("Rio sayısı : "+ str(cities.count("Rio")))
cities.pop(3)
cities.insert(0,"Berlin")
print(cities)
