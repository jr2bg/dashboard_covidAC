# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#####
##### Información básica
#####

#sz_r = 200

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)





app.layout = html.Div([
    ######
    ######  Dimensiones del mapa
    html.Div(id="sz-r-output", style={"margin-top":1}),
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
        id="sz-r",
    ),
    
    html.Div(id="sz-c-output", style={"margin-top":20}),
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
        id="sz-c",
    ),
    
    
    
    ######
    ###### radio de la esfera de influencia
    html.Div(id="d-output", style={"margin-top":20}),
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
        id="d",
    ),
    
    
    ######
    ###### densidad de población
    html.Div(id="D-output", style={"margin-top":20}),
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
        id="D",
    ),
    
    
    ######
    ###### Número de ciclos
    html.Div(id="n-cycles-output", style={"margin-top":20}),
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
        id="n-cycles",
    ),
    
    
    # ######
    # ###### R_0
    html.Div(id="R-0-output", style={"margin-top":20}),
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
        id="R-0",
    ),
    
    
    # ######
    # ###### t_infec
    html.Div(id="t-infec-output", style={"margin-top":20}),
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
        id="t-infec",
    ),
    
    
    # ######
    # ###### t_I
    html.Div(id="t-I-output", style={"margin-top":20}),
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
        id="t-I",
    ),
    
    
    # ######
    # ###### p_Q
    html.Div(id="p-Q-output", style={"margin-top":20}),
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
        id="p-Q",
    ),
    
    
    # ######
    # ###### t_Q
    html.Div(id="t-Q-output", style={"margin-top":20}),
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
        id="t-Q",
    ),
    
    
    # ######
    # ###### t_L
    html.Div(id="t-L-output", style={"margin-top":20}),
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
        id="t-L",
    ),
    
    
    # ######
    # ###### t_R
    html.Div(id="t-R-output", style={"margin-top":20}),
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
        id="t-R",
    ),
    
    
    # ######
    # ###### E_in
    html.Div(id="E-in-output", style={"margin-top":20}),
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
        id="E-in",
    ),
    
    
    # ######
    # ###### I_in
    html.Div(id="I-in-output", style={"margin-top":20}),
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
        id="I-in",
    ),
    
    
    
    # ######
    # ######
    html.Div(id='inpt-tst-output', style={"margin-top":20}),
    dcc.Input(
        type="text",
        placeholder="valores separados por comas",
        value='',
        id="inpt-ts",
    ),
    html.Div(id='inpt-tst2-output', style={"margin-top":20}),
    dcc.Input(
        type="text",
        placeholder="valores separados por comas",
        value='',
        id="inpt-ts2",
    ),
    
    html.Button("START", id='button-start'),
    html.Button("STOP", id='button-stop'),
    html.Div(id="button-pressed",style={"margin-top":20})

    
], style={'columnCount': 2})



@app.callback(Output('sz-r-output','children'),
#             [Input('slider-drag','drag-value'), Input('slider-drag','value')])
             [Input('sz-r', 'drag_value')])
def display_value_r(drag_value):
    #global sz_r
    #sz_r = int(drag_value)
    return "Número de filas: {}".format(drag_value)



@app.callback(Output('sz-c-output','children'),
#             [Input('slider-drag','drag-value'), Input('slider-drag','value')])
             [Input('sz-c', 'drag_value')])
def display_value_c(drag_value):
    return "Número de columnas: {}".format(drag_value)



@app.callback(Output('d-output','children'),
#             [Input('slider-drag','drag-value'), Input('slider-drag','value')])
             [Input('d', 'drag_value')])
def display_value_d(drag_value):
    return "Radio de la esfera de influencia: {}".format(drag_value)



@app.callback(Output('D-output','children'),
#             [Input('slider-drag','drag-value'), Input('slider-drag','value')])
             [Input('D', 'drag_value')])
def display_value_D(drag_value):
    return "Densidad de población: {}".format(drag_value)
    
    
    
