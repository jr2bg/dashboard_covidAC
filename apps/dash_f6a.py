# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


import plotly.express as px


########## ---------- Figura 6 a
from apps.b_fig6a import iterations_6a

from app import app



layout = html.Div([

    # Título
    html.Div([
        html.H4("FIGURA 6a")
    ]),


    # Parámetros
    html.Div([
        ######
        ######  Dimensiones del mapa
        html.Div(id="f6a-sz-r-output", style={"margin-top":1}),
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
            id="f6a-sz-r",
        ),

        html.Div(id="f6a-sz-c-output", style={"margin-top":20}),
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
            id="f6a-sz-c",
        ),



        ######
        ###### radio de la esfera de influencia
        html.Div(id="f6a-d-output", style={"margin-top":20}),
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
            id="f6a-d",
        ),


        ######
        ###### densidad de población
        html.Div(id="f6a-D-output", style={"margin-top":20}),
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
            id="f6a-D",
        ),


        ######
        ###### Número de ciclos
        html.Div(id="f6a-n-cycles-output", style={"margin-top":20}),
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
            id="f6a-n-cycles",
        ),


        # ######
        # ###### R_0
        html.Div(id="f6a-R-0-output", style={"margin-top":20}),
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
            id="f6a-R-0",
        ),


        # ######
        # ###### t_infec
        html.Div(id="f6a-t-infec-output", style={"margin-top":20}),
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
            id="f6a-t-infec",
        ),


        # ######
        # ###### case-fatality ratio (a pesar de no ser constante)
        html.Div(id="f6a-cfr-output", style={"margin-top":20}),
        dcc.Slider(
            min=0,
            max=1,
            step=0.001,
            value=0.1,
            marks={
            0: {'label': '0', 'style': {'color': '#77b0b1'}},
            0.1: {'label': '0.1'},
            1: {'label': '1', 'style': {'color': '#f50'}}
            },
            id="f6a-cfr",
        ),


        # ######
        # ###### t_I
        html.Div(id="f6a-t-I-output", style={"margin-top":20}),
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
            id="f6a-t-I",
        ),


        # ######
        # ###### p_Q
        html.Div(id="f6a-p-Q-output", style={"margin-top":20}),
        dcc.Input(
            type="text",
            placeholder="valores separados por comas",
            value='',
            id="f6a-p-Q",
        ),


        # ######
        # ###### t_Q
        html.Div(id="f6a-t-Q-output", style={"margin-top":20}),
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
            id="f6a-t-Q",
        ),


        # ######
        # ###### t_L
        html.Div(id="f6a-t-L-output", style={"margin-top":20}),
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
            id="f6a-t-L",
        ),


        # ######
        # ###### t_R
        html.Div(id="f6a-t-R-output", style={"margin-top":20}),
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
            id="f6a-t-R",
        ),


        # ######
        # ###### E_in
        html.Div(id="f6a-E-in-output", style={"margin-top":20}),
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
            id="f6a-E-in",
        ),


        # ######
        # ###### I_in
        html.Div(id="f6a-I-in-output", style={"margin-top":20}),
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
            id="f6a-I-in",
        ),



        html.Button("START", id='f6a-button-start', n_clicks=0),
        html.Div(id="f6a-program-status",style={"margin-top":20})


    ], style={'columnCount': 2}),


    #############
    #######   GRÁFICA
    ############
    html.Div([
        dcc.Loading(
            id="f6a-loading-graph",
            children=html.Div([dcc.Graph(id = 'fig-6a')]),
            type="default"
        )
    ])
])



@app.callback(Output('f6a-sz-r-output','children'),
             [Input('f6a-sz-r', 'drag_value')])
def display_value_r(drag_value):
    return "Número de filas: {}".format(drag_value)



@app.callback(Output('f6a-sz-c-output','children'),
             [Input('f6a-sz-c', 'drag_value')])
def display_value_c(drag_value):
    return "Número de columnas: {}".format(drag_value)



@app.callback(Output('f6a-d-output','children'),
             [Input('f6a-d', 'drag_value')])
def display_value_d(drag_value):
    return "Radio de la esfera de influencia: {}".format(drag_value)



@app.callback(Output('f6a-D-output','children'),
             [Input('f6a-D', 'drag_value')])
