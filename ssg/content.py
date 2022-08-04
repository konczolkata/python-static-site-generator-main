import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)
    
    
    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        metadata = load(fm, Loader = FullLoader)
        return cls(metadata, content)

    
    def __init__(self, metadata, content):
        self.data = metadata   
        self.data["content"] = content
    
    @property   
    def body(self):
        return self.data["content"]
    
    @property    
    def type(self):
        self.data["type"] if "type" in self.data else None
                
    @type.setter
    def type(self, type):
        self.data["type"] = type
        
    def __getitem__(self, key):
        self.key = key
        return self.data[key]
    
    def __iter__(self):
        iter(self.data)
        
    def __len__(self):
        return len(self.data)
        
    def __repr__(self):
        data = []
        return str(data)
        
for key, value in self.data.items():
    if key != "content":
        data[key] = value
        
    
    