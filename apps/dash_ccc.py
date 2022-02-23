# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


import plotly.express as px


########## ---------- Figura 5 a
from apps.b_ccc import iterations_ccc

from app import app



layout = html.Div([

    # Título
    html.Div([
        html.H4("Acumulado de casos confirmados")
    ]),


    # Parámetros
    html.Div([

        ### COLUMNA IZQUIERDA
        html.Div([
            ######
            ######  Dimensiones del mapa
            html.Div(id="fccc-sz-r-output", style={"margin-top":1}),
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
                id="fccc-sz-r",
            ),

            html.Div(id="fccc-sz-c-output", style={"margin-top":20}),
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
                id="fccc-sz-c",
            ),



            ######
            ###### radio de la esfera de influencia
            html.Div(id="fccc-d-output", style={"margin-top":20}),
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
                id="fccc-d",
            ),


            ######
            ###### densidad de población
            html.Div(id="fccc-D-output", style={"margin-top":20}),
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
                id="fccc-D",
            ),


            ######
            ###### Número de ciclos
            html.Div(id="fccc-n-cycles-output", style={"margin-top":20}),
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
                id="fccc-n-cycles",
            ),


            # ######
            # ###### R_0
            html.Div(id="fccc-R-0-output", style={"margin-top":20}),
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
                id="fccc-R-0",
            ),


            # ######
            # ###### t_infec
            html.Div(id="fccc-t-infec-output", style={"margin-top":20}),
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
                id="fccc-t-infec",
            ),


            # ######
            # ###### case-fatality ratio (a pesar de no ser constante)
            html.Div(id="fccc-cfr-output", style={"margin-top":20}),
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
                id="fccc-cfr",
            ),
        ]),


        ### COLUMNA DERECHA
        html.Div([
            # ######
            # ###### t_I
            html.Div(id="fccc-t-I-output", style={"margin-top":20}),
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
                id="fccc-t-I",
            ),


            # ######
            # ###### p_Q
            html.Div(id="fccc-p-Q-output", style={"margin-top":20}),
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
                id="fccc-p-Q",
            ),


            # ######
            # ###### t_Q
            html.Div(id="fccc-t-Q-output", style={"margin-top":20}),
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
                id="fccc-t-Q",
            ),


            # ######
            # ###### t_L
            html.Div(id="fccc-t-L-output", style={"margin-top":20}),
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
                id="fccc-t-L",
            ),


            # ######
            # ###### t_R
            html.Div(id="fccc-t-R-output", style={"margin-top":20}),
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
                id="fccc-t-R",
            ),


            # ######
            # ###### E_in
            html.Div(id="fccc-E-in-output", style={"margin-top":20}),
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
                id="fccc-E-in",
            ),


            # ######
            # ###### I_in
            html.Div(id="fccc-I-in-output", style={"margin-top":20}),
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
                id="fccc-I-in",
            ),
        ])


    ], style={'columnCount': 2}),

    ###
    ### Botón de inicio
    ###
    html.Button("START", id='fccc-button-start', n_clicks=0),
    html.Div(id="fccc-program-status",style={"margin-top":20}),

    #############
    #######   GRÁFICA
    ############
    html.Div([
        dcc.Loading(
            id="fccc-loading-graph",
            children=html.Div([dcc.Graph(id = 'fig-ccc')]),
            type="default"
        )
    ])
])



@app.callback(Output('fccc-sz-r-output','children'),
             [Input('fccc-sz-r', 'drag_value')])
def display_value_r(drag_value):
    return "Número de filas: {}".format(drag_value)



@app.callback(Output('fccc-sz-c-output','children'),
             [Input('fccc-sz-c', 'drag_value')])
def display_value_c(drag_value):
    return "Número de columnas: {}".format(drag_value)



@app.callback(Output('fccc-d-output','children'),
             [Input('fccc-d', 'drag_value')])
def display_value_d(drag_value):
    return "Radio de la esfera de influencia: {}".format(drag_value)



@app.callback(Output('fccc-D-output','children'),
             [Input('fccc-D', 'drag_value')])
def display_value_D(drag_value):
    return "Densidad de población: {}".format(drag_value)



@app.callback(Output('fccc-n-cycles-output','children'),
             [Input('fccc-n-cycles', 'drag_value')])
def display_value_r(drag_value):
    return "Número de ciclos: {}".format(drag_value)



@app.callback(Output('fccc-R-0-output','children'),
             [Input('fccc-R-0', 'drag_value')])
def display_value_r(drag_value):
    return "R_0: {}".format(drag_value)



@app.callback(Output('fccc-t-infec-output','children'),
             [Input('fccc-t-infec', 'drag_value')])
def display_value_r(drag_value):
    return "Tiempo que un contagiado puede infectar: {}".format(drag_value)


@app.callback(Output('fccc-cfr-output','children'),
             [Input('fccc-cfr', 'drag_value')])
def display_value_r(drag_value):
    return "Case-fatality risk: {}".format(drag_value)


@app.callback(Output('fccc-t-I-output','children'),
             [Input('fccc-t-I', 'drag_value')])
def display_value_r(drag_value):
    return "t_I: {}".format(drag_value)



@app.callback(Output('fccc-p-Q-output','children'),
             [Input('fccc-p-Q', 'drag_value')])
def display_value_r(drag_value):
    return "p_Q: {}".format(drag_value)



@app.callback(Output('fccc-t-Q-output','children'),
             [Input('fccc-t-Q', 'drag_value')])
def display_value_r(drag_value):
    return "t_Q: {}".format(drag_value)



@app.callback(Output('fccc-t-L-output','children'),
             [Input('fccc-t-L', 'value')])
def display_value_r(value):
    return "t_L: {}".format(value)



@app.callback(Output('fccc-t-R-output','children'),
             [Input('fccc-t-R', 'drag_value')])
def display_value_r(drag_value):
    return "t_R: {}".format(drag_value)



@app.callback(Output('fccc-E-in-output','children'),
             [Input('fccc-E-in', 'drag_value')])
def display_value_r(drag_value):
    return "E_in: {}".format(drag_value)



@app.callback(Output('fccc-I-in-output','children'),
             [Input('fccc-I-in', 'drag_value')])
def display_value_r(drag_value):
    return "I_in: {}".format(drag_value)


@app.callback(
     Output("fig-ccc", "figure"),
    [Input('fccc-button-start', 'n_clicks')],
    [State('fccc-sz-r','value'),
     State('fccc-sz-c','value'),
     State('fccc-d', 'value'),
     State("fccc-D",'value'),
     State('fccc-n-cycles','value'),
     State('fccc-R-0','value'),
     State('fccc-t-infec','value'),
     State('fccc-t-I','value'),
     State('fccc-p-Q','value'),
     State('fccc-t-Q','value'),
     State('fccc-cfr','value'),
     State('fccc-t-L','value'),
     State('fccc-t-R','value'),
     State('fccc-E-in','value'),
     State('fccc-I-in','value'),
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
                       cfr,
                       t_L,
                       t_R,
                       E_in,
                       I_in,
                       ):

    #vals_ent = l_t_L.split(",")
    #l_t_L = [int(x) for x in vals_ent]
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
    print("p_D: %d" %(cfr))
    print('t_L: %f' %(t_L))
    print("t_R: %d" %(t_R))
    print("E_in: %d" %(E_in))
    print("I_in: %d" %(I_in))
    df = iterations_ccc(
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
               cfr,
               t_L,
               t_R,
               E_in,
               I_in,
              )
    print(df.keys())
    fig = px.scatter(df, x = "t", y = "% de casos confirmados acumulados")

    return fig
