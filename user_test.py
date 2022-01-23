from credentials import Credentials
from users import Users
import unittest

class TestCredential(unittest.TestCase):
    def tearDown(self):
        Users.user_credentials = []

    def setUp(self):
        '''
        this test runs before every test occurs
        '''
        self.new_credential = Users('tracy', 'mbone', 'star', '2000')

    def test_init(self):
        '''
        a test to assert whether the values entered would appear when the roperty is called
        '''
        self.assertEqual(self.new_credential.first_name, 'tracy')
        self.assertEqual(self.new_credential.last_name, 'mbone')
        self.assertEqual(self.new_credential.user_name, 'star')
        self.assertEqual(self.new_credential.credential, '2000')
+9
def test_save_credential(self):
        '''
        a test to check whether the save function works
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.user_credentials), 1)

def test_save_multiple_credentials(self):
        '''
        a test that checks whether both values appended to the array are actually present\ and returns the user itself
        '''
        self.new_credential.save_account()
        test_credentials = Credentials('abcd', 'efgh', 'ijkl', 'mnop')
        test_credentials.save_credential()
        self.assertEqual(len(Credentials.user_credentials), 2)

def test_del_credentials(self):
        '''
        test that check the delete function
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials('abcd', 'efgh', 'ijkl', 'mnop')
        test_credentials.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.user_credentials), 1)

def test_find_credential_by_username(self):
        '''
        test to check whether the function used to find credentials really works
        '''
        self.new_credential.save_credential()
        test_credential = Credentials('abcd', 'efgh', 'ijkl', 'mnop')
        test_credential.save_credential()
        found_credentials = Credentials.find_by_user_name('ijkl')
        self.assertEqual(found_credentials.user_name, test_credential.user_name)

def test_credential_exists(self):
        '''
        unlike the previous test this test returns a true/false soort of answer depending on whether the account exists or not
        '''
        self.new_credentials.save_credential()
        test_credentials = Credentials('abcd', 'efgh', 'ijkl', 'mnop')
        test_credentials.save_credential()
        test_credentials = Credentials.credential_exists('ijkl')
        self.assertTrue(Credentials)

def test_display_credentials(self):
        '''
        a test to check the display credentials function
        '''
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.user_credential)


if __name__ == '__main__':
    unittest.main()