@app.callback(Output('n-cycles-output','children'),
#             [Input('slider-drag','drag-value'), Input('slider-drag','value')])
             [Input('n-cycles', 'drag_value')])
def display_value_r(drag_value):
    return "Número de ciclos: {}".format(drag_value)
    


@app.callback(Output('R-0-output','children'),
#             [Input('slider-drag','drag-value'), Input('slider-drag','value')])
             [Input('R-0', 'drag_value')])
def display_value_r(drag_value):
    return "R_0: {}".format(drag_value)    



@app.callback(Output('t-infec-output','children'),
#             [Input('slider-drag','drag-value'), Input('slider-drag','value')])
             [Input('t-infec', 'drag_value')])
def display_value_r(drag_value):
    return "Tiempo que un contagiado puede infectar: {}".format(drag_value) 



@app.callback(Output('t-I-output','children'),
             [Input('t-I', 'drag_value')])
def display_value_r(drag_value):
    return "t_I: {}".format(drag_value) 



@app.callback(Output('p-Q-output','children'),
             [Input('p-Q', 'drag_value')])
def display_value_r(drag_value):
    return "p_Q: {}".format(drag_value) 



@app.callback(Output('t-Q-output','children'),
             [Input('t-Q', 'drag_value')])
def display_value_r(drag_value):
    return "t_Q: {}".format(drag_value) 



@app.callback(Output('t-L-output','children'),
             [Input('t-L', 'drag_value')])
def display_value_r(drag_value):
    return "t_L: {}".format(drag_value) 



@app.callback(Output('t-R-output','children'),
             [Input('t-R', 'drag_value')])
def display_value_r(drag_value):
    return "t_R: {}".format(drag_value) 



@app.callback(Output('E-in-output','children'),
             [Input('E-in', 'drag_value')])
def display_value_r(drag_value):
    return "E_in: {}".format(drag_value)



@app.callback(Output('I-in-output','children'),
             [Input('I-in', 'drag_value')])
def display_value_r(drag_value):
    return "I_in: {}".format(drag_value)


@app.callback(Output('inpt-tst-output','children'),
             [Input('inpt-ts', 'value')],)
def display_value_txt(value):
    return "Probando entrada: {}".format(value)

@app.callback(Output('inpt-tst2-output','children'),
             [Input('inpt-ts2', 'value')],)
def display_value_txt(value):
    print(value)
    return "Probando entrada: {}".format(value)

@app.callback(
    Output("button-pressed", "children"),
    [Input('button-start', 'n_clicks'),
     Input('button-stop', 'n_clicks'),
     Input('sz-r','value'),
     Input('sz-c','value'),
     Input('d', 'value'),
     Input("D",'value'),
     Input('n-cycles','value'),
     Input('R-0','value'),
     Input('t-infec','value'),
     Input('t-I','value'),
     Input('p-Q','value'),
     Input('t-Q','value'),
     Input('t-L','value'),
     Input('t-R','value'),
     Input('E-in','value'),
     Input('I-in','value'),
     Input('inpt-ts','value')])
def display_values_tot(btn_start,
                       btn_stop,
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
                       E_in,
                       I_in,
                       str_ts):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    
    if 'button-start' in changed_id:
        msg = 'START was most recently clicked'
        vals_ent = str_ts.split(",")
        vals_ent = [float(x) for x in vals_ent]
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
        print("t_L: %d" %(t_L))
        print("t_R: %d" %(t_R))
        print("E_in: %d" %(E_in))
        print("I_in: %d" %(I_in))
        #print("Test_string: %s" %(str_ts))
        print('test string: ' + str(vals_ent)[1:-1])
        #print("sz_c: %d" %(sz_c))
        #print("sz_c: %d" %(sz_c))
    elif 'button-stop' in changed_id:
        msg = 'STOP was most recently clicked'
    #elif 'btn-nclicks-3' in changed_id:
    #    msg = 'Button 3 was most recently clicked'
    else:
        msg = 'None of the buttons have been clicked yet'
    return html.Div(msg)


if __name__ == '__main__':
    app.run_server(debug=True)
