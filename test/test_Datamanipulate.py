from Widgets.DataManipulate import data_manipulate
import unittest
import json
import pandas

class TestDatamanipulate(unittest.TestCase):

    def setUp(self):
        self.dt = data_manipulate()
        self.dt.load_data('data1.csv')
        self.dt.separated_dimension_measure()

    def test_is_dimension(self):
        self.assertTrue(self.dt.is_dimension('City'))
        self.assertTrue(self.dt.is_dimension('State'))
        self.assertFalse(self.dt.is_dimension('Profit'))
        self.assertFalse(self.dt.is_dimension('Discount'))

    def test_is_measure(self):
        self.assertTrue(self.dt.is_measure('Profit'))
        self.assertTrue(self.dt.is_measure('Discount'))
        self.assertFalse(self.dt.is_measure('City'))
        self.assertFalse(self.dt.is_measure('State'))
    
    def test_get_measure(self):
        self.assertIsInstance(self.dt.get_measure(), list)
    
    def test_get_dimension(self):
        self.assertIsInstance(self.dt.get_dimension(), list)

    def test_get_column(self):
        self.assertIsInstance(self.dt.get_column(), list)

    def test_get_unique(self):
        self.assertIsInstance(self.dt.get_unique('City'), list)
    
    def test_get_groupby(self):
        col = ['City']
        measure = {'Profit': 'sum'}
        data = self.dt.get_groupby(col, measure, {})['dataframe']
        sum_profit = self.dt.data.loc[self.dt.data['City'] == 'Henderson', 'Profit'].sum()
        self.assertEqual(round(data.loc[data['City']=='Henderson', 'Profit'].values[0], 2), round(sum_profit, 2))
    
    def test_check_date_col(self):
        self.assertTrue(self.dt.check_date_col('ship Date'))
        self.assertTrue(self.dt.check_date_col('hi date'))
        self.assertFalse(self.dt.check_date_col('City'))
        self.assertFalse(self.dt.check_date_col('State'))

