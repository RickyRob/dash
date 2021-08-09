import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

x = np.random.randint(1,101,100)
y = np.random.randint(1,101,100)

data = [go.Scatter(x=x,y=y,mode='markers',
                    marker=dict(
                        size=15,
                        color='rgb(51,204,153)',
                        symbol='circle',
                        # line={'width':2}
                    ))]

layout = go.Layout(title='Scatter',
                    xaxis=dict(title='Date'),
                    yaxis=dict(title='Datos'),
                    )
fig = go.Figure(data=data,layout=layout)

pyo.plot(fig, filename='sactter.html')
