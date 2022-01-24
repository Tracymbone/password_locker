#!/usr/bin/env python3.6
from users import Users
from credentials import Credentials


def create_credentials(first_name, last_name, user_name, credential):
    users = Users(first_name, last_name, user_name, credential)
    return users


def save_user(users):
    users.save_users()


def delete_users(users):
    users.delete_users()


def find_users(user_name):
    return Users.find_by_user_name(user_name)


def isexist_users(user_name):
    return Users.users_exists(user_name)


def display_users():
    return Users.display_users()


def create_page(page, credentials):
    credentials = credentials(page, credentials)
    return credentials


def save_page(credentials):
    credentials.save_page()


def find_page(pager):
    return Credentials.find_by_page(pager)


def isexist_page(pager):
    return Credentials.page_exists(pager)


def delete_page(credential):
    Credentials.delete_page()


def display_pages():
    return Credentials.display_page()


def main():
    print('WELCOME TO PASSWORD_LOCKER')
    print('Use the following numbers to pick their corresponding values')
    while True:

        print(" 1) LOGIN \n 2) SIGN UP \n 3) ABOUT PASSLOCK \n 4) DISPLAY ACCOUNTS \n 5) SIGN OUT")

        choice = int(input())
        if choice == 1:
            print('Enter username')
            username = input()
            print('Enter passoword')
            password = input()
            account = find_users(username)
            if account.user_name == username and account.password == password:

                print('logged in ')
                while True:

                    print(
                        f'Welcome {username}, Use the following numbers to select their corresponding          values')

                    print(
                        ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                    log_choice = int(input())
                    if log_choice == 1:
                        print('New page')
                        print('*'*100)

                        print('Page name')
                        page = input()

                        print('credentials')
                        password = input()

                    # created and saved page
                        save_page(create_page(page, Credentials))

                    elif log_choice == 2:
                        print("Enter the name of the page you want to delete")

                        page = input()
                        if isexist_page(page):
                            remove_page = (page)
                            delete_page(remove_page)

                        else:
                            print(f'I cant find {page}')

                    elif log_choice == 3:
                        if display_pages():
                            for pag in display_pages():
                                print(
                                    f'{pag.page}:{pag.credential}'
                                )
                        else:
                            print('NO CREDENTIAL SAVED YET')
                            print('\n')

                    elif log_choice == 4:
                        print('adios')
                        break
            else:
                print('wrong passwords')

        if choice == 2:
            print('NEW USERS')
            print('*'*100)

            print('FIRSTNAME')
            first_name = input()

            print('LASTNAME')
            last_name = input()

            print('USERNAME')
            user_name = input()

            print('CREDENTIALS')
            password = input()

            save_user(create_user(
                first_name, last_name, user_name, Credentials))
            # create and save a new user
            print('ACCOUNT FORMED')
            while True:

                print(
                    f'Welcome {user_name}, Use the following numbers to select their corresponding values')
                print(
                    ' 1) Save new credential \n 2) Delete credential \n 3) Display saved credential \n 4) Log out ')

                log_choice = int(input())
                if log_choice == 1:
                    print('New page')
                    print('*'*100)

                    print('Page name')
                    page = input()

                    print('credential')
                    Credentials = input()

                    # created and saved page
                    save_page(create_page(page, Credentials))

                elif log_choice == 2:
                    print("Enter the name of the page you want to delete")

                    page = input()
                    if isexist_page(page):
                        remove_page = (page)
                        delete_page(remove_page)

                    else:
                        print(f'I cant find {page}')

                elif log_choice == 3:
                    if display_pages():
                        for pag in display_pages():
                            print(
                                f'{pag.page}:{pag.credential}'
                            )
                    else:
                        print('NO CREDENTIAL SAVED YET')

                elif log_choice == 4:
                    break

        elif choice == 3:
            print('ABOUT PASSLOCK')
            print(
                '''
            Passlock is an sort of script application that allows you to store  password from different ccounts. In case of many accounts on social media passlock can be used to store the different password from the social media  accounts.Instead of having to use one password for all your sites so that you can remember  easily,you can use different password and store them in passlock and only have to remember your passlock password. This can prove to be very helpful especially  against hackers.
                                    ''')

        elif choice == 4:
            if display_users():
                for account in display_users():
                    print(
                        f'{Users.user_name}'
                    )
            else:
                print('NO USERS')

        elif choice == 5:
            print('adios')
            break


if __name__ == '__main__':
    main()