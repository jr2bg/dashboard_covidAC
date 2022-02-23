# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


import plotly.graph_objects as go
import plotly.express as px

import xarray as xr


########## ---------- multiples densidades
from apps.b_follow_one import iterations_follow_one

from app import app



layout = html.Div([

    # Título
    html.Div([
        html.H4("Seguimiento a uno solo")
    ]),


    # Parámetros
    html.Div([

        ### COLUMNA IZQUIERDA
        html.Div([
            ######
            ######  Dimensiones del mapa
            html.Div(id="f-follow-one-sz-r-output", style={"margin-top":1}),
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
                id="f-follow-one-sz-r",
            ),

            html.Div(id="f-follow-one-sz-c-output", style={"margin-top":20}),
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
                id="f-follow-one-sz-c",
            ),



            ######
            ###### radio de la esfera de influencia
            html.Div(id="f-follow-one-d-output", style={"margin-top":20}),
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
                id="f-follow-one-d",
            ),


            # ######
            # ###### densidad de población
            # html.Div(id="f-follow-one-D-output", style={"margin-top":20}),
            # dcc.Input(
            #     type="text",
            #     placeholder="valores separados por comas",
            #     value='',
            #     id="f-follow-one-D",
            # ),


            ######
            ###### Número de días
            html.Div(id="f-follow-one-n-days-output", style={"margin-top":20}),
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
                id="f-follow-one-n-days",
            ),


            # ######
            # ###### R_0
            html.Div(id="f-follow-one-R-0-output", style={"margin-top":20}),
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
                id="f-follow-one-R-0",
            ),


            # ######
            # ###### t_infec
            html.Div(id="f-follow-one-t-infec-output", style={"margin-top":20}),
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
                id="f-follow-one-t-infec",
            ),


            # ######
            # ###### case-fatality ratio (a pesar de no ser constante)
            html.Div(id="f-follow-one-cfr-output", style={"margin-top":20}),
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
                id="f-follow-one-cfr",
            ),
        ]),


        ### COLUMNA DERECHA
        html.Div([
            # ######
            # ###### t_I
            html.Div(id="f-follow-one-t-I-output", style={"margin-top":20}),
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
                id="f-follow-one-t-I",
            ),


            # ######
            # ###### p_Q
            html.Div(id="f-follow-one-p-Q-output", style={"margin-top":20}),
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
                id="f-follow-one-p-Q",
            ),


            # ######
            # ###### t_Q
            html.Div(id="f-follow-one-t-Q-output", style={"margin-top":20}),
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
                id="f-follow-one-t-Q",
            ),


            # ######
            # ###### t_L
            html.Div(id="f-follow-one-t-L-output", style={"margin-top":20}),
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
                id="f-follow-one-t-L",
            ),


            # ######
            # ###### t_R
            html.Div(id="f-follow-one-t-R-output", style={"margin-top":20}),
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
                id="f-follow-one-t-R",
            ),

        ])


    ], style={'columnCount': 2}),

    ##################
    #### parámetros para cada área
    ##################

    ##### Casa
    html.Div(children="PARÁMETROS PARA CASA", style={"margin-top":20}, className="twelve columns"),
    html.Div([
        ##### Densidad
        html.Div([
            dcc.Input(
                type="text",
                placeholder="D: float",
                value='',
                id="f-follow-one-casa-D",
            ),
        ], className="two columns"),

        ##### Suceptible
        html.Div([
            dcc.Input(
                type="text",
                placeholder="S: float",
                value='',
                id="f-follow-one-casa-S",
            ),
        ], className="two columns"),

        ##### Expuesto
        html.Div([
            dcc.Input(
                type="text",
                placeholder="E: float",
                value='',
                id="f-follow-one-casa-E",
            ),
        ], className="two columns"),


        ##### Infectado
        html.Div([
            dcc.Input(
                type="text",
                placeholder="I: float",
                value='',
                id="f-follow-one-casa-I",
            ),
        ], className="two columns"),


        ##### Cuarentena
        html.Div([
            dcc.Input(
                type="text",
                placeholder="Q: float",
                value='',
                id="f-follow-one-casa-Q",
            ),
        ], className="two columns"),

        ##### Recuperado
        html.Div([
            dcc.Input(
                type="text",
                placeholder="R: float",
                value='',
                id="f-follow-one-casa-R",
            ),
        ], className="two columns"),

    ], className="twelve columns"),

    ##### Transporte
    html.Div(children="PARÁMETROS PARA TRANSPORTE", style={"margin-top":20}, className="twelve columns"),
    html.Div([
        ##### Densidad
        html.Div([
            dcc.Input(
                type="text",
                placeholder="D: float",
                value='',
                id="f-follow-one-trans-D",
            ),
        ], className="two columns"),

        ##### Suceptible
        html.Div([
            dcc.Input(
                type="text",
                placeholder="S: float",
                value='',
                id="f-follow-one-trans-S",
            ),
        ], className="two columns"),

        ##### Expuesto
        html.Div([
            dcc.Input(
                type="text",
                placeholder="E: float",
                value='',
                id="f-follow-one-trans-E",
            ),
        ], className="two columns"),


        ##### Infectado
        html.Div([
            dcc.Input(
                type="text",
                placeholder="I: float",
                value='',
                id="f-follow-one-trans-I",
            ),
        ], className="two columns"),


        ##### Cuarentena
        html.Div([
            dcc.Input(
                type="text",
                placeholder="Q: float",
                value='',
                id="f-follow-one-trans-Q",
            ),
        ], className="two columns"),

        ##### Recuperado
        html.Div([
            dcc.Input(
                type="text",
                placeholder="R: float",
                value='',
                id="f-follow-one-trans-R",
            ),
        ], className="two columns"),

    ], className="twelve columns"),


    ##### Trabajo
    html.Div(children="PARÁMETROS PARA TRABAJO", style={"margin-top":20}, className="twelve columns"),
    html.Div([
        ##### Densidad
        html.Div([
            dcc.Input(
                type="text",
                placeholder="D: float",
                value='',
                id="f-follow-one-work-D",
            ),
        ], className="two columns"),

        ##### Suceptible
        html.Div([
            dcc.Input(
                type="text",
                placeholder="S: float",
                value='',
                id="f-follow-one-work-S",
            ),
        ], className="two columns"),

        ##### Expuesto
        html.Div([
            dcc.Input(
                type="text",
                placeholder="E: float",
                value='',
                id="f-follow-one-work-E",
            ),
        ], className="two columns"),


        ##### Infectado
        html.Div([
            dcc.Input(
                type="text",
                placeholder="I: float",
                value='',
                id="f-follow-one-work-I",
            ),
        ], className="two columns"),


        ##### Cuarentena
        html.Div([
            dcc.Input(
                type="text",
                placeholder="Q: float",
                value='',
                id="f-follow-one-work-Q",
            ),
        ], className="two columns"),

        ##### Recuperado
        html.Div([
            dcc.Input(
                type="text",
                placeholder="R: float",
                value='',
                id="f-follow-one-work-R",
            ),
        ], className="two columns"),

    ], className="twelve columns"),


    ###
    ### Botón de inicio
    ###
    html.Button("START", id='f-follow-one-button-start', n_clicks=0),
    html.Div(id="f-follow-one-program-status",style={"margin-top":20}),

    #############
    #######   Animación
    ############
    html.Div([
        dcc.Loading(
            id="anim-follow-one-loading-graph",
            children=html.Div([dcc.Graph(id="anim-follow-one")]),
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
                    id="fncc-follow-one-loading-graph",
                    children=html.Div([dcc.Graph(id = 'fig-ncc-follow-one')]),
                    type="default"
                ),
            ], className= "six columns"),
            html.Div([
                dcc.Loading(
                    id="fccc-follow-one-loading-graph",
                    children=html.Div([dcc.Graph(id = 'fig-ccc-follow-one')]),
                    type="default"
                ),
            ], className="six columns")
        ], className= "row"),
        html.Div([
            html.Div([
                dcc.Loading(
                    id="fndc-follow-one-loading-graph",
                    children=html.Div([dcc.Graph(id = 'fig-ndc-follow-one')]),
                    type="default"
                ),
            ], className="six columns"),
            html.Div([
                dcc.Loading(
                    id="fcdc-follow-one-loading-graph",
                    children=html.Div([dcc.Graph(id = 'fig-cdc-follow-one')]),
                    type="default"
                )
            ], className="six columns"),
        ], className="row")
    ])
])



