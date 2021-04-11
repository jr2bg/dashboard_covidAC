# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


import plotly.express as px


########## ---------- Figura 5b
from apps.b_fig5b import iterations_5b

from app import app



layout = html.Div([

    # Título
    html.Div([
        html.H4("FIGURA 5b")
    ]),
    
    
    # Parámetros
    html.Div([
        ######
        ######  Dimensiones del mapa
        html.Div(id="f5b-sz-r-output", style={"margin-top":1}),
        dcc.Slider(
            min=25,
            max=400,
            step=25,
            value=200,
            marks={
            25: {'label': '25', 'style': {'color': '#77b0b1'}},
            200: {'label': '200'},
            400: {'label': '400', 'style': {'color': '#f50'}}
            },
            id="f5b-sz-r",
        ),
        
        html.Div(id="f5b-sz-c-output", style={"margin-top":20}),
        dcc.Slider(
            min=25,
            max=400,
            step=25,
            value=200,
            marks={
            25: {'label': '25', 'style': {'color': '#77b0b1'}},
            200: {'label': '200'},
            400: {'label': '400', 'style': {'color': '#f50'}}
            },
            id="f5b-sz-c",
        ),
        
        
        
        ######
        ###### radio de la esfera de influencia
        html.Div(id="f5b-d-output", style={"margin-top":20}),
        dcc.Slider(
            min=0,
            max=5,
            step=1,
            value=3,
            marks={
            0: {'label': '0', 'style': {'color': '#77b0b1'}},
            3: {'label': '3'},
            5: {'label': '5', 'style': {'color': '#f50'}}
            },
            id="f5b-d",
        ),
        
        
        ######
        ###### densidad de población
        html.Div(id="f5b-D-output", style={"margin-top":20}),
        dcc.Slider(
            min=0,
            max=1,
            step=0.01,
            value=0.5,
            marks={
            0: {'label': '0', 'style': {'color': '#77b0b1'}},
            0.5: {'label': '0.5'},
            1: {'label': '1', 'style': {'color': '#f50'}}
            },
            id="f5b-D",
        ),
        
        
        ######
        ###### Número de ciclos
        html.Div(id="f5b-n-cycles-output", style={"margin-top":20}),
        dcc.Slider(
            min=0,
            max=200,
            step=1,
            value=100,
            marks={
            0: {'label': '0', 'style': {'color': '#77b0b1'}},
            100: {'label': '100'},
            200: {'label': '200', 'style': {'color': '#f50'}}
            },
            id="f5b-n-cycles",
        ),
        
        
        # ######
        # ###### R_0
        html.Div(id="f5b-R-0-output", style={"margin-top":20}),
        dcc.Slider(
            min=0.01,
            max=10,
            step=0.01,
            value=1.5,
            marks={
            0.01: {'label': '0.01', 'style': {'color': '#77b0b1'}},
            1.5: {'label': '1.5'},
            10: {'label': '10', 'style': {'color': '#f50'}}
            },
            id="f5b-R-0",
        ),
        
        
        # ######
        # ###### t_infec
        html.Div(id="f5b-t-infec-output", style={"margin-top":20}),
        dcc.Slider(
            min=0,
            max=20,
            step=1,
            value=10,
            marks={
            0: {'label': '0', 'style': {'color': '#77b0b1'}},
            10: {'label': '10'},
            20: {'label': '20', 'style': {'color': '#f50'}}
            },
            id="f5b-t-infec",
        ),
        
        
        # ######
        # ###### t_I
        html.Div(id="f5b-t-I-output", style={"margin-top":20}),
        dcc.Slider(
            min=0,
            max=20,
            step=1,
            value=8,
            marks={
            0: {'label': '0', 'style': {'color': '#77b0b1'}},
            8: {'label': '8'},
            20: {'label': '20', 'style': {'color': '#f50'}}
            },
            id="f5b-t-I",
        ),
        
        
        # ######
        # ###### p_Q
        html.Div(id="f5b-p-Q-output", style={"margin-top":20}),
        dcc.Slider(
            min=0,
            max=1,
            step=0.01,
            value=0.5,
            marks={
            0: {'label': '0', 'style': {'color': '#77b0b1'}},
            0.5: {'label': '0.5'},
            1: {'label': '1', 'style': {'color': '#f50'}}
            },
            id="f5b-p-Q",
        ),
        
        
        # ######
        # ###### t_Q
        html.Div(id="f5b-t-Q-output", style={"margin-top":20}),
        dcc.Slider(
            min=0,
            max=21,
            step=1,
            value=15,
            marks={
            0: {'label': '0', 'style': {'color': '#77b0b1'}},
            15: {'label': '15'},
            21: {'label': '21', 'style': {'color': '#f50'}}
            },
            id="f5b-t-Q",
        ),
        
        
        # ######
        # ###### t_L
        html.Div(id="f5b-t-L-output", style={"margin-top":20}),
        dcc.Slider(
            min=0,
            max=21,
            step=1,
            value=15,
            marks={
            0: {'label': '0', 'style': {'color': '#77b0b1'}},
            15: {'label': '15'},
            21: {'label': '21', 'style': {'color': '#f50'}}
            },
            id="f5b-t-L",
        ),
        
        
        # ######
        # ###### t_R
        html.Div(id="f5b-t-R-output", style={"margin-top":20}),
        dcc.Slider(
            min=0,
            max=21,
            step=1,
            value=15,
            marks={
            0: {'label': '0', 'style': {'color': '#77b0b1'}},
            15: {'label': '15'},
            21: {'label': '21', 'style': {'color': '#f50'}}
            },
            id="f5b-t-R",
        ),
        
        
        # ######
        # ###### E_in
        html.Div(id="f5b-E-in-output", style={"margin-top":20}),
        dcc.Input(
            type="text",
            placeholder="valores separados por comas",
            value='',
            id="f5b-E-in",
        ),
        
        
        # ######
        # ###### I_in
        html.Div(id="f5b-I-in-output", style={"margin-top":20}),
       dcc.Input(
            type="text",
            placeholder="valores separados por comas",
            value='',
            id="f5b-I-in",
        ),
        
        
        
        html.Button("START", id='f5b-button-start', n_clicks=0),
        html.Div(id="f5b-program-status",style={"margin-top":20})
    
        
    ], style={'columnCount': 2}),
    
    
    #############
    #######   GRÁFICA
    ############
    html.Div([
        dcc.Loading(
            id="f5b-loading-graph",
            children=html.Div([dcc.Graph(id = 'fig-5b')]),
            type="default"
        )
    ])
])



