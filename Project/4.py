import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
app = dash.Dash()
df = pd.read_csv('scanvote.csv',encoding= 'unicode_escape')
app.layout = html.Div([
    dcc.Graph(
        id='Vote per-vs-Population',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['District'] == i]['Percentage'],
                    y=df[df['District'] == i]['Pop'],
                    text=df[df['District'] == i]['Country'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.District.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Vote Percentage'},
                yaxis={'title': 'Population'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])
if __name__ == '__main__':
    app.run_server()
