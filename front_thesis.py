import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

import dash_f5a as df5a

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H2("Modelación de la complejidad usando estructuras matemáticas discretas"),
    dcc.Tabs(id='tabs-disertation', value='tab-5a', children=[
        dcc.Tab(label='Fig 3a', value='tab-3a'),
        dcc.Tab(label='Fig 3b', value='tab-3b'),
        #dcc.Tab(label='Fig 4', value='tab-4'),
        dcc.Tab(label='Fig 5a', value='tab-5a'),
        dcc.Tab(label='Fig 5b', value='tab-5b'),
        dcc.Tab(label='Fig 5c', value='tab-5c'),
        dcc.Tab(label='Fig 5d', value='tab-5d'),
        dcc.Tab(label='Fig 6a', value='tab-6a'),
        dcc.Tab(label='Fig 6b', value='tab-6b'),
        dcc.Tab(label='Fig 6c', value='tab-6c'),
        dcc.Tab(label='Fig 6d', value='tab-6d'),
    ]),
    html.Div(id='tab-fig')
])

@app.callback(Output('tab-fig', 'children'),
              Input('tabs-disertation', 'value'))
def render_content(tab):
    if tab == 'tab-3a':
        return html.Div([
            html.H3('Figura 3a')
        ])
    elif tab == 'tab-3b':
        return html.Div([
            html.H3('Figura 3b')
        ])
    # elif tab == 'tab-4':
        # return html.Div([
            # html.H3('Figura 4')
        # ])
    elif tab == 'tab-5a':
        return html.Div([
            df5a.layout
        ])
    elif tab == 'tab-5b':
        return html.Div([
            html.H3('Figura 5b')
        ])
    elif tab == 'tab-5c':
        return html.Div([
            html.H3('Figura 5c')
        ])
    elif tab == 'tab-5d':
        return html.Div([
            html.H3('Figura 5d')
        ])
    elif tab == 'tab-6a':
        return html.Div([
            html.H3('Figura 6a')
        ])
    elif tab == 'tab-6b':
        return html.Div([
            html.H3('Figura 6b')
        ])
    elif tab == 'tab-6c':
        return html.Div([
            html.H3('Figura 6c')
        ])
    elif tab == 'tab-6d':
        return html.Div([
            html.H3('Figura 6d')
        ])
        


if __name__ == '__main__':
    app.run_server(debug=True)
