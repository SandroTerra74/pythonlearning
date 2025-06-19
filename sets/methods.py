#método add
age={23,22,34,36,24,41}
age.add(56)
print(age)
#método remove
age.remove(22)
print(age)
#método pop
age.pop()
print(age)
#métodos issubset e issuperset
A={1,2,3}
B={1,2,3,4,5}
C={100,101,102}
print(A.issubset(B))
print(B.issuperset(A))
print(A.isdisjoint(B))
print(A.isdisjoint(C))
#iterações
bricsNations={"B","R","I","C","S"}
bricsNations.discard("Z")
print(bricsNations)
bricsNations.remove("Z")
print(bricsNations)