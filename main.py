import pandas 
from typing import Tuple,List,Union,Dict
import numpy 

from dataset import DataSet

from plottish import Plottish,FigType  
    
import matplotlib.pyplot as plt 
import numpy as np 

import os 
import sys

OUTFOLDER = "./out2"

def make_out_folder(dir):
    try:
        os.mkdir(dir)
    except OSError as e:
        if e.errno==17:
            pass
        else:
            print(e)
            
def treat_warnings(warnings):
    for warn in warnings:
        if warn != "OK":
            print("Warning: ",warn)

import time 
if __name__ == "__main__":
    print('cmd entry:', sys.argv)
    filename = "sample.json"
    
    make_out_folder(OUTFOLDER)
    fh = DataSet()
    try:
        start = time.time()
        fh.load_json(filename)
        print("loaded")
        # pl = Plottish(OUTFOLDER,[FigType.PNG,FigType.SHOW],fh)
        pl = Plottish(OUTFOLDER,[FigType.PNG],fh)
        end  = time.time()
        warns = pl.plot()
        print(end-start)
    
    except Exception as e :
        print(f"Error: {e}")
        exit(1)

    treat_warnings(warns)
    
