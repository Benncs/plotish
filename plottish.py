import matplotlib.pyplot as plt 
from dataset import DataSet
from interfaces.figureinterface import FigureInterface
from enum import Enum
from typing import List 

class FigType(Enum):
    PDF=0,
    PGF=1,
    PNG=2,
    SVG=3,
    SHOW=4,
    

class Plottish:
    def __init__(self,outfolder,types:List[FigType], dataset:DataSet) -> None:
        self._outfolder = outfolder
        self._dataset = dataset
        plt.style.use('ggplot')
        self.types = types

                
    def plot(self)->str:
        warns = []
        for i,fig in enumerate(self._dataset.data):
            fig,warn = self.makeFig(fig)
            for type in self.types:
                self.save(type,i)
            warns.append(warn)
        return warns
                
    def save(self,type,i):
        name = f"{self._outfolder}/{self._dataset.name}_{i}"
        match type:
            case FigType.PDF:   
                plt.savefig(f"{name}.pdf",backend="pgf",dpi=300)
            case FigType.PGF:
                plt.savefig(f"{name}.pgf",backend="pgf",dpi=300)
            case FigType.PNG:
                plt.savefig(f"{name}.png",dpi=300)
            case FigType.SVG:
                plt.savefig(f"{name}.svg",dpi=300)
            case FigType.SHOW:
                plt.show()
            case _:
                plt.savefig(f"{name}.png",dpi=50)       

    def makeFig(self,fi:FigureInterface):
        fig,ax = plt.subplots()
        ax.set_title(fi.title)
        ax.set_xlabel(fi.xlabel)
        ax.set_ylabel(fi.ylabel)
        
        for line in fi.lines:
            ax.plot(line._xdata,line._ydata,**line.kwargs)
    
        try:
            if fi.legendPosition is not None and fi.legendPosition!="None":
                ax.legend(loc=fi.legendPosition)
        except Exception as e :
            ax.legend(loc="best")
            return fig,f"Plotting:makefig legend:\r\n{str(e)}"
        
        return fig,"OK"
        