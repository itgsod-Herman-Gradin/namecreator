
        from nick.py import create_username

        # open the file
        with open('users.csv') as usersfile:

            # read lines
            for line in usersfile.readlines():
                # for every row split on
                user = line.strip().split(',')

                # put first value in firstname and the seconds value in
                firstname = user[0]
                lastname = user[1]
                birthday = user[2]
                number = randint(1, 21)

                username = create_username(firstname, lastname, number)

                # print out firstname, lastname and username
                print firstname, lastname, username


