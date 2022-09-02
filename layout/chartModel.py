import math
import random
class chartModel:

    def __init__(self):
        self.label = None
        self.x = None
        self.y = None

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def setLabel(self,label):
        self.label = label

    # base on documentation from
    # https://www.chartjs.org/docs/latest/general/data-structures.html
    def getPrimitive(self):
        data= {
            "datasets": [{"data": self.x}],
            "labels": self.label
        }
        return data

    def getObject(self,title,sortTheData=False):
        dataList = []
        if (sortTheData):
            sortData= []
            for i in range(len(self.x)):
                sortData.append([self.x[i],self.y[i]])
            sortData = sorted(sortData, key=lambda x: x[0])
            for i in range(len(sortData)):
                dataList.append({"x":sortData[i][0],"y":sortData[i][1]})

        else:
            for i in range(len(self.x)):
                dataList.append({"x":self.x[i],"y":self.y[i]})

        data= {
            "datasets": [{
                "data": dataList,
                "type": title,
                "label":"Chart " + title,
                "backgroundColor": self.getRandomColor(),
            }]
        }
        return data

    def getRandomColor(self):
        letters = '0123456789ABCDEF'
        color = '#'
        for i in range(6):
            color += letters[math.floor(random.random() * 16 )]

        return color

    def __str__(self):
        return self.getObject()