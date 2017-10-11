
from nick import create_nick
from random import randint

# open the file
with open('users.csv') as usersfile:

    # read lines
    for line in usersfile.readlines():
        # for every row split on00
        user = line.strip().split(',')

        # put first value in firstname and the seconds value in
        firstname = user[0]
        lastname = user[1]
        number = randint(1, 21)

        username = create_nick(firstname, lastname, number)

        # print out firstname, lastname and username
        print firstname, lastname, username


