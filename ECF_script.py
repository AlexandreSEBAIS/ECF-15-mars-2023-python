# coding: utf-8

#####
# Par convention, on considérera les règles de création d'un nom d'utilisateur pour un compte Google
# comme règles de validité pour la partie locale d'une adresse mail.
# Elles sont disponibles à l'adresse : https://support.google.com/mail/answer/9211434?hl=fr
#
# Par conséquent :
# - Les lettres minuscules (a-z) ou majuscules (A-Z) et les chiffres (0-9) sont acceptées.
# - Les points (.) sont acceptés, sauf en début ou en fin de nom d'utilisateur.
#
# - L'esperluette (&), le signe égal (=), le trait de soulignement (_) sont interdits.
# - L'apostrophe (') est interdite.
# - Le tiret (-), le signe plus (+), la virgule (,) et les crochets (<,>) sont interdits.
#
# - Le nom d'utilisateur (la partie locale, avant l'arobase) doit faire entre 6 et 30 caractères.
#
#
# Par ailleurs et également par convention :
#
# - Les espaces sont interdits.
# - Les caractères accentués sont interdits.
# - Le point-virgule (;) est interdit.
# - Le backslash (\) est interdit pour éviter les échappements involontaires.
# - Les doubles-apostrophes (") pour éviter qu'une chaine de caractères soit mal interprêtée.
#
# - L'arobase (@) est réservée à la séparation de la partie locale et du nom de domaine.
#
# - Les points d'exclamation et d'interrogation (!,?) sont acceptés.
# - Les accolades ({,}) sont acceptées.
# - Le dièse (#) est accepté.
# - Le slash (/) est accepté.
# - L'astérisque (*) est accepté.
# - Le signe pourcentage (%) est accepté.
# - Le signe dollar ($) est accepté.
# 
# Tous les caractères non-cités précédemment sont considérés par défaut comme étant interdits.
#####
#####
# Pour les noms de domaine, par convention, seuls les lettres minuscules (a-z), les lettres majuscules (A-Z),
# les chiffres (0-9), les tirets (-) et le point (.) sont autorisés.
# Les lettres accentuées ne le sont pas.
#####
# Pour les extensions des noms de domaine, la question ne se pose pas vraiment ici
# puisque l'on ne cherche que les (.fr).
# On acceptera cependant les lettres minuscules comme majuscules.


import os
import re #Pour faire les regex

adresse_fichier = "C:/Users/Administrateur/Downloads/input-emails.txt"
fichier = open(adresse_fichier, 'r')
lines = fichier.readlines()
fichier.close()

pattern_mail = '[A-Za-z0-9!?{}#/*%$]{1}[A-Za-z0-9!?{}#/*%$.]{4,28}[A-Za-z0-9!?{}#/*%$]{1}@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'

res = list()
for i in range(len(lines)) :
    for elem in lines[i].split() :
        if re.fullmatch(pattern_mail, elem) : #Test du pattern mail
            if '..' not in elem and len(elem.split('@')[0]) in range(6,31) : #Test absence de '..' et longueur de la partie locale
                if elem[-3:] in ['.fr','.fR','.Fr','.FR'] : #Test extension '.fr'
                    res.append(elem)
for mail in res :
    print(mail)