@app.callback(Output('f-follow-one-sz-r-output','children'),
             [Input('f-follow-one-sz-r', 'drag_value')])
def display_value_r(drag_value):
    return "Número de filas: {}".format(drag_value)



@app.callback(Output('f-follow-one-sz-c-output','children'),
             [Input('f-follow-one-sz-c', 'drag_value')])
def display_value_c(drag_value):
    return "Número de columnas: {}".format(drag_value)



@app.callback(Output('f-follow-one-d-output','children'),
             [Input('f-follow-one-d', 'drag_value')])
def display_value_d(drag_value):
    return "Radio de la esfera de influencia: {}".format(drag_value)



# @app.callback(Output('f-follow-one-D-output','children'),
#              [Input('f-follow-one-D', 'value')])
# def display_value_D(drag_value):
#     return "Densidades de población: {}".format(drag_value)



@app.callback(Output('f-follow-one-n-days-output','children'),
             [Input('f-follow-one-n-days', 'value')])
def display_value_r(drag_value):
    return "Número de ciclos: {}".format(drag_value)



@app.callback(Output('f-follow-one-R-0-output','children'),
             [Input('f-follow-one-R-0', 'drag_value')])
def display_value_r(drag_value):
    return "R_0: {}".format(drag_value)



@app.callback(Output('f-follow-one-t-infec-output','children'),
             [Input('f-follow-one-t-infec', 'drag_value')])
