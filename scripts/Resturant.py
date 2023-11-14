import json

class Restaurant:


    def __init__(self):
        self.emptyMeta = True
        self.emptyMenu = True
        
        pass

    
    def parseMenu(self):
        pass
    
    def parseMeta(self):
        pass

    def __repr__(self):
        if self.emptyMeta:
            print("No meta data")
        if self.emptyMenu:
            print("No Menu data")

