# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


import plotly.graph_objects as go
import plotly.express as px

import xarray as xr


########## ---------- multiples densidades
from apps.b_multDensities import iterations_multDensities

from app import app



layout = html.Div([

    # Título
    html.Div([
        html.H4("Diferentes densidades con distinto número de ciclos")
    ]),


    # Parámetros
    html.Div([

        ### COLUMNA IZQUIERDA
        html.Div([
            ######
            ######  Dimensiones del mapa
            html.Div(id="fmultDensities-sz-r-output", style={"margin-top":1}),
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
                id="fmultDensities-sz-r",
            ),

            html.Div(id="fmultDensities-sz-c-output", style={"margin-top":20}),
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
                id="fmultDensities-sz-c",
            ),



            ######
            ###### radio de la esfera de influencia
            html.Div(id="fmultDensities-d-output", style={"margin-top":20}),
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
                id="fmultDensities-d",
            ),


            ######
            ###### densidad de población
            html.Div(id="fmultDensities-D-output", style={"margin-top":20}),
            dcc.Input(
                type="text",
                placeholder="valores separados por comas",
                value='',
                id="fmultDensities-D",
            ),


            ######
            ###### Número de ciclos
            html.Div(id="fmultDensities-n-cycles-output", style={"margin-top":20}),
            dcc.Input(
                type="text",
                placeholder="valores separados por comas",
                value='',
                id="fmultDensities-n-cycles",
            ),


            # ######
            # ###### R_0
            html.Div(id="fmultDensities-R-0-output", style={"margin-top":20}),
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
                id="fmultDensities-R-0",
            ),


            # ######
            # ###### t_infec
            html.Div(id="fmultDensities-t-infec-output", style={"margin-top":20}),
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
                id="fmultDensities-t-infec",
            ),


            # ######
            # ###### case-fatality ratio (a pesar de no ser constante)
            html.Div(id="fmultDensities-cfr-output", style={"margin-top":20}),
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
                id="fmultDensities-cfr",
            ),
        ]),


        ### COLUMNA DERECHA
        html.Div([
            # ######
            # ###### t_I
            html.Div(id="fmultDensities-t-I-output", style={"margin-top":20}),
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
                id="fmultDensities-t-I",
            ),


            # ######
            # ###### p_Q
            html.Div(id="fmultDensities-p-Q-output", style={"margin-top":20}),
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
                id="fmultDensities-p-Q",
            ),


            # ######
            # ###### t_Q
            html.Div(id="fmultDensities-t-Q-output", style={"margin-top":20}),
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
                id="fmultDensities-t-Q",
            ),


            # ######
            # ###### t_L
            html.Div(id="fmultDensities-t-L-output", style={"margin-top":20}),
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
                id="fmultDensities-t-L",
            ),


            # ######
            # ###### t_R
            html.Div(id="fmultDensities-t-R-output", style={"margin-top":20}),
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
                id="fmultDensities-t-R",
            ),


            # ######
            # ###### E_in
            html.Div(id="fmultDensities-E-in-output", style={"margin-top":20}),
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
                id="fmultDensities-E-in",
            ),


            # ######
            # ###### I_in
            html.Div(id="fmultDensities-I-in-output", style={"margin-top":20}),
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
                id="fmultDensities-I-in",
            ),
        ])


    ], style={'columnCount': 2}),

    ###
    ### Botón de inicio
    ###
    html.Button("START", id='fmultDensities-button-start', n_clicks=0),
    html.Div(id="fmultDensities-program-status",style={"margin-top":20}),

    #############
    #######   Animación
    ############
    html.Div([
        dcc.Loading(
            id="anim-multDensities-loading-graph",
            children=html.Div([dcc.Graph(id="anim-multDensities")]),
            type="default"
        )
    ]),

    #############
    #######   GRÁFICA
    ############
    html.Div([
        html.Div([
            html.Div([
                dcc.Loading(
                    id="fncc-multDensities-loading-graph",
                    children=html.Div([dcc.Graph(id = 'fig-ncc-multDensities')]),
                    type="default"
                ),
            ], className= "six columns"),
            html.Div([
                dcc.Loading(
                    id="fccc-multDensities-loading-graph",
                    children=html.Div([dcc.Graph(id = 'fig-ccc-multDensities')]),
                    type="default"
                ),
            ], className="six columns")
        ], className= "row"),
        html.Div([
            html.Div([
                dcc.Loading(
                    id="fndc-multDensities-loading-graph",
                    children=html.Div([dcc.Graph(id = 'fig-ndc-multDensities')]),
                    type="default"
                ),
            ], className="six columns"),
            html.Div([
                dcc.Loading(
                    id="fcdc-multDensities-loading-graph",
                    children=html.Div([dcc.Graph(id = 'fig-cdc-multDensities')]),
                    type="default"
                )
            ], className="six columns"),
        ], className="row")
    ])
])



