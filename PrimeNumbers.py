num = int(input("Bir sayı giriniz = "))
x = "asal"
for x in range(2,num):
    if (num % x) == 0:
        x = "asal degil"
        break

x=="asal"
print("Bu sayı asal")
#else:
 #   print("asal değil")


#asal sayılarda hata veriyor4