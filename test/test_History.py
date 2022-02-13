import unittest
from Widgets.History import History

class testHistory(unittest.TestCase):

    def setUp(self):
        self.hist = History()
    
    def test_get_hist(self):
        self.assertIsInstance(self.hist.get_hist(), dict)

    def test_check_file(self):
        self.assertTrue(self.hist.check_file('C:/Users/User/Desktop/softdev/tableau-likeit/data1.csv'))