lista1=[]
note=[]
with open("c:/Users/User/Downloads/clasa.txt", "r") as f:
    lista=f.readlines()
    for i in lista:
        lista1.append(i[0:-1])
print("nume", "prenume", "nota", "limba")
for i in lista1:
    print(i)
    for a in i.split():
        if a.isdigit():
            note.append(int(a))
print("nota medie a clasei- ", sum(note)/len(note))
with open("Germana.txt", "w") as g:
    y=[]
    s=0
    g.write("nume"+"prenume"+"nota"+"limba"+"\n")
    for i in lista1:
        if i [-3:-1]=="an":
            g.write(str(i)+"\n")
            for a in i.split():
                if a.isdigit(): 
                    y.append(int(a))   
    g.write("nota medie a grupei de germana- " + str(round(sum(y)/len(y), 2)))    
with open("Engleza.txt", "w") as e:
    x=[]
    s=0
    e.write("nume"+"prenume"+"nota"+"limba"+"\n")
    for i in lista1:
        if i [-3:-1]=="ez":
            e.write(str(i)+"\n")
            for a in i.split():
                if a.isdigit(): 
                    x.append(int(a))   
    e.write("nota medie a grupei de engleza- " + str(round(sum(x)/len(x), 2)))    