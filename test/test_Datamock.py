
from Widgets.DataManipulate import data_manipulate
import unittest
import pandas as pd
class TestDatamanipulate(unittest.TestCase):

    def setUp(self):
        self.dt = data_manipulate()
        self.dt.load_data('mock data.xlsx')
        self.dt.separated_dimension_measure()
    
    def test_get_data(self):
        self.assertIsInstance(self.dt.get_data(), list)

    def test_get_measure(self):
        self.assertIsInstance(self.dt.get_measure(), list)
    
    def test_get_dimension(self):
        self.assertIsInstance(self.dt.get_dimension(), list)

    def test_get_column(self):
        self.assertIsInstance(self.dt.get_column(), list)

    def test_get_unique(self):
        self.assertIsInstance(self.dt.get_unique('Name'), list)
        self.assertListEqual(self.dt.get_unique('Name'), ['Pasit', 'Norasate'])
    
    def test_is_measure(self):
        self.assertTrue(self.dt.is_measure('amout'))
        self.assertFalse(self.dt.is_measure('Name'))

    def test_is_dimension(self):
        self.assertTrue(self.dt.is_dimension('Name'))
        self.assertFalse(self.dt.is_dimension('amout'))
    
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

    def test_get_groupby_filter_dimension(self):
        col = ['Name']
        measure = {'amout': 'count'}
        fil = {'Name': ["Pasit"]}
        data = self.dt.get_groupby(col, measure, fil)['dataframe']
        name = data['Name'].unique()
        self.assertEqual(name, ['Pasit'])

    def test_get_groupby_filter_measure(self):
        col = ['Name']
        measure = {'amout': 'max'}
        fil = {'amout': {'condition':'>', 'value': 7, 'state': True}}
        data = self.dt.get_groupby(col, measure, fil)['dataframe']
        value = data['amout']
        for i in value: 
            self.assertGreater(i, 7)
    
    def test_measure_condition(self):
        self.assertEqual(self.dt.measure_condition('test', '==', 10), "`test` == 10")
        self.assertEqual(self.dt.measure_condition('good', '>=', 10), "`good` >= 10")
    
    def test_union_data(self):
        self.dt.unioun_data('mock data copy.xlsx')
        name = ['Pasit']*5+['Norasate']*6+['Pasit']*2+['Norasate']*2
        df = pd.DataFrame({'Name':name, 'amout':[1,2,3,4,5,11,11,11,11,11,11,6,7,12,12]})
        self.assertEqual(self.dt.data.values.tolist(), df.values.tolist())

    def test_import_data(self):
        dt = data_manipulate()
        dt.load_data("mock data.xlsx")
        # self.dt.unioun_data('mock data copy.xlsx')
        name = ['Pasit']*5+['Norasate']*6
        df = pd.DataFrame({'Name':name, 'amout':[1,2,3,4,5,11,11,11,11,11,11]})
        self.assertEqual(dt.data.values.tolist(), df.values.tolist())