
import json


personne={
    "nom":"ivan",
    "age":25,
    "ami":["Sophie","Junior","Leael"]
}

personne_serialise=json.dumps(personne)

fichier_personne=open("Personne.txt","w")
print(personne_serialise)
fichier_personne.write(personne_serialise)
fichier_personne.close()