#união - union() ou | - traz apenas elementos únicos
A={1,2,3,4,5}
B={4,5,6,7,8}
"using | operator"
print(A | B)
"using union() method"
print(A.union(B))
#intersecção - intersection() ou & - apenas elementos que hajam em todos conjuntos
A={1,2,3,4,5}
B={4,5,6,7,8}
"using & operator"
print(A & B)
"using intersection() method"
print(A.intersection(B))
#diferença - difference() ou - apenas elementos que existam em um, mas não no outro conjunto
A={1,2,3,4,5}
B={4,5,6,7,8}
"using - operator"
print("A - B=",A - B)
print("B - A=",B - A)
"using difference() method"
print("A - B=",A.difference(B))
print("B - A=",B.difference(A))