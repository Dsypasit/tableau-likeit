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
    
    def get_type(self):
        return self.data.dtypes.tolist()

if __name__ == "__main__":
    d = data_manipulate()
    d.load_data('Superstore.csv')
    print(d.get_type())
