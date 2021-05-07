# Emeline JJ - 23858
# Francoise RUCH - 23861

# module to test our fonction and methods
import unittest
from bank import createPin
from bank import createAccountNumber
from bank import dictionary
from bank import Customer


class UneClasseDeTest(unittest.TestCase):

    def setUp(self):
        print("Avant le test")

    def tearDown(self):
        print("Après le test")

    def test_1(self):
        self.assertEqual(createPin('Joe', 'Smith'), str(1019) )
    
    def test_2(self):
        cust= Customer('1019','Joe','Smith','j@gmail.com')
        self.assertEqual(createAccountNumber(cust), 'js-8-10-19')

    def test_3(self):
        self.assertEqual(dictionary('u'), 21)

   


if __name__ == '__main__':
    unittest.main()
 