import json
import os


def pex2():
   nom="ex2.json"
   diccionari={}
   # Si existeix el fitxer, el llegim i el guardem en el diccionari
   if os.path.isfile(nom):
       with open(nom,"r") as f:
           diccionari=json.load(f)
   b=''
   while b!='.':
       print(""" Menú fitxers:
           1. Crear una tasca
           2. Eliminar una tasca
           3. Modificar una tasca
           4. Mostrar totes les tasques
           5. Guardar-ho al fitxer per continuar treballant
           6. Sortir
       """)
       b = int(input("Elegeixi l'opció: "))
       match(b):
           case 1: # Crear tasca
               n = len(diccionari)+1
               diccionari[str(n)]=input("Introdueixi la tasca desenvolupar: ")
           case 2: # Eliminar tasca
               for x,y in diccionari.items():
                   print("{}: {} \n".format(x,y))
               n=input("Indiqui el número de la tasca a eliminar: ")
               diccionari.pop(n)
               for x,y in diccionari.items():
                   print("{}: {} \n".format(x,y))               
           case 3: # Modificar un element
               for x,y in diccionari.items():
                   print("{}: {} \n".format(x,y))
               n=input("Indiqui el número de la tasca a modificar: ")
               diccionari[n]=input("Introdueixi el nou valor per a la tasca: ")
               for x,y in diccionari.items():
                   print("{}: {} \n".format(x,y))
           case 4:#Llistar
               for x,y in diccionari.items():
                   print("{}: {} \n".format(x,y))
           case 5: #Guardar-ho al fitxer abans de sortir de l'app
               with open(nom,"w") as f:
                   json.dump(diccionari,f,indent=4)   
               with open(nom,"r") as f:
                   diccionari=json.load(f)              
           case 6: # Sortir
               with open(nom,"w") as f:
                   json.dump(diccionari,f,indent=4)
               print("Adéu \n")
               b="."
           case other:
               print("Opció no vàlida \n")  
# Si voleu provar la lliberia abans de dur-la al fitxer principal.py
# pex2()
