
import apps.utils.basic_rules as rl

from math import inf


#### valores fijos
def iterations_multDensities(
                   sz_r,
                   sz_c,
                   d,
                   l_D,
                   l_n_cycles,
                   R_0,
                   t_infecc,
                   t_I,
                   p_Q,
                   t_Q,
                   cfr,
                   t_L,
                   t_R,
                   E_int,
                   I_int
                  ):
    '''
    PROGRAMA PRINCIPAL
    '''
    d_data={}

    d_data["% nuevas muertes confirmadas"] = []
    d_data["% acumulado muertes confirmadas"] = []
    d_data["% de casos confirmados acumulados"] = []
    d_data["% nuevos casos confirmados"] = []
    time = []

    # número de personas en la vecindad
    # puede conducir a un error
    n_p = l_D[0] * (2*d + 1)**2

    # probabilidad S -> E
    p_E = R_0 / (n_p * t_infecc)
    print("p_E:\t%f" % (p_E))

    # probabilidad de E -> I
    l_p_I = rl.f_p_I()


    d_variable = True

    d_params = {"p_E" :  p_E,
                "p_I" :  l_p_I,         # pasamos toda la lista
                "t_I" :  t_I,
                "p_Q" :  p_Q,
                "t_Q" :  t_Q,
                "p_R" :  rl.f_p_R,         # pasamos la función como key
                "t_R" :  t_R,
                "d"   :  d,
                "t_L" :  t_L,
                "t"   :  0,
                "p_D" :  cfr,
                "d_variable" : d_variable}


    arr_population, habs = rl.f_initPop(sz_r, sz_c,l_D[0])
    arr_tiempo = [[0 for i in range(sz_c)] for j in range(sz_r)]

    n_habs = len(habs)

    #### población infectada o expuesta al tiempo 0
    pop_i0 = habs[:I_int]
    pop_e0 = habs[I_int: E_int + I_int]



    for r,c in pop_i0:
        arr_population[r][c] = 3
    for r,c in pop_e0:
        arr_population[r][c] = 2
    ####

    arr_evo = arr_population.copy()
    arr_nt = arr_tiempo.copy()

    #### tiempo primer infectado ---> t_fi
    t_fi = 0

    # no hay en cuarentena ni recuperados, solo suceptibles, expuestos e infects
    d_ncont = {"s": [(n_habs - I_int - E_int)/n_habs],
              "e": [E_int/n_habs],
              "i":[I_int/n_habs],
              "q": [0],
              "r": [0],
              "d": [0]}

    time.append(0)


    # 1er ciclo
    for c in range(1,l_n_cycles[0]):
        #print(c)
        rl.f_evolution(sz_r, sz_c, d_params, arr_tiempo, arr_nt, arr_population, arr_evo)

        d_ncont = rl.data_number_nstates(sz_r, sz_c, n_habs , d_ncont, arr_population, arr_tiempo)

        time.append(c)

    #########################################
    # 2do ciclo
    # cambio de la densidad de población
    change_pop = int((l_D[1] - l_D[0]) * sz_r * sz_c)
    # si el cambio es mayor => hay que introducir elementos, dados por change_pop
    # si el cambio es menor => hay que remover elementos, dados por change_pop
    rl.f_newPop(sz_r, sz_c, arr_population, change_pop)

    for c in range(l_n_cycles[0], l_n_cycles[0] + l_n_cycles[1]):
        #print(c)
        rl.f_evolution(sz_r, sz_c, d_params, arr_tiempo, arr_nt, arr_population, arr_evo)

        d_ncont = rl.data_number_nstates(sz_r, sz_c, n_habs , d_ncont, arr_population, arr_tiempo)

        time.append(c)

    #########################################
    # 3er ciclo
    # cambio de la densidad de población
    change_pop = int((l_D[2] - l_D[1]) * sz_r * sz_c)
    # si el cambio es mayor => hay que introducir elementos, dados por change_pop
    # si el cambio es menor => hay que remover elementos, dados por change_pop
    rl.f_newPop(sz_r, sz_c, arr_population, change_pop)
    for c in range(l_n_cycles[0] + l_n_cycles[1], l_n_cycles[0] + l_n_cycles[1] + l_n_cycles[2]):

        rl.f_evolution(sz_r, sz_c, d_params, arr_tiempo, arr_nt, arr_population, arr_evo)

        d_ncont = rl.data_number_nstates(sz_r, sz_c, n_habs , d_ncont, arr_population, arr_tiempo)

        time.append(c)


    ########################################
    print("tamanio tiempo:\t",len(time))
    # acumulados, hacer copia por que las listas "son punteros"
    d_ncont["cq"] = d_ncont["q"].copy()
    d_ncont["cd"] = d_ncont["d"].copy()
    for c in range(1,sum(l_n_cycles)):
        d_ncont["cq"][c] += d_ncont["cq"][c - 1]
        d_ncont["cd"][c] += d_ncont["cd"][c - 1]

    #diccionario a pasar
    d_data["% nuevas muertes confirmadas"] += d_ncont["d"]
    d_data["% nuevos casos confirmados"] += d_ncont["q"]
    d_data["% acumulado muertes confirmadas"] += d_ncont["cd"]
    d_data["% de casos confirmados acumulados"] += d_ncont["cq"]


    d_data["t"] = time

    return d_data
