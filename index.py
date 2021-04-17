import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import dash_f5a, dash_f5b, dash_f6a, dash_f6b, dash_f6c, dash_ncc, dash_ccc, dash_ndc#, dash_f6d
#from apps import dash_ndc


app.layout = html.Div([
    html.H2("Modelación de la complejidad usando estructuras matemáticas discretas"),
    dcc.Tabs(id='tabs-disertation', value='tab-5a', children=[
        # dcc.Tab(label='Fig 3a', value='tab-3a'),
        # dcc.Tab(label='Fig 3b', value='tab-3b'),
        # #dcc.Tab(label='Fig 4', value='tab-4'),
        dcc.Tab(label='Fig 5a', value='tab-5a'),
        dcc.Tab(label='Fig 5b', value='tab-5b'),
        # dcc.Tab(label='Fig 5c', value='tab-5c'),
        # dcc.Tab(label='Fig 5d', value='tab-5d'),
        dcc.Tab(label='Fig 6a', value='tab-6a'),
        # dcc.Tab(label='Fig 6b', value='tab-6b'),
        # dcc.Tab(label='Fig 6c', value='tab-6c'),
        # # dcc.Tab(label='Fig 6d', value='tab-6d'),
        # dcc.Tab(label='Fig NCC', value='tab-ncc'),
        # dcc.Tab(label='Fig CCC', value='tab-ccc'),
        dcc.Tab(label='Fig NDC', value='tab-ndc'),
    ]),
    html.Div(id='tab-fig')
])

@app.callback(Output('tab-fig', 'children'),
              Input('tabs-disertation', 'value'))
def render_content(tab):
    # if tab == 'tab-3a':
    #     return html.Div([
    #         html.H3('Figura 3a')
    #     ])
    # elif tab == 'tab-3b':
    #     return html.Div([
    #         html.H3('Figura 3b')
    #     ])
    # # elif tab == 'tab-4':
    #     # return html.Div([
    #         # html.H3('Figura 4')
    #     # ])
    if tab == 'tab-5a':
        return html.Div([
            dash_f5a.layout
        ])
    elif tab == 'tab-5b':
        return html.Div([
            dash_f5b.layout
        ])
    # elif tab == 'tab-5c':
    #     return html.Div([
    #         html.H3('Figura 5c')
    #     ])
    # elif tab == 'tab-5d':
    #     return html.Div([
    #         html.H3('Figura 5d')
    #     ])
    elif tab == 'tab-6a':
        return html.Div([
            dash_f6a.layout
        ])
    # elif tab == 'tab-6b':
    #     return html.Div([
    #         dash_f6b.layout
    #     ])
    # elif tab == 'tab-6c':
    #     return html.Div([
    #         dash_f6c.layout
    #     ])
    # # elif tab == 'tab-6d':
    # #     return html.Div([
    # #         dash_f6d.layout
    # #     ])
    # elif tab == 'tab-ncc':
    #     return html.Div([
    #         dash_ncc.layout
    #     ])
    # elif tab == 'tab-ccc':
    #     return html.Div([
    #         dash_ccc.layout
    #     ])
    # elif tab == 'tab-ndc':
    elif tab == 'tab-ndc':
        return html.Div([
            dash_ndc.layout
        ])



if __name__ == '__main__':
    app.run_server(debug=True)
