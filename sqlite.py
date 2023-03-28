import sqlite3

connexion=sqlite3.connect("albums.db")

create_table="""CREATE TABLE Article (
    article_id INTERGER Not Null PRIMARY KEY ,
    nom  VARCHAR   
)"""

create_table_album="""CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY , 
    artiste_id INTEGER REFERENCES Article,
    titre VARCHAR,
    annee_sortie INTEGER)
"""

curseur=connexion.cursor() #objet pour acceder aux requetes de la base de données
curseur.execute(create_table)
curseur.execute(create_table_album)

curseur.execute('INSERT INTO Article (article_id,nom) VALUES (1,"Michael Jackson");')
mj_id=curseur.lastrowid  #recuperer l'id du dernier element de la colone
curseur.execute('INSERT INTO Article (article_id,nom) VALUES (2,"Celine Dion");') 
cd_id=curseur.lastrowid



curseur.execute('INSERT INTO album (album_id ,artiste_id, titre, annee_sortie) VALUES (1, '+str(mj_id)+', "Thriller", 1982);')
curseur.execute('INSERT INTO album (album_id ,artiste_id, titre, annee_sortie) VALUES (2,'+str(mj_id)+', "Falling into You", 1996);')
curseur.execute('INSERT INTO album (album_id ,artiste_id, titre, annee_sortie) VALUES (3,'+str(cd_id)+', "Let\'s Talk About Love", 1997);')


connexion.commit()# garantir que toutes les requetes d'ecritures dans la base de données sont correctes
connexion.close()



