from typing import Dict
from interfaces.utils import check_in_dict 
from numpy import ndarray,array

class LineInterface:
    def __init__(self,data:Dict) -> None:
        self._data = data
        self._color = check_in_dict(data,"color",None)
        self._style = check_in_dict(data,"style",None)
        self._label = check_in_dict(data,"legend",None)
        self._marker = check_in_dict(data,"marker",None)
        self._xdata = array(check_in_dict(data,"xdata",None))

        if "ydata" in data:
            self._ydata = array(data["ydata"])
        else:
            raise Exception("Line must have Y data")
    @property
    def data(self)->ndarray:
        return array([self._xdata,self._ydata])
                    
    @property
    def kwargs(self):
        return {
            "color":self._color,
            "linestyle":self._style,
            "label":self._label,
            "marker":self._marker
        }
    