
import apps.utils.basic_rules as rl

from math import inf


##### Cambia E_in y I_in
def iterations_5b(
                   sz_r,
                   sz_c,
                   d,
                   D,
                   n_cycles,
                   R_0,
                   t_infecc,
                   t_I,
                   p_Q,
                   t_Q,
                   cfr,
                   t_L,
                   t_R,
                   l_E_int,
                   l_I_int
                ):
    '''
    PROGRAMA PRINCIPAL
    '''
    d_data={}
    d_data["E_in,I_in"] = []
    d_data["f_infec"] = []
    time = []


    n_p = D * (2*d + 1)**2

    # probabilidad S -> E
    p_E = R_0 / (n_p * t_infecc)
    print("p_E:\t%f" % (p_E))

    # probabilidad de E -> I
    l_p_I = rl.f_p_I()

    ##### ---------------------- Ciclo sobre l_E_in e l_I_in
    for i in range(len(l_I_int)):

        I_int = l_I_int[i]
        E_int = l_E_int[i]

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
                    "d_variable":d_variable}


        arr_population, habs = rl.f_initPop(sz_r, sz_c, D)
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
        d_cont = {"s": [(n_habs - I_int - E_int)/n_habs],
                  "e": [E_int/n_habs],
                  "i":[I_int/n_habs],
                  "q": [0],
                  "r": [0]}

        time.append(0)



        for c in range(1,n_cycles):

            rl.f_evolution(sz_r, sz_c, d_params, arr_tiempo, arr_nt, arr_population, arr_evo)

            d_cont = rl.data_exp(n_habs , d_cont, arr_population)

            time.append(c)

        d_data["E_in,I_in"] += [(E_int, I_int) for k in range(n_cycles)]
        d_data["f_infec"] += d_cont["i"]

    d_data["t"] = time

    return d_data
