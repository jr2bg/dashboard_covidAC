
import apps.utils.basic_rules as rl

from math import inf

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

from copy import deepcopy

class C_p_R_step:
    '''
    clase que modifica f_p_R para que tenga el step adecuado
    step -> días
    '''
    def __init__(self, step = 1):
        self.step = step

    def C_m_p_R(self, t):
        return rl.f_p_R(t * self.step)



def f_d_cont_app(d_day, d_tot):
    '''
    función que le agrega a d_tot los valores que existen en d_day
    '''
    for key, val in d_day.items():
        d_tot[key].append(val)



#### valores fijos
def iterations_follow_one(
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
    '''
    PROGRAMA PRINCIPAL
    '''
    d_data={}

    d_data["% nuevas muertes confirmadas"] = []
    d_data["% acumulado muertes confirmadas"] = []
    d_data["% de casos confirmados acumulados"] = []
    d_data["% nuevos casos confirmados"] = []

    d_ncont = {"s": [],
               "e": [],
               "i": [],
               "q": [],
               "r": [],
               "d": []}


    casa_ps = { "D": casa_D,
                "S": casa_S,
                "E": casa_E,
                "I": casa_I,
                "Q": casa_Q,
                "R":casa_R
            }

    trans_ps ={
                "D": trans_D,
                "S": trans_S,
                "E": trans_E,
                "I": trans_I,
                "Q": trans_Q,
                "R": trans_R
                }

    work_ps = {
                "D": work_D,
                "S": work_S,
                "E": work_E,
                "I": work_I,
                "Q": work_Q,
                "R": work_R
                }

    step = 1/24

    # número de personas en la vecindad
    # puede conducir a un error
    #n_p = l_D[0] * (2*d + 1)**2

    # probabilidad S -> E
    #p_E = R_0 / (n_p * t_infecc)
    p_E = 0.5
    print("p_E:\t%f" % (p_E))

    # probabilidad de E -> I
    # hay 24 hrs en 1 día
    l_p_I = rl.f_p_I(step = step)

    # p_R
    p_R = C_p_R_step(step = step)

    # diametro estático
    d_variable = False

    d_params = {"p_E" :  p_E,
                "p_I" :  l_p_I,         # pasamos toda la lista
                "t_I" :  t_I,
                "p_Q" :  p_Q,
                "t_Q" :  t_Q,
                "p_R" :  p_R.C_m_p_R,         # pasamos método como key
                "t_R" :  t_R,
                "d"   :  d,
                "t_L" :  t_L,
                "t"   :  0,
                "p_D" :  cfr,
                "d_variable" : d_variable,
                "step": step}

    arr_tiempo = [[0 for i in range(sz_c)] for j in range(sz_r)]
    arr_nt = deepcopy(arr_tiempo)
    arr_evo = []       # se pone pero realmente no tiene utilidad en el código

    arr_casa = []
    arr_work = []
    l_frames = []



    # dias
    for c in range(n_days):
        d_ncont_day = rl.f_one_day_24h(
                                       sz_r,
                                       sz_c,
                                       d_params,
                                       arr_tiempo,
                                       arr_nt,
                                       arr_casa,
                                       arr_work,
                                       arr_evo,
                                       casa_ps,
                                       trans_ps,
                                       work_ps,
                                       l_frames
                                  )
        # apendeo de la nueva información a d_ncont
        f_d_cont_app(d_ncont_day, d_ncont)
        #print(d_ncont)


    # acumulados, hacer copia por que las listas "son punteros"
    d_ncont["cq"] = d_ncont["q"].copy()
    d_ncont["cd"] = d_ncont["d"].copy()
    for c in range(1,n_days):
        d_ncont["cq"][c] += d_ncont["cq"][c - 1]
        d_ncont["cd"][c] += d_ncont["cd"][c - 1]

    #diccionario a pasar
    d_data["% nuevas muertes confirmadas"] += d_ncont["d"]
    d_data["% nuevos casos confirmados"] += d_ncont["q"]
    d_data["% acumulado muertes confirmadas"] += d_ncont["cd"]
    d_data["% de casos confirmados acumulados"] += d_ncont["cq"]


    d_data["t"] = [c for c in range(n_days)]

    return d_data, l_frames
