# Namecreator

?r ett program som tar anv?ndare och f?rkortar deras namn efter en namngivnings policy. Programmet kr?ver 3 olika filer f?r att fungera,
Den f?rsta ?r users.csv, 09.19.py och herman.py

## anv?ndarnamn

Min namngivnigs algoritm och plicy ?r att man tar dem 3 f?rsta bokst?verna av f?rnamnet och dem 2 sista bokst?verna av efternamnet och sedan l?gger man till en slumpm?ssig siffra efter namnet f?r att
minsta risken att f? duplicationer i algoritmen.

ex

    Herman Gradin

Blir till

    HerGr9

 ### koden

 Users.csv
 herman gradin
andreas brun

09-19.py
#open the file

with open('users.csv') as usersfile:
    for line in usersfile.readlines():
        user = line.strip().split(',')
        firstname = user[0]
        lastname =  user[1]

        print firstname, lastname

herman.py

from random import randint
def create_username(firstname,lastname, number):

    username = firstname + lastname + number

    username = list(username)

    firstname = herman[:3]
    lastname = gradin[:2]
    number =




    return username[:1]