def display_value_r(drag_value):
    return "Tiempo que un contagiado puede infectar: {}".format(drag_value)


@app.callback(Output('f-follow-one-cfr-output','children'),
             [Input('f-follow-one-cfr', 'drag_value')])
def display_value_r(drag_value):
    return "Case-fatality risk: {}".format(drag_value)


@app.callback(Output('f-follow-one-t-I-output','children'),
             [Input('f-follow-one-t-I', 'drag_value')])
def display_value_r(drag_value):
    return "t_I: {}".format(drag_value)



@app.callback(Output('f-follow-one-p-Q-output','children'),
             [Input('f-follow-one-p-Q', 'drag_value')])
def display_value_r(drag_value):
    return "p_Q: {}".format(drag_value)



@app.callback(Output('f-follow-one-t-Q-output','children'),
             [Input('f-follow-one-t-Q', 'drag_value')])
def display_value_r(drag_value):
    return "t_Q: {}".format(drag_value)



@app.callback(Output('f-follow-one-t-L-output','children'),
             [Input('f-follow-one-t-L', 'value')])
def display_value_r(value):
    return "t_L: {}".format(value)



@app.callback(Output('f-follow-one-t-R-output','children'),
             [Input('f-follow-one-t-R', 'drag_value')])
def display_value_r(drag_value):
    return "t_R: {}".format(drag_value)



