from typing import Dict,List,Union
import pandas
import numpy
from dataclasses import dataclass
from .linesInterface import LineInterface
def check_in_dict(dic,name,default):
    if name in dic:
        val = dic[name]
    else:
        val=default
    return val

@dataclass
class FigureLegend:
    text:List[str]
    position:str

class FigureInterface:
    
    @property
    def lines(self)->List[LineInterface]:
        return self._lines

    @property
    def title(self)->str:
        return self._title
    
    @property
    def legendPosition(self)->str:
        return self._legend
    
    def __init__(self,data:Dict) -> None:
        self._data = data
        self.xlabel,self.ylabel,self.zlabel = self._getLabels()
        self._legend = check_in_dict(self._data,"legend_position",None)
        self._title = check_in_dict(self._data,"title","")
        self._lines = self._getLines()
        
    def _getLines(self)->List[LineInterface]:
        lines = []
        if "lines" in self._data:            
            for line in self._data["lines"]:
                lines.append(LineInterface(line))
                
        if lines==[]:
            raise Exception("There must be at least one line to plot in the figure")        
        return lines
    
    def _getLabels(self):
        xlabel = check_in_dict(self._data,"xlabel","")
        ylabel = check_in_dict(self._data,"ylabel","")
        second = check_in_dict(self._data,"second_axe",False)
        if second =="true":
            second = True
            zlabel = check_in_dict(self._data,"zlabel","")
        else:
            zlabel = None
        return xlabel,ylabel,zlabel

