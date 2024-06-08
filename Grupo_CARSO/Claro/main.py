import unittest
import HtmlTestRunner 

from TestCases.test_validation_TXT_CV import TestCases_validation_TXT_CV
from Locators.locators_validation_TXT_CV import Locators_validation_TXT_CV

class Claro(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass

    def test_Claro(self):
        tc = TestCases_validation_TXT_CV()
        tc.start()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=Locators_validation_TXT_CV.Evidence_path))