import pandas 
from typing import Tuple,List
import numpy 
from interfaces.figureinterface import FigureInterface
from interfaces.utils import check_in_dict

class DataSet:
    
    @property
    def date(self)->str:
        return self._date
    @property
    def description(self)->str:
        return self._description
    
    @property
    def data(self)->List[FigureInterface]:
        return self._data
    
    
    @property
    def name(self)->str:
        return self._name[0]
    
    def __init__(self) -> None:
        pass
        
    def load(self,description:str,date:str,name:str,data:List[FigureInterface]):
        self._date = date
        self._name = name
        self._description = description
        self._data = data
        
    def load_json(self,filename:str):
        self._raw_data = DataSet._openfile(filename)
        self._date,self._description = self.getMetaData()
        self._data,self._n = self.getData()
        self._name = check_in_dict(self._raw_data,"Name","figure")
        

    def getMetaData(self)->Tuple[str]:
        date = check_in_dict(self._raw_data,"date",["01/01/1900"])[0]
        description = check_in_dict(self._raw_data,"description",["No description"])[0]
        return date,description
    
    def getData(self)->Tuple[numpy.ndarray,int]:
        if "data" in self._raw_data:
            n = len(self._raw_data["data"])
            data = []#numpy.empty((n,1),dtype=Dict)
            for i,fig in enumerate(self._raw_data["data"]):
                data.append(FigureInterface(fig))
        else:
            n = 0
            data = numpy.empty((0))
        return numpy.array(data),n
    
    @staticmethod
    def _openfile(filename:str)-> pandas.DataFrame:
        return pandas.read_json(filename)