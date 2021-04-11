import apps.utils.basic_rules as rl

from math import inf


#### CAMBIA EL p_R <----- Ya tenemos este :v
def iterations_6d(
                   sz_r,
                   sz_c,
                   d,
                   D,
                   n_cycles,
                   R_0,
                   t_infecc,
                   t_I,
                   l_p_Q,
                   t_Q,
                   t_L,
                   t_R,
                   E_int,
                   I_int
                  ):
    '''
    PROGRAMA PRINCIPAL
    '''
    n_cycles = 100
    d_data = {}

    sz_r = 400
    sz_c = 400
    D = 0.46
    d = 2
    l_p_R = [0.001, 0.01 , 0.1,  1]
    # inicialización del dic con los valores a considerar
    for i in range(4):
        d_data["p_R=" + str(l_p_R[i])] = []

    #####
    for p_R in l_p_R:
    ##############################
        # pueden cambiar p_E, p_I, p_Q, p_R y t_Q => t_I y t_R NO CAMBIAN
        p_E =  0.5
        p_I =  0.5
        t_I = 8     ####
        p_Q =  0.1
        t_Q =  2    ####
        #p_R = 0.12
        t_R = 18
        #d = 2
        t_L = 15

        d_params = {"p_E" :  p_E, "p_I" :  p_I, "t_I" : t_I, "p_Q" :  p_Q,
                    "t_Q" :  t_Q, "p_R" : p_R, "t_R" : t_R, "d" : d,
                     "t_L" : t_L, "t":0}

        # personas infectadas y expuestas al principio
        I_int = 6
        E_int = 200

        arr_population, habs = f_initPop(sz_r, sz_c, D)
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

        #### gráficas
        #frac_pers_i = []
        time = []

        #### ANIMACION
        cmap = ListedColormap(["black", "blue", "green", "red", "cyan", "yellow"])
        #fig = plt.figure(dpi = 200, tight_layout = False, constrained_layout = True)
        #plots = []

        ##### Fig 3a
        # no hay en cuarentena ni recuperados, solo suceptibles, expuestos e infects
        d_cont = {"s": [(n_habs - I_int - E_int)/n_habs],
                  "e": [E_int/n_habs],
                  "i":[I_int/n_habs],
                  "q": [0],
                  "r": [0]}

        ####
        #plt.axis('off')
        #img = plt.imshow(arr_population, vmin = 0, vmax = 5, cmap = cmap)
        #plots.append([img])
        #frac_pers_i.append(sum([rw.count(3) for rw in arr_population])/ int(D * sz_r * sz_c))
        time.append(0)




        for c in range(1,n_cycles):
            print(c)
            f_evolution(sz_r, sz_c, d_params, arr_tiempo, arr_nt, arr_population, arr_evo)

            #plt.axis('off')
            #img = plt.imshow(arr_population, vmin = 0, vmax = 5, cmap = cmap)
            #plots.append([img])
            #frac_pers_i.append(sum([rw.count(3) for rw in arr_population])/ int(D * sz_r * sz_c))

            d_cont = data_fig3a(n_habs , d_cont, arr_population)

            time.append(c)
        d_data["p_R=" + str(p_R)] = d_cont["i"]

    ######################################

    # enviar datos a la carpeta de interés
    file_str = "exportedData/Fig6d.csv"
    d_data["t"] = time
    df = pd.DataFrame(d_data)
    df.to_csv(file_str)

    # consideraremos solo ciertas llaves de interés, no todas, para el plot
    # relevant keys
    r_ks = list(d_data.keys())
    r_ks.remove("t")

    df[(df["t"] >= 30) & (df["t"] <= 60)].plot(x = "t", y = r_ks, xlabel = "tiempo (d)",
            ylabel= "fracción de personas infectadas (i)",
            title = "Fig 6d" ,
            color = ["red", "blue", "lime", "cyan", "green"])
    plt.show()
    #print(max(d_cont["i"]))

    print("\n----------- ARCHIVO GENERADO-----------\n")

    # # generar la animación
    # ani = animation.ArtistAnimation(fig, plots, interval=100, blit=True,
    #                                 repeat_delay=1000)
    # Writer = animation.writers['ffmpeg']
    # writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    # ani.save("evolucion_d_{}.mp4".format(d), writer = writer)

if __name__ == "__main__":
    iterations()
