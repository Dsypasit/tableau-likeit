import unittest
from Widgets.History import History

class testHistory(unittest.TestCase):

    def setUp(self):
        self.hist = History()
    
    def test_get_hist(self):
        self.assertIsInstance(self.hist.get_hist(), dict)