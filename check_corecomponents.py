# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),

    html.Label('Text Input'),
    dcc.Input(value='MTL', type='text'),

    html.Label('número de filas'),
    dcc.Slider(
        min=0,
        max=400,
        step=25,
        #marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=250,
        id="sz-r",
    ),
    
    html.Div(id="sz-r-output", style={"margin-top":1}),
    
    html.Label('número de columnas'),
    dcc.Slider(
        min=0,
        max=400,
        step=25,
        #marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=250,
        id="sz-c",
    ),
    
    html.Div(id="sz-c-output", style={"margin-top":20})
    
], style={'columnCount': 2})



@app.callback(Output('sz-r-output','children'),
#             [Input('slider-drag','drag-value'), Input('slider-drag','value')])
             [Input('sz-r', 'drag_value'), Input('sz-r', 'value')])
def display_value_r(drag_value,value):
    return "drag_value: {} |  value: {}".format(drag_value, value)



@app.callback(Output('sz-c-output','children'),
#             [Input('slider-drag','drag-value'), Input('slider-drag','value')])
             [Input('sz-c', 'drag_value'), Input('sz-c', 'value')])
def display_value_c(drag_value,value):
    return "drag_value: {} |  value: {}".format(drag_value, value)





if __name__ == '__main__':
    app.run_server(debug=True)