def display_value_D(drag_value):
    return "Densidad de población: {}".format(drag_value)



@app.callback(Output('f6a-n-cycles-output','children'),
             [Input('f6a-n-cycles', 'drag_value')])
def display_value_r(drag_value):
    return "Número de ciclos: {}".format(drag_value)



@app.callback(Output('f6a-R-0-output','children'),
             [Input('f6a-R-0', 'drag_value')])
def display_value_r(drag_value):
    return "R_0: {}".format(drag_value)



@app.callback(Output('f6a-t-infec-output','children'),
             [Input('f6a-t-infec', 'drag_value')])
def display_value_r(drag_value):
    return "Tiempo que un contagiado puede infectar: {}".format(drag_value)


@app.callback(Output('f6a-cfr-output','children'),
             [Input('f6a-cfr', 'drag_value')])
def display_value_r(drag_value):
    return "Case-fatality risk: {}".format(drag_value)


@app.callback(Output('f6a-t-I-output','children'),
             [Input('f6a-t-I', 'drag_value')])
def display_value_r(drag_value):
    return "t_I: {}".format(drag_value)



@app.callback(Output('f6a-p-Q-output','children'),
             [Input('f6a-p-Q', 'value')])
def display_value_r(value):
    return "Valores de p_Q: {}".format(value)



@app.callback(Output('f6a-t-Q-output','children'),
             [Input('f6a-t-Q', 'drag_value')])
def display_value_r(drag_value):
    return "t_Q: {}".format(drag_value)



@app.callback(Output('f6a-t-L-output','children'),
             [Input('f6a-t-L', 'value')])
def display_value_r(value):
    return "t_L: {}".format(value)



@app.callback(Output('f6a-t-R-output','children'),
             [Input('f6a-t-R', 'drag_value')])
def display_value_r(drag_value):
    return "t_R: {}".format(drag_value)



@app.callback(Output('f6a-E-in-output','children'),
             [Input('f6a-E-in', 'drag_value')])
def display_value_r(drag_value):
    return "E_in: {}".format(drag_value)



@app.callback(Output('f6a-I-in-output','children'),
             [Input('f6a-I-in', 'drag_value')])
def display_value_r(drag_value):
    return "I_in: {}".format(drag_value)


@app.callback(
     Output("fig-6a", "figure"),
    [Input('f6a-button-start', 'n_clicks')],
    [State('f6a-sz-r','value'),
     State('f6a-sz-c','value'),
     State('f6a-d', 'value'),
     State("f6a-D",'value'),
     State('f6a-n-cycles','value'),
     State('f6a-R-0','value'),
     State('f6a-t-infec','value'),
     State('f6a-t-I','value'),
     State('f6a-p-Q','value'),
     State('f6a-t-Q','value'),
     State('f6a-cfr','value'),
     State('f6a-t-L','value'),
     State('f6a-t-R','value'),
     State('f6a-E-in','value'),
     State('f6a-I-in','value'),
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
                       l_p_Q,
                       t_Q,
                       cfr,
                       t_L,
                       t_R,
                       E_in,
                       I_in,
                       ):

    vals_ent = l_p_Q.split(",")
    l_p_Q = [float(x) for x in vals_ent]
    print("sz_r: %d" %(sz_r))
    print("sz_c: %d" %(sz_c))
    print("d: %d" %(d))
    print("D: %f" %(D))
    print("n_cycles: %d" %(n_cycles))
    print("R_0: %f" %(R_0))
    print("t_infec: %d" %(t_infec))
    print("t_I: %d" %(t_I))
    print("l_p_Q: " + str(l_p_Q)[1:-1])
    print("t_Q: %d" %(t_Q))
    print("p_D: %d" %(cfr))
    print('t_L: %d' %(t_L))
    print("t_R: %d" %(t_R))
    print("E_in: %d" %(E_in))
    print("I_in: %d" %(I_in))
    df = iterations_6a(
               sz_r,
               sz_c,
               d,
               D,
               n_cycles,
               R_0,
               t_infec,
               t_I,
               l_p_Q,
               t_Q,
               cfr,
               t_L,
               t_R,
               E_in,
               I_in,
              )
    print(df.keys())
    fig = px.scatter(df, x = "t", y = "f_infec", color = "p_Q")

    return fig
