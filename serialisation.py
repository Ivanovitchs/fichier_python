
import json

'''
personne={
    "nom":"ivan",
    "age":25,
    "ami":["Sophie","Junior","Leael"]
}

personne_serialise=json.dumps(personne)

fichier_personne=open("Personne.txt","w")
fichier_personne.write(personne_serialise)
fichier_personne.close()

print(personne_serialise)'''

personne=open("Personne.txt","r")
donnees_personne=personne.read()
personne.close
donnees_json=json.loads(donnees_personne)
print(donnees_json)


