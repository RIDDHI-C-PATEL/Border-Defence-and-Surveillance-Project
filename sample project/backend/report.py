import pandas as pd


def generate():

    data={
    'Alert':['Drone','Vehicle','Person'],
    'Risk':['High','Medium','Low']
    }

    df=pd.DataFrame(data)

    df.to_csv('report.csv')