@app.callback(Output('f5b-sz-r-output','children'),
             [Input('f5b-sz-r', 'drag_value')])
def display_value_r(drag_value):
    return "Número de filas: {}".format(drag_value)



@app.callback(Output('f5b-sz-c-output','children'),
             [Input('f5b-sz-c', 'drag_value')])
def display_value_c(drag_value):
    return "Número de columnas: {}".format(drag_value)



@app.callback(Output('f5b-d-output','children'),
             [Input('f5b-d', 'drag_value')])
def display_value_d(drag_value):
    return "Radio de la esfera de influencia: {}".format(drag_value)



@app.callback(Output('f5b-D-output','children'),
             [Input('f5b-D', 'drag_value')])
def display_value_D(drag_value):
    return "Densidad de población: {}".format(drag_value)
    
    
    
@app.callback(Output('f5b-n-cycles-output','children'),
             [Input('f5b-n-cycles', 'drag_value')])
def display_value_r(drag_value):
    return "Número de ciclos: {}".format(drag_value)
    


@app.callback(Output('f5b-R-0-output','children'),
             [Input('f5b-R-0', 'drag_value')])
def display_value_r(drag_value):
    return "R_0: {}".format(drag_value)    



@app.callback(Output('f5b-t-infec-output','children'),
             [Input('f5b-t-infec', 'drag_value')])
