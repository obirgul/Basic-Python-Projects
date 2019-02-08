lights = ["green", "yellow", "red"]
from random import randint
currentlight = lights[randint(0,2)]
print(currentlight)

if currentlight == "green":
    print("go!")
elif currentlight == "yellow":
    print("ready")
elif currentlight == "red":
    print("wait") 