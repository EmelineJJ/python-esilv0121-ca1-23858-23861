# Emeline JJ - 23858
# Francoise RUCH - 23861

# module to test our fonction and methods
import unittest
from bank import createPin
from bank import createAccountNumber
from bank import dictionary
from bank import Customer

#test class
class UneClasseDeTest(unittest.TestCase):

    def setUp(self):
        print("Before")

    def tearDown(self):
        print("After")

    #test for create code Pin
    def test_1(self):
        self.assertEqual(createPin('Joe', 'Smith'), str(1019) )
    
    #test for create account number
    def test_2(self):
        cust= Customer('1019','Joe','Smith','j@gmail.com')
        self.assertEqual(createAccountNumber(cust), 'js-8-10-19')

    #test of the index of a letter in a dictionnary
    def test_3(self):
        self.assertEqual(dictionary('u'), 21)

   


if __name__ == '__main__':
    unittest.main()
 