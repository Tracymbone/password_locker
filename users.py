class Users:
    def __init__(self, first_name, last_name, user_name, credential):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.credential = credential

    user_users = []

    def save_user(self):
        '''
        this is a save function that appends the account to the user_users array
        '''
        Users.user_credentials.append(self)

    def delete_user(self):
        '''
        a function used to delete a selected user
        '''
        Users.user_credentials.remove(self)
    @classmethod
    def find_by_user_name(cls, user_name):
        '''
        this is a function that checks whether the username provided by the username is available and if it is it returns the user
        '''
        for user in cls.user_users:
            if user.user_name == user_name:
                return user

    @classmethod
    def user_exists(cls, user_name):
        '''
        this function loops through the present array of users while searching for the username entered by the user and returns true/false
        '''
        for user in cls.user_users:
            if user.user_name == user_name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        return cls.user_users