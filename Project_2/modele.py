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

        if np.random.rand() <= prob_change:
            x = np.random.normal(0, 0.20) # Ajouter une distribution gaussienne à P
            S += x
            


        vectP.append(P)
        vectS.append(S)
        temps.append(i)
        

    plt.subplot(3, 1, 1)
    plt.plot(temps, vectP, label='P')
    plt.title('Évolution de P au fil du temps avec fluctuations aléatoires')
    plt.xlabel('Jours')
    plt.ylabel('Valeur de P')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(temps, vectS, label='S', color='orange')
    plt.title('Évolution de S au fil du temps avec fluctuations aléatoires')
    plt.xlabel('Jours')
    plt.ylabel('Valeur de S')
    plt.legend()

    plt.subplot(3, 1, 3)
    #plt.plot(temps, vectP, label='P')
    plt.plot(temps, vectP, label='P avec fluctuations aléatoires')
    #plt.plot(temps, vectS, label='S', color='orange')
    plt.plot(temps, vectS, label='S avec fluctuations aléatoires', color='orange')
    plt.title('Superposition de P et S avec fluctuations aléatoires au fil du temps')
    #plt.title('Superposition de P et S')
    plt.xlabel('Jours')
    plt.ylabel('Valeur')
    plt.legend()

    plt.tight_layout()

    # Afficher les graphiques
    plt.show()

plot_mode(500, -1.585, 0)
