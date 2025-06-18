fp = open("data.txt",'r')
print("Point position before reading is: ",
fp.tell())
print(fp.read())
print("Pointer position after reading is:",
fp.tell())