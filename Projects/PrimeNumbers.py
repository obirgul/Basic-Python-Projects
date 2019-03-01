num = int(input("Bir sayı giriniz = "))
x = "asal"
for x in range(2, int(num/2)):
    if (num % x) == 0:
        x = "asal degil"
        break

if x == "asal":
    print("Bu sayı asal")
else:
    print("asal değil")
