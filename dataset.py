import config
import torch

class NERDataset:
    def __init__(self,texts,pos,tag):
        # text == [["Hi","my name is shreya"]]
        # tag =[ [1,2,4,5,6],[],[1,6,2]]
        self.texts = texts
        self.pos = pos
        self.tag = tag

    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self,item):
        texts = self.texts[item]
        pos = self.pos[item]
        tag = self.tag[item]

        