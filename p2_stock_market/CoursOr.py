
import matplotlib.pyplot as plt
import numpy as np

def plot_mode(n, P0, S0, prob_change=0.8):
    a = 1.2
    b = 0.5
    c = 0.4
    e = 0.55
    d = 0.1

    vectP = [P0]
    vectS = [S0]
    temps = [0]
    P = P0
    S = S0
    
    for i in range(1, n):
        Ptemp = P
        P = c * S + P - d * P * P * P
        S = (1 + e * c) * S - a * Ptemp - b * S * S * S - e * d * Ptemp * Ptemp * Ptemp 

        if np.random.rand() < prob_change:
           S += np.random.uniform(-0.5, 0.5)  # Ajouter une fluctuation normale à P



        vectP.append(P)
        vectS.append(S)
        temps.append(i)
        
    for i in range(0,n):
        vectP[i] = (102.9*(10 + i/365) + 1049.41)*(vectP[i]*0.0659/5 + 1)

    plt.subplot(2, 1, 1)
    plt.plot(temps, vectP, label='P')
    plt.title('Évolution de P au fil du temps')
    plt.xlabel('Jours')
    plt.ylabel('Valeur de P')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(temps, vectS, label='S', color='orange')
    plt.title('Évolution de S au fil du temps')
    plt.xlabel('Jours')
    plt.ylabel('Valeur de S')
    plt.legend()

    plt.tight_layout()

    # Afficher les graphiques
    plt.show()

import numpy as np

plot_mode(500, 0.35, 0.5, prob_change=0.5)