@app.callback(Output('fmultDensities-sz-r-output','children'),
             [Input('fmultDensities-sz-r', 'drag_value')])
def display_value_r(drag_value):
    return "Número de filas: {}".format(drag_value)



@app.callback(Output('fmultDensities-sz-c-output','children'),
             [Input('fmultDensities-sz-c', 'drag_value')])
def display_value_c(drag_value):
    return "Número de columnas: {}".format(drag_value)



@app.callback(Output('fmultDensities-d-output','children'),
             [Input('fmultDensities-d', 'drag_value')])
def display_value_d(drag_value):
    return "Radio de la esfera de influencia: {}".format(drag_value)



@app.callback(Output('fmultDensities-D-output','children'),
             [Input('fmultDensities-D', 'value')])
def display_value_D(drag_value):
    return "Densidades de población: {}".format(drag_value)



@app.callback(Output('fmultDensities-n-cycles-output','children'),
             [Input('fmultDensities-n-cycles', 'value')])
def display_value_r(drag_value):
    return "Número de ciclos: {}".format(drag_value)



@app.callback(Output('fmultDensities-R-0-output','children'),
             [Input('fmultDensities-R-0', 'drag_value')])
def display_value_r(drag_value):
    return "R_0: {}".format(drag_value)



@app.callback(Output('fmultDensities-t-infec-output','children'),
             [Input('fmultDensities-t-infec', 'drag_value')])
def display_value_r(drag_value):
    return "Tiempo que un contagiado puede infectar: {}".format(drag_value)


@app.callback(Output('fmultDensities-cfr-output','children'),
             [Input('fmultDensities-cfr', 'drag_value')])
def display_value_r(drag_value):
    return "Case-fatality risk: {}".format(drag_value)


@app.callback(Output('fmultDensities-t-I-output','children'),
             [Input('fmultDensities-t-I', 'drag_value')])
def display_value_r(drag_value):
    return "t_I: {}".format(drag_value)



@app.callback(Output('fmultDensities-p-Q-output','children'),
             [Input('fmultDensities-p-Q', 'drag_value')])
def display_value_r(drag_value):
    return "p_Q: {}".format(drag_value)



@app.callback(Output('fmultDensities-t-Q-output','children'),
             [Input('fmultDensities-t-Q', 'drag_value')])
def display_value_r(drag_value):
    return "t_Q: {}".format(drag_value)



@app.callback(Output('fmultDensities-t-L-output','children'),
             [Input('fmultDensities-t-L', 'value')])
def display_value_r(value):
    return "t_L: {}".format(value)



@app.callback(Output('fmultDensities-t-R-output','children'),
             [Input('fmultDensities-t-R', 'drag_value')])
def display_value_r(drag_value):
    return "t_R: {}".format(drag_value)



@app.callback(Output('fmultDensities-E-in-output','children'),
             [Input('fmultDensities-E-in', 'drag_value')])
def display_value_r(drag_value):
    return "E_in: {}".format(drag_value)



