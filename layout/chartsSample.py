import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np
from . import chartModel as cm

plt.style.use('seaborn')

# graph sgd generated with dummy
def sgd_dummy():

    pos = np.arange(10)+ 2

    fig = plt.figure(figsize=(8, 3))
    ax = fig.add_subplot(111)

    ax.barh(pos, np.arange(1, 11), align='center')
    ax.set_yticks(pos)
    ax.set_yticklabels(('#hcsm',
                        '#ukmedlibs',
                        '#ImmunoChat',
                        '#HCLDR',
                        '#ICTD2015',
                        '#hpmglobal',
                        '#BRCA',
                        '#BCSM',
                        '#BTSM',
                        '#OTalk',),
                       fontsize=15)
    ax.set_xticks([])
    ax.invert_yaxis()

    ax.set_xlabel('Popularity')
    ax.set_ylabel('Hashtags')
    ax.set_title('Hashtags')

    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return graphic

def chartDataset(x,y,title, sorted = False, label = None ):
    dataset = cm.chartModel()
    dataset.setX(x)
    dataset.setY(y)
    if(sorted):
        None
    return dataset.getObject(title,True);


