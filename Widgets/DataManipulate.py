import pandas as pd
import pandas 
import hashlib

# from Widgets.History import History
class data_manipulate:
    """
    data_manipulate class is object for manipulate data to pyqt

    ...

    Attributes
    ----------
    data : pandas.core.frame.DataFrame
        keep data as dataframe
    column : list
        column of data
    dimension : list
        dimension column of data
    measure : list
        measure column of data
    hist : History
        manipulate history object
    filename : str
        collect current filename


    """
    def __init__(self):
        self.data : pandas.core.frame.DataFrame = None
        self.column : list = []
        self.data_separated_date = None
        self.dimension : list = []
        self.measure : list = []
        self.hist : History = History()
        self.filename : str = ""

    def load_data(self, filename:str) -> None:
        """
        import csv file, exel file to data and drop blank row

        Parameters
        ----------
        filename: str
            path of csv file, excel file
        """
        self.filename = filename
        if filename.split('.')[-1] == "csv":
            try:
                self.data = pd.read_csv(filename, encoding='windows-1252')
                self.column = self.data.columns
                self.data = self.data.dropna()
            except UnicodeDecodeError:
                self.data = pd.read_csv(filename, encoding='utf8')
                self.column = self.data.columns
                self.data = self.data.dropna()
        else:
            self.data = pd.read_excel(filename)
            self.column = self.data.columns
            self.data = self.data.dropna()


    
    def get_data(self) -> list:
        """
        get values of data to list

        Returns
        -------
        list
            values of data
        """
        return self.data.values.tolist()

    def get_column(self) -> list:
        """
        get column of data to list

        Returns
        -------
        list
            columns of data 
        """
        return self.column.tolist()
    
    def check_dimension_name(self, s:str) -> bool:
        """
        check column name. if column name match with id, ID, Id, Code, CODE
        then it's dimension.

        Parameters
        ----------
        s : str
            column name

        Returns
        -------
        bool
            if dimension return true, else return false 
        """
        l = ['id', 'ID', 'Id', 'Code', 'CODE']
        for i in l:
            if i in s:
                return True
        return False
    
    def separated_dimension_measure(self) -> None:
        """
        This method will separated column to measure list, dimension list.
        if history have filename then use measure and dimension in history.
        """
        self.separated_date()
        hist_dict = self.hist.get_hist()    # get dict of history
        hash_name = self.getMd5(self.filename)
        if hash_name in hist_dict.keys():   # check that filename in history
            self.dimension = hist_dict[hash_name]['dimension']
            self.measure = hist_dict[hash_name]['measure']
        else:
            self.dimension = []
            self.measure = []
            for colname, coltype in self.data.dtypes.iteritems():
                if self.check_date_col(colname):
                    self.dimension.append(colname+"_year")
                elif coltype == 'object': 
                    self.data[colname] = self.data[colname].astype(str)
                    self.dimension.append(colname)
                elif self.check_dimension_name(colname):
                    self.data[colname] = self.data[colname].astype(int)     # round to decimal
                    self.data[colname] = self.data[colname].astype(str)
                    self.dimension.append(colname)
                else : self.measure.append(colname)
                self.save_hist()    # save to history file

    def save_hist(self) -> None:
        """
        This method will save measure and dimension to history file
        """
        new_dict = {'dimension': self.dimension, 'measure': self.measure}
        hash_name = self.getMd5(self.filename)
        self.hist.creat_hist(hash_name, new_dict)

    
    def is_dimension(self, s:str) -> bool:
        """
        This method will check column in dimension

        Parameters
        ----------
        s: str
            column name 

        Returns
        -------
        bool
            True if column in dimension
        """
        return s in self.dimension

    def is_measure(self, s:str) -> bool:
        """
        This method will check column in measure

        Parameters
        ----------
        s: str
            column name 

        Returns
        -------
        bool
            True if column in measure
        """
        return s in self.measure
    
    def get_dimension(self) -> list:
        """
        This method will return dimension list

        Returns
        -------
        list
            dimension list
        """
        return self.dimension

    def get_measure(self) -> list:
        """
        This method will return measure list

        Returns
        -------
        list
            measure list
        """
        return self.measure
    
    def get_groupby(self, col:list, measure:dict, fil:dict) -> dict:
        """
        This method will groupby dimension, measure. and query data.

        Parameters
        ----------
        col: list
            list of dimension column
        measure: dict
            dict of measure column
            keys -> column
            values -> method 
        fil: dict
            dict of filter column
        
        Returns
        -------
        dict
            data -> values of data
            col -> column of data
        """
        data = self.data_separated_date.copy()
        if fil:     # if fileter have item
            querylist = []  # list of query string
            for _, name in enumerate(fil):
                if self.check_date_col(name):
                    for method in ['day', 'month', 'year']:
                        querylist.append(f'(`{name}_{method}` == {fil[name][method]})')
                elif self.is_measure(name):
                    continue
                else:
                    querylist.append(f'(`{name}` == {fil[name]})')
            querylist = " & ".join(querylist)   # join to string
            if querylist:
                data = data.query(querylist)    #queryl
        if len(measure) > 0:    # if measure have item
            data = data.groupby(col, as_index=False).agg(measure)
        else:
            data = data.groupby(col, as_index=False).mean()
            data = data.iloc[:,:len(col)]   # select dimension column only
        querylist = []
        for _, name in enumerate(fil):
            if self.is_measure(name):
                if fil[name]['state']:
                    measure_query = self.measure_condition(name, fil[name]['condition'], fil[name]['value'])
                    querylist.append(measure_query)
        querylist = " & ".join(querylist)   # join to string
        if querylist:
            data = data.query(querylist)    #queryl
        data = self.date_to_string(data)
        def get_col():
            """ This method will return column of data"""
            return data.columns.tolist()
        return {'data': data.values.tolist(), 'col': get_col(), 'dataframe': data}
    
    def date_to_string(self, data: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
        for col in data.columns:
            if self.check_date_col(col):
                data[col] = data[col].dt.strftime('%d/%m/%Y')
        return data

    def data_filter(self, item1: list, item2: list, fil1: dict, fil2: dict, measure1:dict, measure2:dict) -> pd.core.frame.DataFrame:
        """
        This method will filter column and item, then return as DataFrame

        Parameters
        ----------
        item1 : list
            column list
        item2 : list
            row list
        fil1 : dict
            column filter
        fil2 : dict
            row filter
        
        Returns
        -------
        DataFrame
            filter data
        """
        item = item1+item2  # merge item
        dimension = [i for i in item if self.is_dimension(i) or self.check_date_col2(i)]
        if not dimension:
            dimension = item
        measure = {**measure1, **measure2}
        fil = {**fil1, **fil2}    # merge filter 
        data_groupby = self.get_groupby(dimension, measure, fil)
        data = data_groupby['dataframe']
        for i in data.columns:
            if self.check_date_col2(i):
                data[i] = data[i].astype(str)
        return data
    
    def select_plot_data(self, item , fil, data):
        l = []
        data = data.copy()
        for col in item:
            if self.check_date_col(col):
                data[col] = data[f'{col}_{fil[col]["graph"]}']
                data[col] = data[col].astype(str)
        data = data[item]
        return data

    def measure_condition(self, col:str, condition:str, value:float) -> str:
        return f'`{col}` {condition} {value}'
    
    def check_date_col(self, name:str) -> bool:
        return 'date' in name.lower() and "_" not in name.lower()

    def check_date_col2(self, name:str) -> bool:
        return 'date' in name.lower()
    
    def separated_date(self):
        self.data_separated_date = self.data.copy()
        for col in self.column:
            if self.check_date_col(col):
                self.data_separated_date[col] = pd.to_datetime(self.data[col], format="%d/%m/%Y")
                self.data_separated_date[col+'_day'] = self.data_separated_date[col].dt.day.astype(int)
                self.data_separated_date[col+'_month'] = self.data_separated_date[col].dt.month.astype(int)
                self.data_separated_date[col+'_year'] = self.data_separated_date[col].dt.year.astype(int)
    
    def unioun_data(self, filename:str) -> None:
        """
        This method will union new data to current data

        Parameters
        ----------
        filename : str
            path of file
        """
        union_data = None
        if filename.split('.')[-1] == "csv":
            try:
                union_data = pd.read_csv(filename, encoding='windows-1252')
                union_data = union_data.dropna()
            except UnicodeDecodeError:
                union_data = pd.read_csv(filename, encoding='utf8')
                self.column = union_data.columns
                union_data = union_data.dropna()
        else:
            union_data = pd.read_excel(filename)
            union_data = union_data.dropna()
        self.data = pd.concat([self.data, union_data])
        self.separated_dimension_measure()
    
    def get_unique_date(self, col, method) -> list:
        data = pd.unique(self.data_separated_date[f'{col}_{method}']).tolist()
        data = sorted(data)
        return data

    def get_unique(self, col:str) -> list:
        """
        This method will return unique value of column

        Parameters
        ----------
        col : str
            column name
        
        Returns
        -------
        list
            unique value list
        """
        return pd.unique(self.data_separated_date[col]).tolist()
    
    def change_to_dimension(self, name:str) -> None:
        """
        this method will change measure column to dimension column

        parameters
        ----------
        name : str
            column name
        """
        self.dimension.append(name)
        self.measure.remove(name)
        self.save_hist()

    def change_to_measure(self, name:str) -> None:
        """
        this method will change dimension column to measure column

        parameters
        ----------
        name : str
            column name
        """
        self.dimension.remove(name)
        self.measure.append(name)
        self.save_hist()
    
    def getMd5(self, name:str):
        with open(name, 'rb') as r:
            hash_name = hashlib.md5(r.read()).hexdigest()
            return hash_name

if __name__ == "__main__":
    from History import History
    d = data_manipulate()
    d.load_data('data1.csv')
    print(d.get_column())
    d.separated_date()
    print(d.data_separated_date.head())
    print(d.data_separated_date['Order Date_day'].unique())
    # print(d.get_unique_date('Order Date', 'day'))
    # print(d.check_date_col('ship Date'))
    print(d.get_unique('City'))

else:
    from Widgets.History import History