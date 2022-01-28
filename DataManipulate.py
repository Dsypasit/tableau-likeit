import pandas as pd
class data_manipulate:
    def __init__(self):
        self.data = None
        self.column = None

    def load_data(self, filename):
        try:
            self.data = pd.read_csv(filename, encoding='windows-1252')
            self.column = self.data.columns
        except UnicodeDecodeError:
            self.data = pd.read_csv(filename, encoding='utf8')
            self.column = self.data.columns

    
    def get_data(self):
        return self.data.values.tolist()

    def get_column(self):
        return self.column.tolist()
    
    def check_dimension_name(self, s):
        l = ['id', 'ID', 'Id', 'Code', 'CODE']
        for i in l:
            if i in s:
                return True
        else :
            return False
    
    
    def separated_dimension_measure(self):
        self.dimension = []
        self.measure = []

        for colname, coltype in self.data.dtypes.iteritems():
            if coltype == 'object' or self.check_dimension_name(colname): self.dimension.append(colname)
            else : self.measure.append(colname)
    
    def is_dimension(self, s):
        return s in self.dimension

    def is_measure(self, s):
        return s in self.measure
    
    def get_dimension(self):
        return self.dimension

    def get_measure(self):
        return self.measure
    
    def get_groupby(self, col, measure):
        if len(measure) > 0:
            data = self.data.groupby(col, as_index=False).agg(measure)
        else:
            data = self.data.groupby(col, as_index=False).mean()
            data = data.iloc[:,:len(col)]
            # data = self.data[col]

        def get_col():
            return data.columns.tolist()
        return {'data': data.values.tolist(), 'col': get_col()}



if __name__ == "__main__":
    d = data_manipulate()
    d.load_data('Superstore.csv')
    d.separated_dimension_measure()
    # print('m',d.get_measure())
    # print('d',d.get_dimension())
    # data = d.data
    # p = ['Sales', 'Discount']
    # print(data.groupby(['Region']).mean())
    di = ['State', 'City']
    # me = { 'Sales': 'sum', 'Discount':'sum' }
    me = {}
    x = d.get_groupby(di, me)
    # print(x['data'][:5])
    # print(x.keys())
    # print(x['col'])

