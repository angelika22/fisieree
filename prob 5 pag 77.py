vocale="aAbBcCdDeE"
y=0
with open("c:/Users/user/Desktop/aaa.txt", "r") as f:
    x=f.read()
with open("Text2.txt", "w") as f:
    for i in x:
        if i in vocale:
            f.write(i)
            y+=1
print("vocalele sunt", y)