def display_value_r(drag_value):
    return "Tiempo que un contagiado puede infectar: {}".format(drag_value) 



@app.callback(Output('f5b-t-I-output','children'),
             [Input('f5b-t-I', 'drag_value')])
def display_value_r(drag_value):
    return "t_I: {}".format(drag_value) 



@app.callback(Output('f5b-p-Q-output','children'),
             [Input('f5b-p-Q', 'drag_value')])
def display_value_r(drag_value):
    return "p_Q: {}".format(drag_value) 



@app.callback(Output('f5b-t-Q-output','children'),
             [Input('f5b-t-Q', 'drag_value')])
def display_value_r(drag_value):
    return "t_Q: {}".format(drag_value) 



@app.callback(Output('f5b-t-L-output','children'),
             [Input('f5b-t-L', 'value')])
def display_value_r(value):
    return "t_L: {}".format(value) 



@app.callback(Output('f5b-t-R-output','children'),
             [Input('f5b-t-R', 'drag_value')])
def display_value_r(drag_value):
    return "t_R: {}".format(drag_value) 



@app.callback(Output('f5b-E-in-output','children'),
             [Input('f5b-E-in', 'value')])
def display_value_r(value):
    return "Valores de E_in: {}".format(value)



@app.callback(Output('f5b-I-in-output','children'),
             [Input('f5b-I-in', 'value')])
def display_value_r(value):
    return "Valores de I_in: {}".format(value)


@app.callback(
     Output("fig-5b", "figure"),
    [Input('f5b-button-start', 'n_clicks')],
    [State('f5b-sz-r','value'),
     State('f5b-sz-c','value'),
     State('f5b-d', 'value'),
     State("f5b-D",'value'),
     State('f5b-n-cycles','value'),
     State('f5b-R-0','value'),
     State('f5b-t-infec','value'),
     State('f5b-t-I','value'),
     State('f5b-p-Q','value'),
     State('f5b-t-Q','value'),
     State('f5b-t-L','value'),
     State('f5b-t-R','value'),
     State('f5b-E-in','value'),
     State('f5b-I-in','value'),
     ])
def display_values_tot(btn_start,
                       sz_r, 
                       sz_c,
                       d,
                       D,
                       n_cycles,
                       R_0,
                       t_infec,
                       t_I,
                       p_Q,
                       t_Q,
                       t_L,
                       t_R,
                       l_E_in,
                       l_I_in,
                       ):
                           
    vals_E_in = l_E_in.split(",")
    l_E_in = [int(x) for x in vals_E_in]
    vals_I_in = l_I_in.split(",")
    l_I_in = [int(x) for x in vals_I_in]
    
    print("sz_r: %d" %(sz_r))
    print("sz_c: %d" %(sz_c))
    print("d: %d" %(d))
    print("D: %f" %(D))
    print("n_cycles: %d" %(n_cycles))
    print("R_0: %f" %(R_0))
    print("t_infec: %d" %(t_infec))
    print("t_I: %d" %(t_I))
    print("p_Q: %f" %(p_Q))
    print("t_Q: %d" %(t_Q))
    print('t_L: %d' %(t_L))
    print("t_R: %d" %(t_R))
    print("l_E_in: " + str(l_E_in)[1:-1])
    print("l_I_in: " + str(l_I_in)[1:-1])
    df = iterations_5b(
               sz_r, 
               sz_c,
               d,
               D,
               n_cycles,
               R_0,
               t_infec,
               t_I,
               p_Q,
               t_Q,
               t_L,
               t_R,
               l_E_in,
               l_I_in,
              )
    print(df.keys())
    fig = px.scatter(df, x = "t", y = "f_infec", color = "E_in,I_in")
                  
    return fig
