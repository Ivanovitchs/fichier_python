import os.path


'''f=open("monfichier.txt","w")
for i in range(1,10):
    f.write("\n"+str(i))
f.close() '''

fileName="monfichier.txt"
if os.path.exists(fileName):
    f1=open(fileName,"r")
    read=f1.read()
    print(read)
    f1.close()

else:
     print("Le fichier n'existe pas")

