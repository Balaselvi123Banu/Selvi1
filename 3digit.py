import PyDictionary as e
h = e.PyDictionary()
f = open("three.txt")
print("Hiii")
for i in f:
    print(i)
    print(h.meaning(i))
    if h.meaning(i) != None:
        if len(h.meaning(i))>0:
            x.write(i)

