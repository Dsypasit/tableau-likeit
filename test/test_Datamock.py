
from Widgets.DataManipulate import data_manipulate
import unittest

class TestDatamanipulate(unittest.TestCase):

    def setUp(self):
        self.dt = data_manipulate()
        self.dt.load_data('mock data.xlsx')
        self.dt.separated_dimension_measure()
    
    def test_get_measure(self):
        self.assertIsInstance(self.dt.get_measure(), list)
    
    def test_get_dimension(self):
        self.assertIsInstance(self.dt.get_dimension(), list)

    def test_get_column(self):
        self.assertIsInstance(self.dt.get_column(), list)

    def test_get_unique(self):
        self.assertIsInstance(self.dt.get_unique('Name'), list)
    
    def test_get_groupby_sum(self):
        col = ['Name']
        measure = {'amout': 'sum'}
        data = self.dt.get_groupby(col, measure, {})['dataframe']
        pasit_amount = data.loc[data['Name'] == 'Pasit', 'amout'].values[0]
        norasate_amount = data.loc[data['Name'] == 'Norasate', 'amout'].values[0]
        self.assertEqual(pasit_amount, 15)
        self.assertEqual(norasate_amount, 66)

    def test_get_groupby_mean(self):
        col = ['Name']
        measure = {'amout': 'mean'}
        data = self.dt.get_groupby(col, measure, {})['dataframe']
        pasit_amount = data.loc[data['Name'] == 'Pasit', 'amout'].values[0]
        norasate_amount = data.loc[data['Name'] == 'Norasate', 'amout'].values[0]
        self.assertEqual(pasit_amount, 3)
        self.assertEqual(norasate_amount, 11)

    def test_get_groupby_max(self):
        col = ['Name']
        measure = {'amout': 'max'}
        data = self.dt.get_groupby(col, measure, {})['dataframe']
        pasit_amount = data.loc[data['Name'] == 'Pasit', 'amout'].values[0]
        norasate_amount = data.loc[data['Name'] == 'Norasate', 'amout'].values[0]
        self.assertEqual(pasit_amount, 5)
        self.assertEqual(norasate_amount, 11)

    def test_get_groupby_min(self):
        col = ['Name']
        measure = {'amout': 'min'}
        data = self.dt.get_groupby(col, measure, {})['dataframe']
        pasit_amount = data.loc[data['Name'] == 'Pasit', 'amout'].values[0]
        norasate_amount = data.loc[data['Name'] == 'Norasate', 'amout'].values[0]
        self.assertEqual(pasit_amount, 1)
        self.assertEqual(norasate_amount, 11)

    def test_get_groupby_count(self):
        col = ['Name']
        measure = {'amout': 'count'}
        data = self.dt.get_groupby(col, measure, {})['dataframe']
        pasit_amount = data.loc[data['Name'] == 'Pasit', 'amout'].values[0]
        norasate_amount = data.loc[data['Name'] == 'Norasate', 'amout'].values[0]
        self.assertEqual(pasit_amount, 5)
        self.assertEqual(norasate_amount, 6)