import json  #pour analyser le JSON
from datetime import datetime

"""
            dict=json.load(file-io)  <---load----- file  
                                     ----dump----->json.dump(dict, file-io)
 dict list
             dict=json.loads(str)  <---loads----- string  
                                     ----dumps----->json.dumps(dict)
load(s) pour lire dans python
dump(s) ecrire vers  un fichier ou string pour (dumps)

"""
#load(s) transforme en python object (lire en python le json
#dict=json.load(file-io) (équivalent fichier)  dict=json.loads(str) (str équivalent string)
#dump(s) vers un fichier/string  permet d'écrire vers
#json.dump(dict, file-io)    str=json.dumps(dict)

""" user.json
{
  "name": "John",
  "age": 50,
  "is_married": false,
  "profession": null,
  "hobbies": ["traveling", "photography"]
}
"""
#on met le contenu du fichier dans une variable
with open('user.json') as user_file: #on ouvre avec open et attribue les données de flux à user_file.
  file_contents = user_file.read()#avec read on transmet le contenu textuel dans la variable.
print(file_contents) #la variable contient une version stringifiée du json

#Analyser le fichier avec les méthode json
parsed_json = json.loads(file_contents)#permet de posséder un dictionnaire valide pour accèder aux clés/valeurs.
print(parsed_json)
#{'name': 'John', 'age': 50, 'is_married': False, 'profession': None, 'hobbies': ['traveling', 'photography']}
#dictionary = json.loads(open("user.json","r").read()) #En une ligne


with open('user.json') as user_file:
  parsed_json = json.load(user_file) #load permet d'analyser en même temps que lire l'objet
print(parsed_json)
#dictionary = json.load(open("user.json","r")) #En une ligne


#****dump/dumps****
d1 = {'alpha': 1, 'beta': 2}
s = json.dumps(d1)#la variable contient le json mais reste à l'écrire
open("out.json","w").write(s)

d2 = {'alpha': 1, 'beta': 2}
json.dump(d2, open("out2.json","w"))#ecrit le fichier
#Notez que le json. dump () nécessite un descripteur de fichier ainsi qu'un obj, dump(obj, fp ...).
print("\n**********************Utilisation*********************\n")
"""
EXEMPLE:
nous allons convertir le dictionnaire Python en JSON et l'écrire dans un fichier texte. 
Ensuite, nous lirons le fichier et jouerons avec.

"""
#nous allons construire un dictionnaire Python comme ceci
# Quatre forces fondamentales avec JSON
d = {}

d ["gravité"] = {
"médiateur": "gravitons",
"force relative" : "1",
"gamme" : "infini"
}
d ["faible"] = {
"médiateur": "Bosons W/Z",
"force relative" : "10^25",
"plage" : "10^-18"
}
d ["électromagnétique"] = {
"médiateur": "photons",
"force relative" : "10^36",
"gamme" : "infini"
}
d ["strong"] = {
"médiateur": "gluons",
"force relative" : "10^38",
"plage" : "10^-15"
}
print(type(d))
print(d)
print("convertir le dictionnaire en chaîne (liste) avec dumps")
donnees = json.dumps(d)# dump(s) renvoie une chaine comme indiqué le s (Encodage)
print(type(donnees))
print(donnees)
with open ("4forces.json","w") as f: #Ecrire dans un fichier
    f.write(donnees)
#relire le fichier 
#décode la chaine codée en json  dans une structure de données de dictionnaire python
with open ("4forces.json","r") as f:
    donnees = f.read()
#decoder le json en dictionnaire
d = json.loads(donnees)

#trouver la forces relative de l'électromagnétisme par rapport à la gravité?
print(d["électromagnétique"]["force relative"])
#Qui est le médiateur de la force « forte » ?
print(d["strong"]["médiateur"])
print(type(d))
print(d)
print("**nous préférons travailler avec des fichiers plutôt qu'avec des chaînes json.dump-encoder/jsonload-decoder***")
#ecrire dans un fichier
with open("4forcess.json","w") as f:
    json.dump(d,f)
#le relit
with open("4forcess.json","r") as f:
    d=json.load(f)
print(type(d))
print(d)

print("exemple simple")
in_dict = {"a":1,"b":2}
with open("out2.json","w") as fw :
    json.dump(in_dict, fw)#dict list --->  file (dict, file.io)
with open("out2.json","r") as fr :
  out_dict = json.load(fr) #dict list <--- file (dict, file.io)
print(type(out_dict))
print(out_dict)

with open("out2.json", "r") as fr :
    out_str = fr.read()
out_dict = json.loads (out_str)
print(type(out_dict))
print(out_dict)

in_str = json.dumps (in_dict)
with open("out3.json","w") as fw :
    fw.write(in_str)

#print( json.dumps(datetime.now(), default=json_serial))


#verifie l'objet serialisable car nous pouvons serialiser et le reste en string 
#mais parfois il y a des problème pour la deserialisatio
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))