import json
import os
import copy

class History:
    """
    This class will manipulate file history
    
    ...

    Attributes
    ----------
    hist : dict
        history file keys is path, values is list of measure and dimension
    filename : str
        history file 
    """
    def __init__(self):
        self.hist:dict = {}
        self.filename:str = 'hist.json'
        self.load_hist()

    def creat_hist(self, filename:str, md:dict) -> None:
        """
        This method will create new history filename and keep measure and dimension
        to json

        Parameters
        ----------
        filename : str
            path of file
        md: dict
            measure and dimension
        """
        self.hist[filename] = md
        self.save_hist()

    def get_hist(self) -> dict:
        """
        This method will return history dict

        Returns
        -------
        dict
            history dict
        """
        self.load_hist()
        return copy.deepcopy(self.hist)

    def save_hist(self) -> None:
        """
        This method will save history to json file
        """
        with open(self.filename, 'w') as file:
            json.dump(self.hist, file)

    def load_hist(self):
        """
        This method will load history to json file
        """
        if not(os.path.isfile(self.filename)):  # check file isn't exist
            self.save_hist()
        with open(self.filename, 'r') as file:
            self.hist = json.load(file)
    
    def check_file(self, name:str) -> bool:
        return name in self.hist.keys()

a = History()