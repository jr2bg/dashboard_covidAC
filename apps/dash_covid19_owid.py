# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


import plotly.graph_objects as go


########## ---------- Figura 5 a
from apps.b_covid19owid import iterations_covid19owid

from app import app



layout = html.Div([

    # Título
    html.Div([
        html.H4("Covid 19 - Our World in Data")
    ]),


    # Parámetros
    html.Div([

        ### COLUMNA IZQUIERDA
        html.Div([
            ######
            ######  Dimensiones del mapa
            html.Div(id="fcovid19owid-sz-r-output", style={"margin-top":1}),
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
                id="fcovid19owid-sz-r",
            ),

            html.Div(id="fcovid19owid-sz-c-output", style={"margin-top":20}),
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
                id="fcovid19owid-sz-c",
            ),



            ######
            ###### radio de la esfera de influencia
            html.Div(id="fcovid19owid-d-output", style={"margin-top":20}),
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
                id="fcovid19owid-d",
            ),


            ######
            ###### densidad de población
            html.Div(id="fcovid19owid-D-output", style={"margin-top":20}),
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
                id="fcovid19owid-D",
            ),


            ######
            ###### Número de ciclos
            html.Div(id="fcovid19owid-n-cycles-output", style={"margin-top":20}),
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
                id="fcovid19owid-n-cycles",
            ),


            # ######
            # ###### R_0
            html.Div(id="fcovid19owid-R-0-output", style={"margin-top":20}),
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
                id="fcovid19owid-R-0",
            ),


            # ######
            # ###### t_infec
            html.Div(id="fcovid19owid-t-infec-output", style={"margin-top":20}),
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
                id="fcovid19owid-t-infec",
            ),


            # ######
            # ###### case-fatality ratio (a pesar de no ser constante)
            html.Div(id="fcovid19owid-cfr-output", style={"margin-top":20}),
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
                id="fcovid19owid-cfr",
            ),
        ]),


        ### COLUMNA DERECHA
        html.Div([
            # ######
            # ###### t_I
            html.Div(id="fcovid19owid-t-I-output", style={"margin-top":20}),
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
                id="fcovid19owid-t-I",
            ),


            # ######
            # ###### p_Q
            html.Div(id="fcovid19owid-p-Q-output", style={"margin-top":20}),
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
                id="fcovid19owid-p-Q",
            ),


            # ######
            # ###### t_Q
            html.Div(id="fcovid19owid-t-Q-output", style={"margin-top":20}),
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
                id="fcovid19owid-t-Q",
            ),


            # ######
            # ###### t_L
            html.Div(id="fcovid19owid-t-L-output", style={"margin-top":20}),
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
                id="fcovid19owid-t-L",
            ),


            # ######
            # ###### t_R
            html.Div(id="fcovid19owid-t-R-output", style={"margin-top":20}),
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
                id="fcovid19owid-t-R",
            ),


            # ######
            # ###### E_in
            html.Div(id="fcovid19owid-E-in-output", style={"margin-top":20}),
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
                id="fcovid19owid-E-in",
            ),


            # ######
            # ###### I_in
            html.Div(id="fcovid19owid-I-in-output", style={"margin-top":20}),
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
                id="fcovid19owid-I-in",
            ),
        ])


    ], style={'columnCount': 2}),

    ###
    ### Botón de inicio
    ###
    html.Button("START", id='fcovid19owid-button-start', n_clicks=0),
    html.Div(id="fcovid19owid-program-status",style={"margin-top":20}),

    #############
    #######   GRÁFICA
    ############
    html.Div([
        dcc.Loading(
            id="fncc-covid19owid-loading-graph",
            children=html.Div([dcc.Graph(id = 'fig-ncc-covid19owid')]),
            type="default"
        ),
        dcc.Loading(
            id="fccc-covid19owid-loading-graph",
            children=html.Div([dcc.Graph(id = 'fig-ccc-covid19owid')]),
            type="default"
        ),
        dcc.Loading(
            id="fndc-covid19owid-loading-graph",
            children=html.Div([dcc.Graph(id = 'fig-ndc-covid19owid')]),
            type="default"
        ),
        dcc.Loading(
            id="fcdc-covid19owid-loading-graph",
            children=html.Div([dcc.Graph(id = 'fig-cdc-covid19owid')]),
            type="default"
        )
    ])
])



@app.callback(Output('fcovid19owid-sz-r-output','children'),
             [Input('fcovid19owid-sz-r', 'drag_value')])
def display_value_r(drag_value):
    return "Número de filas: {}".format(drag_value)



@app.callback(Output('fcovid19owid-sz-c-output','children'),
             [Input('fcovid19owid-sz-c', 'drag_value')])
def display_value_c(drag_value):
    return "Número de columnas: {}".format(drag_value)



@app.callback(Output('fcovid19owid-d-output','children'),
             [Input('fcovid19owid-d', 'drag_value')])
def display_value_d(drag_value):
    return "Radio de la esfera de influencia: {}".format(drag_value)



@app.callback(Output('fcovid19owid-D-output','children'),
             [Input('fcovid19owid-D', 'drag_value')])
