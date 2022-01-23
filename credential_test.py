from credentials import Credentials
import unittest


class TestCredentials(unittest.TestCase):
    def tearDown(self):
        '''
        this test clears the user_credentials array beore every test
        '''
        Credentials.user_credentials = []

    def setUp(self):
        '''
        this test creates a new instance of the credentials class
        before every test
        '''
        self.new_credential = Credentials('twitter', 'titanium1')

    def test_init(self):
        '''
        this test checks whether the data enterd into the properties if called will appear
        '''
        self.assertEqual(self.new_credential.page, 'twitter')
        self.assertEqual(self.new_credential.credential, 'titanium1')

    def test_save_page(self):
        '''
        this is a test to check whether the value append to the user_credentials array
        '''
        self.new_credential.save_page()
        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_save_multiple(self):
        '''
        this test like the first now test whether both instances created are appended to the array
        '''
        self.new_credential.save_page()
        test_pass = Credentials('linkedin', '7182')
        test_pass.save_page()
        self.assertEqual(len(Credentials.user_credentials), 2)

    def test_delete_page(self):
        '''
        this test checks for the delete function that uses the .remove methods
        '''
        self.new_credential.save_page()
        test_pass = Credentials('linkedin', '7182')
        test_pass.save_page()
        self.new_credential.delete_page()
        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_display_page(self):
        self.assertEqual(Credentials.display_page(), Credentials.user_credentials)

    def test_find_page(self):
        '''
        this test checks whether a credential saved can be searched
        '''
        self.new_credential.save_page()
        test_pass = Credentials('linkedin', '7182')  # new contact
        test_pass.save_page()
        found_page = Credentials.find_by_page('linkedin')
        self.assertEqual(found_page.page, test_pass.page)

    def page_exists(self):
        '''
        returns a true/false value depending on prescence of the searched credential
        '''
        self.new_Credential.save_page()
        test_pass = Credentials('linkedin', '7182')  # new contact
        test_pass.save_page()
        page_exist = Credentials.page_exists('linkedin')
        self.assertTrue(page_exist)


if __name__ == '__main__':
    unittest.main()