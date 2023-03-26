f=open("monfichier.txt","w")

for i in range(1,10):
    f.write("\n"+str(i))
f.close()
f1=open("monfichier.txt","r")
read=f1.read()
print(read)
f1.close()