def display_value_D(drag_value):
    return "Densidad de población: {}".format(drag_value)



@app.callback(Output('fcovid19owid-n-cycles-output','children'),
             [Input('fcovid19owid-n-cycles', 'drag_value')])
def display_value_r(drag_value):
    return "Número de ciclos: {}".format(drag_value)



@app.callback(Output('fcovid19owid-R-0-output','children'),
             [Input('fcovid19owid-R-0', 'drag_value')])
def display_value_r(drag_value):
    return "R_0: {}".format(drag_value)



@app.callback(Output('fcovid19owid-t-infec-output','children'),
             [Input('fcovid19owid-t-infec', 'drag_value')])
def display_value_r(drag_value):
    return "Tiempo que un contagiado puede infectar: {}".format(drag_value)


@app.callback(Output('fcovid19owid-cfr-output','children'),
             [Input('fcovid19owid-cfr', 'drag_value')])
def display_value_r(drag_value):
    return "Case-fatality risk: {}".format(drag_value)


@app.callback(Output('fcovid19owid-t-I-output','children'),
             [Input('fcovid19owid-t-I', 'drag_value')])
def display_value_r(drag_value):
    return "t_I: {}".format(drag_value)



@app.callback(Output('fcovid19owid-p-Q-output','children'),
             [Input('fcovid19owid-p-Q', 'drag_value')])
def display_value_r(drag_value):
    return "p_Q: {}".format(drag_value)



@app.callback(Output('fcovid19owid-t-Q-output','children'),
             [Input('fcovid19owid-t-Q', 'drag_value')])
def display_value_r(drag_value):
    return "t_Q: {}".format(drag_value)



@app.callback(Output('fcovid19owid-t-L-output','children'),
             [Input('fcovid19owid-t-L', 'value')])
def display_value_r(value):
    return "t_L: {}".format(value)



@app.callback(Output('fcovid19owid-t-R-output','children'),
             [Input('fcovid19owid-t-R', 'drag_value')])
def display_value_r(drag_value):
    return "t_R: {}".format(drag_value)



@app.callback(Output('fcovid19owid-E-in-output','children'),
             [Input('fcovid19owid-E-in', 'drag_value')])
def display_value_r(drag_value):
    return "E_in: {}".format(drag_value)



@app.callback(Output('fcovid19owid-I-in-output','children'),
             [Input('fcovid19owid-I-in', 'drag_value')])
def display_value_r(drag_value):
    return "I_in: {}".format(drag_value)


@app.callback(
     [Output("fig-ncc-covid19owid", "figure"),
     Output("fig-ccc-covid19owid", "figure"),
     Output("fig-ndc-covid19owid", "figure"),
     Output("fig-cdc-covid19owid", "figure")],
    [Input('fcovid19owid-button-start', 'n_clicks')],
    [State('fcovid19owid-sz-r','value'),
     State('fcovid19owid-sz-c','value'),
     State('fcovid19owid-d', 'value'),
     State("fcovid19owid-D",'value'),
     State('fcovid19owid-n-cycles','value'),
     State('fcovid19owid-R-0','value'),
     State('fcovid19owid-t-infec','value'),
     State('fcovid19owid-t-I','value'),
     State('fcovid19owid-p-Q','value'),
     State('fcovid19owid-t-Q','value'),
     State('fcovid19owid-cfr','value'),
     State('fcovid19owid-t-L','value'),
     State('fcovid19owid-t-R','value'),
     State('fcovid19owid-E-in','value'),
     State('fcovid19owid-I-in','value'),
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
    df = iterations_covid19owid(
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
    # print(df["% nuevas muertes confirmadas"])
    # print(df["% acumulado muertes confirmadas"])
    # print(df["% nuevas muertes confirmadas"] == df["% acumulado muertes confirmadas"])

    # nuevos casos confirmados
    fig_ncc = go.Figure(data = go.Scatter(x = df["t"],
                                      y = df["% nuevos casos confirmados"],
                                      mode="lines+markers"))
    fig_ncc.update_layout(xaxis_title="t",
                      yaxis_title="% nuevos casos confirmados")

    # acumulado de casos confirmados
    fig_ccc = go.Figure(data = go.Scatter(x = df["t"],
                                      y = df["% de casos confirmados acumulados"],
                                      mode="lines+markers"))
    fig_ccc.update_layout(xaxis_title="t",
                      yaxis_title="% de casos confirmados acumulados")

    # nuevas muertes confirmadas
    fig_ndc = go.Figure(data = go.Scatter(x = df["t"],
                                      y = df["% nuevas muertes confirmadas"],
                                      mode="lines+markers"))
    fig_ndc.update_layout(xaxis_title="t",
                      yaxis_title="% nuevas muertes confirmadas")

    # acumulado miertes confirmadas
    fig_cdc = go.Figure(data = go.Scatter(x = df["t"],
                                      y = df["% acumulado muertes confirmadas"],
                                      mode="lines+markers"))
    fig_cdc.update_layout(xaxis_title="t",
                      yaxis_title="% acumulado muertes confirmadas")



    return fig_ncc, fig_ccc, fig_ndc, fig_cdc
