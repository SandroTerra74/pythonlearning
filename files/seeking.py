fp = open("data.txt","r")
print("Point position before reading is: ", fp.tell())
fp.seek(5)
print("Pointer position after manipulating is:", fp.tell())