@app.callback(
     [Output("fig-ncc-follow-one", "figure"),
     Output("fig-ccc-follow-one", "figure"),
     Output("fig-ndc-follow-one", "figure"),
     Output("fig-cdc-follow-one", "figure"),
     Output("anim-follow-one", "figure")],

    [Input('f-follow-one-button-start', 'n_clicks')],

    [State('f-follow-one-sz-r','value'),
     State('f-follow-one-sz-c','value'),
     State('f-follow-one-d', 'value'),
     State('f-follow-one-n-days','value'),
     State('f-follow-one-R-0','value'),
     State('f-follow-one-t-infec','value'),
     State('f-follow-one-t-I','value'),
     State('f-follow-one-p-Q','value'),
     State('f-follow-one-t-Q','value'),
     State('f-follow-one-cfr','value'),
     State('f-follow-one-t-L','value'),
     State('f-follow-one-t-R','value'),

     State('f-follow-one-casa-D','value'),
     State('f-follow-one-casa-S','value'),
     State('f-follow-one-casa-E','value'),
     State('f-follow-one-casa-I','value'),
     State('f-follow-one-casa-Q','value'),
     State('f-follow-one-casa-R','value'),

     State('f-follow-one-trans-D','value'),
     State('f-follow-one-trans-S','value'),
     State('f-follow-one-trans-E','value'),
     State('f-follow-one-trans-I','value'),
     State('f-follow-one-trans-Q','value'),
     State('f-follow-one-trans-R','value'),

     State('f-follow-one-work-D','value'),
     State('f-follow-one-work-S','value'),
     State('f-follow-one-work-E','value'),
     State('f-follow-one-work-I','value'),
     State('f-follow-one-work-Q','value'),
     State('f-follow-one-work-R','value'),
     ])
def display_values_tot(btn_start,
                       sz_r,
                       sz_c,
                       d,
                       n_days,
                       R_0,
                       t_infec,
                       t_I,
                       p_Q,
                       t_Q,
                       cfr,
                       t_L,
                       t_R,

                       casa_D,
                       casa_S,
                       casa_E,
                       casa_I,
                       casa_Q,
                       casa_R,

                       trans_D,
                       trans_S,
                       trans_E,
                       trans_I,
                       trans_Q,
                       trans_R,

                       work_D,
                       work_S,
                       work_E,
                       work_I,
                       work_Q,
                       work_R
                       ):
    casa_D = float(casa_D)
    casa_S = float(casa_S)
    casa_E = float(casa_E)
    casa_I = float(casa_I)
    casa_Q = float(casa_Q)
    casa_R = float(casa_R)

    trans_D = float(trans_D)
    trans_S = float(trans_S)
    trans_E = float(trans_E)
    trans_I = float(trans_I)
    trans_Q = float(trans_Q)
    trans_R = float(trans_R)

    work_D = float(work_D)
    work_S = float(work_S)
    work_E = float(work_E)
    work_I = float(work_I)
    work_Q = float(work_Q)
    work_R = float(work_R)

    print("sz_r: %d" %(sz_r))
    print("sz_c: %d" %(sz_c))
    print("d: %d" %(d))
    print("n_days: %d" %(n_days))
    print("R_0: %f" %(R_0))
    print("t_infec: %d" %(t_infec))
    print("t_I: %d" %(t_I))
    print("p_Q: %f" %(p_Q))
    print("t_Q: %d" %(t_Q))
    print("p_D: %d" %(cfr))
    print('t_L: %f' %(t_L))
    print("t_R: %d" %(t_R))

    df, l_frames= iterations_follow_one(
                                       sz_r,
                                       sz_c,
                                       d,
                                       n_days,
                                       R_0,
                                       t_infec,
                                       t_I,
                                       p_Q,
                                       t_Q,
                                       cfr,
                                       t_L,
                                       t_R,

                                       casa_D,
                                       casa_S,
                                       casa_E,
                                       casa_I,
                                       casa_Q,
                                       casa_R,

                                       trans_D,
                                       trans_S,
                                       trans_E,
                                       trans_I,
                                       trans_Q,
                                       trans_R,

                                       work_D,
                                       work_S,
                                       work_E,
                                       work_I,
                                       work_Q,
                                       work_R
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
                          coords={"tiempo":[t/24 for t in range(n_days * 24)]}
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
