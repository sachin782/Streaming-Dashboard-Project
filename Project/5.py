import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
X = []
X.append(1)
Y = []
Y.append(1)
app = dash.Dash(__name__)
app.layout = html.Div([dcc.Graph(id='stream-graph', animate=True),dcc.Interval(id='event-update',interval=2*1000),])
@app.callback(Output('stream-graph', 'figure'),[Input('event-update', 'n_intervals')])
def update_graph_scatter(input_data):
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))
    data = plotly.graph_objs.Scatter(x=list(X),y=list(Y),name='Scatter',mode= 'markers+lines')
    return {'data': [data], 'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]), yaxis=dict(range=[min(Y),max(Y)]),)}
if __name__ == '__main__':
    app.run_server(debug=True)