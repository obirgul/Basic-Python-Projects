import MathamaticalMethods as math

print("YAPMAK İSTEDİĞİNİZ İŞLEMİ BOŞLUK VEREREK YAZIN")
print("örnek işlem 24 / 6 ")
a = str(input("---->>> "))
if a.split()[1] == "+":
    math.topla(a.split()[0],a.split()[2])

elif a.split()[1] == "*":
    math.carp(a.split()[0],a.split()[2])

elif a.split()[1] == "/":
    math.bol(a.split()[0],a.split()[2])

elif a.split()[1] == "-":
    math.cikar(a.split()[0],a.split()[2])

elif a.split()[1] == "**":
    math.us(a.split()[0],a.split()[2])