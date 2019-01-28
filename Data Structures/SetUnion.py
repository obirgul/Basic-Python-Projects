setA = {1,2,3,7,8,9}
setB = {1,2,3,4,5,6}

print(setA | setB) #birleşim
print(setA.union(setB))
print(setB.union(setA))

print(setB & setA) #kesişim
print(setA.intersection(setB))
print(setB.intersection(setA))

print(setA - setB) #fark
print(setB.difference(setA))
print(setA.difference(setB))

print(setA ^ setB) # A fark B + B fark A = birleşim - kesişim
print(setB.symmetric_difference(setA))
print(setA.symmetric_difference(setB))