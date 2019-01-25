text = "Hello from the Heart of the world"

#substring
newtext = text[6:14]
newtext2 = text[:13]

print(text)
print(newtext)
print(newtext2)

#len
print(len(text))

newtext3 = text[len(text)-1:len(text)]
print(newtext3)

#lower upper
print(text.upper())
print(text.lower())

#Replace
print("replaced text : "+text.replace("t","W"))
print(text)

#split
print(text.split())
info = "Hello,from,the,Heart,of,the,world"
print(info.split(","))
print("4. kelime : "+info.split(",")[3])

#input
sayi1 = input("sayı 1 = ")
sayi2 = input("sayı 2 = ")
print(sayi1 + sayi2)
print(int(sayi1) + int(sayi2))