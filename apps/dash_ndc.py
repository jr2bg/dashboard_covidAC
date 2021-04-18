# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


import plotly.express as px
import plotly.graph_objects as go


########## ---------- Figura nuevas muertes confirmadas por COVID
from apps.b_ndc import iterations_ndc

from app import app



layout = html.Div([

    # Título
    html.Div([
        html.H4("Nuevas muertes confirmadas")
    ]),


    # Parámetros
    html.Div([

        ### COLUMNA IZQUIERDA
        html.Div([
            ######
            ######  Dimensiones del mapa
            html.Div(id="fndc-sz-r-output", style={"margin-top":1}),
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
                id="fndc-sz-r",
            ),

            html.Div(id="fndc-sz-c-output", style={"margin-top":20}),
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
                id="fndc-sz-c",
            ),



            ######
            ###### radio de la esfera de influencia
            html.Div(id="fndc-d-output", style={"margin-top":20}),
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
                id="fndc-d",
            ),


            ######
            ###### densidad de población
            html.Div(id="fndc-D-output", style={"margin-top":20}),
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
                id="fndc-D",
            ),


            ######
            ###### Número de ciclos
            html.Div(id="fndc-n-cycles-output", style={"margin-top":20}),
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
                id="fndc-n-cycles",
            ),


            # ######
            # ###### R_0
            html.Div(id="fndc-R-0-output", style={"margin-top":20}),
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
                id="fndc-R-0",
            ),


            # ######
            # ###### t_infec
            html.Div(id="fndc-t-infec-output", style={"margin-top":20}),
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
                id="fndc-t-infec",
            ),

            # ######
            # ###### case-fatality ratio (a pesar de no ser constante)
            html.Div(id="fndc-cfr-output", style={"margin-top":20}),
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
                id="fndc-cfr",
            ),
        ]),


        ### COLUMNA DERECHA
        html.Div([
            # ######
            # ###### t_I
            html.Div(id="fndc-t-I-output", style={"margin-top":20}),
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
                id="fndc-t-I",
            ),


            # ######
            # ###### p_Q
            html.Div(id="fndc-p-Q-output", style={"margin-top":20}),
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
                id="fndc-p-Q",
            ),


            # ######
            # ###### t_Q
            html.Div(id="fndc-t-Q-output", style={"margin-top":20}),
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
                id="fndc-t-Q",
            ),


            # ######
            # ###### t_L
            html.Div(id="fndc-t-L-output", style={"margin-top":20}),
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
                id="fndc-t-L",
            ),


            # ######
            # ###### t_R
            html.Div(id="fndc-t-R-output", style={"margin-top":20}),
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
                id="fndc-t-R",
            ),


            # ######
            # ###### E_in
            html.Div(id="fndc-E-in-output", style={"margin-top":20}),
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
                id="fndc-E-in",
            ),


            # ######
            # ###### I_in
            html.Div(id="fndc-I-in-output", style={"margin-top":20}),
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
                id="fndc-I-in",
            ),
        ])


    ], style={'columnCount': 2}),

    ###
    ### Botón de inicio
    ###
    html.Button("START", id='fndc-button-start', n_clicks=0),
    html.Div(id="fndc-program-status",style={"margin-top":20}),

    #############
    #######   GRÁFICA
    ############
    html.Div([
        dcc.Loading(
            id="fndc-loading-graph",
            children=html.Div([dcc.Graph(id = 'fig-ndc')]),
            type="default"
        )
    ])
])



@app.callback(Output('fndc-sz-r-output','children'),
             [Input('fndc-sz-r', 'drag_value')])
def display_value_r(drag_value):
    return "Número de filas: {}".format(drag_value)



@app.callback(Output('fndc-sz-c-output','children'),
             [Input('fndc-sz-c', 'drag_value')])
def display_value_c(drag_value):
    return "Número de columnas: {}".format(drag_value)



@app.callback(Output('fndc-d-output','children'),
             [Input('fndc-d', 'drag_value')])
def display_value_d(drag_value):
    return "Radio de la esfera de influencia: {}".format(drag_value)



@app.callback(Output('fndc-D-output','children'),
             [Input('fndc-D', 'drag_value')])
def display_value_D(drag_value):
    return "Densidad de población: {}".format(drag_value)



@app.callback(Output('fndc-n-cycles-output','children'),
             [Input('fndc-n-cycles', 'drag_value')])
def display_value_r(drag_value):
    return "Número de ciclos: {}".format(drag_value)



@app.callback(Output('fndc-R-0-output','children'),
             [Input('fndc-R-0', 'drag_value')])
def display_value_r(drag_value):
    return "R_0: {}".format(drag_value)



@app.callback(Output('fndc-t-infec-output','children'),
             [Input('fndc-t-infec', 'drag_value')])
def display_value_r(drag_value):
    return "Tiempo que un contagiado puede infectar: {}".format(drag_value)


@app.callback(Output('fndc-cfr-output','children'),
             [Input('fndc-cfr', 'drag_value')])
def display_value_r(drag_value):
    return "Case-fatality risk: {}".format(drag_value)


@app.callback(Output('fndc-t-I-output','children'),
             [Input('fndc-t-I', 'drag_value')])
def display_value_r(drag_value):
    return "t_I: {}".format(drag_value)



@app.callback(Output('fndc-p-Q-output','children'),
             [Input('fndc-p-Q', 'drag_value')])
def display_value_r(drag_value):
    return "p_Q: {}".format(drag_value)



@app.callback(Output('fndc-t-Q-output','children'),
             [Input('fndc-t-Q', 'drag_value')])
def display_value_r(drag_value):
    return "t_Q: {}".format(drag_value)



@app.callback(Output('fndc-t-L-output','children'),
             [Input('fndc-t-L', 'value')])
def display_value_r(value):
    return "t_L: {}".format(value)



@app.callback(Output('fndc-t-R-output','children'),
             [Input('fndc-t-R', 'drag_value')])
def display_value_r(drag_value):
    return "t_R: {}".format(drag_value)



@app.callback(Output('fndc-E-in-output','children'),
             [Input('fndc-E-in', 'drag_value')])
def display_value_r(drag_value):
    return "E_in: {}".format(drag_value)



@app.callback(Output('fndc-I-in-output','children'),
             [Input('fndc-I-in', 'drag_value')])
def display_value_r(drag_value):
    return "I_in: {}".format(drag_value)


@app.callback(
     Output("fig-ndc", "figure"),
    [Input('fndc-button-start', 'n_clicks')],
    [State('fndc-sz-r','value'),
     State('fndc-sz-c','value'),
     State('fndc-d', 'value'),
     State("fndc-D",'value'),
     State('fndc-n-cycles','value'),
     State('fndc-R-0','value'),
     State('fndc-t-infec','value'),
     State('fndc-t-I','value'),
     State('fndc-p-Q','value'),
     State('fndc-t-Q','value'),
     State('fndc-cfr','value'),
     State('fndc-t-L','value'),
     State('fndc-t-R','value'),
     State('fndc-E-in','value'),
     State('fndc-I-in','value'),
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
    # p_D -> probabilidad de deceso
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
    df = iterations_ndc(
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
    fig = px.scatter(df, x = "t", y = "% nuevas muertes confirmadas")

    return fig
