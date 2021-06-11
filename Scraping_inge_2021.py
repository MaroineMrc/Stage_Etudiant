import requests
from bs4 import BeautifulSoup
import time

#Il nous faut un url
'''
url = 'https://www.letudiant.fr/palmares/liste-profils/palmares-des-ecoles-d-ingenieurs/palmares-general-des-ecoles-d-ingenieurs/home.html#indicateurs=900716,900717,900718,900719&criterias'

#On effectue maintenant une requête

response = requests.get(url)  #Si print(reponse) renvoit <Response [200]> ça veut dire que c'est ok y'a pas de problème

if response.ok :
    print(response)
    print(response.headers)
    print(response.text) #Donne le code html de la page
    
    soup = BeautifulSoup(response.text, 'lxml') #Créer l'élement soup, permet de chercher des éléments dans le code source.
    #Par exemple :
    title= soup.find('title') #find permet de trouver des éléments en fonction d'un sélécteur css
    print(title.text) #Ca nous renvoit le titre de la page / le .text permet de ne pas afficher les balises
    tds = soup.findAll('td') #findAll permet de selectionner plusieurs élements
    print(len(tds))
    [print(str(td)+'\n\n') for td in tds]
    
    #On voit ici que y'a trop de balises. On veut seulement les balises associés à chaque école.
    
    links = []
    for td in tds:
        a=td.find('a') #Ce qui différencie les balises des écoles aux autres est le fait que les ecoles ont une balise <a class=...>
        if a :
            links.append(a['href'])
    print(links)

    #Maintenant on a une liste avec tout les liens qui nous interessent
    #Il faut maintenant les stocker
    
with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')
'''     
with open ('urls.txt', 'r') as file:
    for row in file: print(row)
    
url = 'https://www.letudiant.fr/palmares/palmares-des-ecoles-d-ingenieurs/isel-le-havre.html#'
response = requests.get(url)
if response.ok:
    soup=BeautifulSoup(response.text, 'lxml')
    Ecole=soup.find('h1', {'class':'c-hero__etablissement__info__name u-typo-h5'})
    Indesirables=[0,1,9,17,28,31,46,66]
    trs=soup.findAll('tr')
    Liste=['Ecole']
    for k in range(len(trs)):
        if k not in Indesirables :
            balise_bis=trs[k].find('td', {'class':'c-pmd-table__name'})
            Nom_Variable=balise_bis.find('a',{'class':'c-pmd-flex__item'})
            balise_bis_bis=trs[k].find('td',{'class':'c-pmd-table__value'})
            Valeur=balise_bis_bis.find('span',{'class':'u-typo-strong'})
            Liste.append(Nom_Variable.text)
    print(Liste)
            
            
with open ('urls.txt', 'r') as in_file:
    with open('donnees.csv', 'w') as out_file:
        for variable in Liste:
            out_file.write(variable + ';')
        out_file.write('\n')
        for row in in_file:
            url = row.strip()
            
            response = requests.get(url)
            if response.ok and row!='https://www.letudiant.fr/palmares/palmares-des-ecoles-d-ingenieurs/polytech-angers.html':
                soup=BeautifulSoup(response.text, 'lxml')
                Ecole=soup.find('h1', {'class':'c-hero__etablissement__info__name u-typo-h5'})
                Indesirables=[0,1,9,17,28,31,46,66]
                trs=soup.findAll('tr')
                Liste_bis=[Ecole.text]
                for k in range(len(trs)):
                    if k not in Indesirables :
                        balise_bis=trs[k].find('td', {'class':'c-pmd-table__name'})
                        Nom_Variable=balise_bis.find('a',{'class':'c-pmd-flex__item'})
                        balise_bis_bis=trs[k].find('td',{'class':'c-pmd-table__value'})
                        Valeur=balise_bis_bis.find('span',{'class':'u-typo-strong'})
                        Liste_bis.append(Valeur.text)
                for valeur in Liste_bis:
                    out_file.write(valeur.replace(';','/') + ';')
                out_file.write('\n')
            
            time.sleep(1)
    

url = 'https://www.letudiant.fr/palmares/palmares-des-ecoles-d-ingenieurs/polytech-angers.html#'
response = requests.get(url)
if response.ok:
    soup=BeautifulSoup(response.text, 'lxml')
    Ecole=soup.find('h1', {'class':'c-hero__etablissement__info__name u-typo-h5'})
    Indesirables=[0,1,9,17,28,31,46,66]
    trs=soup.findAll('tr')
    Liste=['Ecole']
    for k in range(len(trs)):
        if k not in Indesirables :
            balise_bis=trs[k].find('td', {'class':'c-pmd-table__name'})
            print(balise_bis)
            Nom_Variable=balise_bis.find('a',{'class':'c-pmd-flex__item'})
            balise_bis_bis=trs[k].find('td',{'class':'c-pmd-table__value'})
            Valeur=balise_bis_bis.find('span',{'class':'u-typo-strong'})
            Liste.append(Nom_Variable.text)
            print('OK')
    print(Liste)            
            
            