@app.callback(Output('fmultDensities-I-in-output','children'),
             [Input('fmultDensities-I-in', 'drag_value')])
def display_value_r(drag_value):
    return "I_in: {}".format(drag_value)


@app.callback(
     [Output("fig-ncc-multDensities", "figure"),
     Output("fig-ccc-multDensities", "figure"),
     Output("fig-ndc-multDensities", "figure"),
     Output("fig-cdc-multDensities", "figure"),
     Output("anim-multDensities", "figure")],
    [Input('fmultDensities-button-start', 'n_clicks')],
    [State('fmultDensities-sz-r','value'),
     State('fmultDensities-sz-c','value'),
     State('fmultDensities-d', 'value'),
     State("fmultDensities-D",'value'),
     State('fmultDensities-n-cycles','value'),
     State('fmultDensities-R-0','value'),
     State('fmultDensities-t-infec','value'),
     State('fmultDensities-t-I','value'),
     State('fmultDensities-p-Q','value'),
     State('fmultDensities-t-Q','value'),
     State('fmultDensities-cfr','value'),
     State('fmultDensities-t-L','value'),
     State('fmultDensities-t-R','value'),
     State('fmultDensities-E-in','value'),
     State('fmultDensities-I-in','value'),
     ])
def display_values_tot(btn_start,
                       sz_r,
                       sz_c,
                       d,
                       l_D,
                       l_n_cycles,
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

    # lista de ints para los ciclos
    vals_ent = l_n_cycles.split(",")
    l_n_cycles = [int(x) for x in vals_ent]
    # lista de floats para las densidades
    vals_ent = l_D.split(",")
    l_D = [float(x) for x in vals_ent]

    print("sz_r: %d" %(sz_r))
    print("sz_c: %d" %(sz_c))
    print("d: %d" %(d))
    print("list D: " + str(l_D)[1:-1])
    print("list n_cycles: " + str(l_n_cycles)[1:-1])
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
    df, l_frames= iterations_multDensities(
                                           sz_r,
                                           sz_c,
                                           d,
                                           l_D,
                                           l_n_cycles,
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
    fig_ncc.update_layout(title = "Nuevos casos confirmados",
                      xaxis_title="t",
                      yaxis_title="% nuevos casos confirmados")

    # acumulado de casos confirmados
    fig_ccc = go.Figure(data = go.Scatter(x = df["t"],
                                      y = df["% de casos confirmados acumulados"],
                                      mode="lines+markers"))
    fig_ccc.update_layout(title = "Acumulado casos confirmados",
                      xaxis_title="t",
                      yaxis_title="% de casos confirmados acumulados")

    # nuevas muertes confirmadas
    fig_ndc = go.Figure(data = go.Scatter(x = df["t"],
                                      y = df["% nuevas muertes confirmadas"],
                                      mode="lines+markers"))
    fig_ndc.update_layout(title = "Nuevas muertes confirmadas",
                      xaxis_title="t",
                      yaxis_title="% nuevas muertes confirmadas")

    # acumulado miertes confirmadas
    fig_cdc = go.Figure(data = go.Scatter(x = df["t"],
                                      y = df["% acumulado muertes confirmadas"],
                                      mode="lines+markers"))
    fig_cdc.update_layout(title = "Acumulado de muertes confirmadas",
                      xaxis_title="t",
                      yaxis_title="% acumulado muertes confirmadas")

    # frames para la animación
    frames = xr.DataArray(l_frames,
                          dims=("tiempo", "row", "col"),
                          coords={"tiempo":df["t"]}
                          )

    fig_animation=px.imshow(frames,
                            animation_frame="tiempo",
                            #labels={"x":None, "y":None, "color":None},
                            range_color=[0,5],
                            #width=1400,
                            height=800,
                            aspect="equal",
                            #x=None,
                            #y=None
                            )

    return fig_ncc, fig_ccc, fig_ndc, fig_cdc, fig_animation
