import PyDictionary as e
h = e.PyDictionary()
f = open("three.txt")
x = open("meaning_three.txt","a")
for i in f:
    print(i)
    print(h.meaning(i))
    if h.meaning(i) != None:
        if len(h.meaning(i))>0:
            x.write(i)

