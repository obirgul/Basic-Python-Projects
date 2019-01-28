StudentsSet = {"Ahmet","Ayşe","Ali"}
print(StudentsSet)

for student in StudentsSet :
    print(student)

print("Ayşe" in StudentsSet)

if "Ayşe" in StudentsSet :
    print("Listede var")

StudentsSet.add("Veli")
StudentsSet.update(["Derin","Deren"])
print(StudentsSet)

StudentsSet.remove("Ahmet")
StudentsSet.discard("ayse") #Eğer ayse isimle varsa siler yoksa hata vermez
print(StudentsSet)