# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


import plotly.express as px


########## ---------- Figura 5 a
from apps.b_fig5d import iterations_5d

from app import app



layout = html.Div([

    # Título
    html.Div([
        html.H4("FIGURA 5a")
    ]),


    # Parámetros
    html.Div([
        ######
        ######  Dimensiones del mapa
        html.Div(id="f5a-sz-r-output", style={"margin-top":1}),
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
            id="f5a-sz-r",
        ),

        html.Div(id="f5a-sz-c-output", style={"margin-top":20}),
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
            id="f5a-sz-c",
        ),



        ######
        ###### radio de la esfera de influencia
        html.Div(id="f5a-d-output", style={"margin-top":20}),
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
            id="f5a-d",
        ),


        ######
        ###### densidad de población
        html.Div(id="f5a-D-output", style={"margin-top":20}),
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
            id="f5a-D",
        ),


        ######
        ###### Número de ciclos
        html.Div(id="f5a-n-cycles-output", style={"margin-top":20}),
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
            id="f5a-n-cycles",
        ),


        # ######
        # ###### R_0
        html.Div(id="f5a-R-0-output", style={"margin-top":20}),
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
            id="f5a-R-0",
        ),


        # ######
        # ###### t_infec
        html.Div(id="f5a-t-infec-output", style={"margin-top":20}),
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
            id="f5a-t-infec",
        ),


        # ######
        # ###### t_I
        html.Div(id="f5a-t-I-output", style={"margin-top":20}),
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
            id="f5a-t-I",
        ),


        # ######
        # ###### p_Q
        html.Div(id="f5a-p-Q-output", style={"margin-top":20}),
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
            id="f5a-p-Q",
        ),


        # ######
        # ###### t_Q
        html.Div(id="f5a-t-Q-output", style={"margin-top":20}),
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
            id="f5a-t-Q",
        ),


        # ######
        # ###### t_L
        html.Div(id="f5a-t-L-output", style={"margin-top":20}),
        dcc.Input(
            type="text",
            placeholder="valores separados por comas",
            value='',
            id="f5a-t-L",
        ),


        # ######
        # ###### t_R
        html.Div(id="f5a-t-R-output", style={"margin-top":20}),
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
            id="f5a-t-R",
        ),


        # ######
        # ###### E_in
        html.Div(id="f5a-E-in-output", style={"margin-top":20}),
        dcc.Slider(
            min=75,
            max=375,
            step=25,
            value=200,
            marks={
            75: {'label': '75', 'style': {'color': '#77b0b1'}},
            200: {'label': '200'},
            375: {'label': '375', 'style': {'color': '#f50'}}
            },
            id="f5a-E-in",
        ),


        # ######
        # ###### I_in
        html.Div(id="f5a-I-in-output", style={"margin-top":20}),
        dcc.Slider(
            min=5,
            max=25,
            step=1,
            value=6,
            marks={
            5: {'label': '5', 'style': {'color': '#77b0b1'}},
            6: {'label': '6'},
            25: {'label': '25', 'style': {'color': '#f50'}}
            },
            id="f5a-I-in",
        ),



        html.Button("START", id='f5a-button-start', n_clicks=0),
        html.Div(id="f5a-program-status",style={"margin-top":20})


    ], style={'columnCount': 2}),


    #############
    #######   GRÁFICA
    ############
    html.Div([
        dcc.Loading(
            id="f5a-loading-graph",
            children=html.Div([dcc.Graph(id = 'fig-5a')]),
            type="default"
        )
    ])
])



@app.callback(Output('f5a-sz-r-output','children'),
             [Input('f5a-sz-r', 'drag_value')])
def display_value_r(drag_value):
    return "Número de filas: {}".format(drag_value)



@app.callback(Output('f5a-sz-c-output','children'),
             [Input('f5a-sz-c', 'drag_value')])
def display_value_c(drag_value):
    return "Número de columnas: {}".format(drag_value)



@app.callback(Output('f5a-d-output','children'),
             [Input('f5a-d', 'drag_value')])
def display_value_d(drag_value):
    return "Radio de la esfera de influencia: {}".format(drag_value)



@app.callback(Output('f5a-D-output','children'),
             [Input('f5a-D', 'drag_value')])
def display_value_D(drag_value):
    return "Densidad de población: {}".format(drag_value)



@app.callback(Output('f5a-n-cycles-output','children'),
             [Input('f5a-n-cycles', 'drag_value')])
def display_value_r(drag_value):
    return "Número de ciclos: {}".format(drag_value)



@app.callback(Output('f5a-R-0-output','children'),
             [Input('f5a-R-0', 'drag_value')])
def display_value_r(drag_value):
    return "R_0: {}".format(drag_value)



@app.callback(Output('f5a-t-infec-output','children'),
             [Input('f5a-t-infec', 'drag_value')])
def display_value_r(drag_value):
    return "Tiempo que un contagiado puede infectar: {}".format(drag_value)



@app.callback(Output('f5a-t-I-output','children'),
             [Input('f5a-t-I', 'drag_value')])
def display_value_r(drag_value):
    return "t_I: {}".format(drag_value)



@app.callback(Output('f5a-p-Q-output','children'),
             [Input('f5a-p-Q', 'drag_value')])
def display_value_r(drag_value):
    return "p_Q: {}".format(drag_value)



@app.callback(Output('f5a-t-Q-output','children'),
             [Input('f5a-t-Q', 'drag_value')])
def display_value_r(drag_value):
    return "t_Q: {}".format(drag_value)



@app.callback(Output('f5a-t-L-output','children'),
             [Input('f5a-t-L', 'value')])
def display_value_r(value):
    return "Valores de t_L: {}".format(value)



@app.callback(Output('f5a-t-R-output','children'),
             [Input('f5a-t-R', 'drag_value')])
def display_value_r(drag_value):
    return "t_R: {}".format(drag_value)



@app.callback(Output('f5a-E-in-output','children'),
             [Input('f5a-E-in', 'drag_value')])
def display_value_r(drag_value):
    return "E_in: {}".format(drag_value)



@app.callback(Output('f5a-I-in-output','children'),
             [Input('f5a-I-in', 'drag_value')])
def display_value_r(drag_value):
    return "I_in: {}".format(drag_value)


@app.callback(
     Output("fig-5a", "figure"),
    [Input('f5a-button-start', 'n_clicks')],
    [State('f5a-sz-r','value'),
     State('f5a-sz-c','value'),
     State('f5a-d', 'value'),
     State("f5a-D",'value'),
     State('f5a-n-cycles','value'),
     State('f5a-R-0','value'),
     State('f5a-t-infec','value'),
     State('f5a-t-I','value'),
     State('f5a-p-Q','value'),
     State('f5a-t-Q','value'),
     State('f5a-t-L','value'),
     State('f5a-t-R','value'),
     State('f5a-E-in','value'),
     State('f5a-I-in','value'),
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
                       l_t_L,
                       t_R,
                       E_in,
                       I_in,
                       ):

    vals_ent = l_t_L.split(",")
    l_t_L = [int(x) for x in vals_ent]
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
    print('l_t_L: ' + str(l_t_L)[1:-1])
    print("t_R: %d" %(t_R))
    print("E_in: %d" %(E_in))
    print("I_in: %d" %(I_in))
    df = iterations_5a(
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
               l_t_L,
               t_R,
               E_in,
               I_in,
              )
    print(df.keys())
    fig = px.scatter(df, x = "t", y = "f_infec", color = "t_L")

    return fig
