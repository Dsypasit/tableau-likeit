import json
import os
import copy

class History:
    def __init__(self):
        self.hist = {}
        self.filename = 'hist.json'
        self.load_hist()

    def creat_hist(self, filename, md):
        self.hist[filename] = md
        self.save_hist()

    def get_hist(self):
        self.load_hist()
        return copy.deepcopy(self.hist)

    def save_hist(self):
        with open(self.filename, 'w') as file:
            json.dump(self.hist, file)

    def load_hist(self):
        if not(os.path.isfile(self.filename)):
            self.save_hist()
        with open(self.filename, 'r') as file:
            self.hist = json.load(file)

a = History()