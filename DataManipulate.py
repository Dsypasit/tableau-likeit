import pandas as pd
class data_manipulate:
    def __init__(self):
        self.data = None
        self.column = None
        self.data_separated_date = None

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
    
    def separated_date(self):
        self.data_separated_date = self.data.copy()
        for col in self.column:
            for word in ['Date', 'date', 'DATE']:
                if word in col:
                    self.data_separated_date[col] = pd.to_datetime(self.data[col])
                    self.data_separated_date[col+'_month'] = self.data_separated_date[col].dt.month
                    self.data_separated_date[col+'_year'] = self.data_separated_date[col].dt.year
        print(self.data_separated_date.head())