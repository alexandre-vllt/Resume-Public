import matplotlib.pyplot as plt
import numpy as np



def plot_mode(n, P0, S0, capital, constante, prob_change=1):
    a, b, c , d, e = 1.2 ,0.5 ,0.4 ,0.55 , 0.1
    vectC, vectA, vectP, vectS, vectF = [capital], [0], [P0], [S0], [capital]
    temps, variations_P, actions = [0], [], 0
    P, S, deltaP = P0, S0, 0.4

    for i in range(1, n):
        Ptemp = P
        P = c * S + P - d * P * P * P
        S = (1 + e * c) * S - a * Ptemp - b * S * S * S - e * d * Ptemp * Ptemp * Ptemp 

        #ajout des non linéarités
        if np.random.rand() < prob_change:
           S += np.random.normal(0 ,0.20) 
        
        #MàJ de Pdelta 
        variation = P - vectP[-1]
        variations_P.append(abs(variation))
        if len(variations_P) > 100:
            variations_P.pop(0)
        Pdelta = 1.5*np.mean(variations_P) 


        # Logique d'achat 
        if variation < -deltaP and len(variations_P)==100:
            quantite_achat = capital * (-deltaP - variation)
            cout_achat = quantite_achat * P
            # Achat si le capital est suffisant
            if cout_achat <= capital:
                capital -= cout_achat
                S += quantite_achat/1000
                actions+=quantite_achat
            else:
                quantite_achat = capital / P
                capital = 0
                S += quantite_achat/1000
                actions+=quantite_achat

        # Logique de vente
        elif variation > deltaP and len(variations_P)==100:
            quantite_vente = capital * (variation - deltaP)
            # Assurer que la banque ne vend pas plus que ce qu'elle détient
            if quantite_vente<actions:
                quantite_vente = quantite_vente
                capital += quantite_vente * P
                S -= quantite_vente/1000
                actions-=quantite_vente
   
        vectP.append(P)
        vectS.append(S)
        temps.append(i)
        vectC.append(capital)
        vectA.append(actions)
        vectF.append(capital+actions*P)


    plt.subplot(4, 1, 1)
    plt.plot(temps, vectP, label='P')
    plt.title('Évolution de P au fil du temps')
    plt.xlabel('Jours')
    plt.ylabel('Valeur de P')
    plt.legend()

    plt.subplot(4, 1, 2)
    plt.plot(temps, vectS, label='S', color='orange')
    plt.title('Évolution de S au fil du temps')
    plt.xlabel('Jours')
    plt.ylabel('Valeur de S')
    plt.legend()

    plt.subplot(4, 1, 3)
    plt.plot(temps, vectC, label='C', color='green')
    plt.title('Évolution de l´argent au fil du temps')
    plt.xlabel('Jours')
    plt.ylabel('Valeur de C')
    plt.legend()

    plt.subplot(4, 1, 4)
    plt.plot(temps, vectA, label='A', color='violet')
    plt.title('Évolution du nombre d´actions au fil du temps')
    plt.xlabel('Jours')
    plt.ylabel('Valeur de A')
    plt.legend()

    

    plt.tight_layout()

    # Afficher les graphiques
    plt.show()

    
    
plot_mode(250, 0.35, 0.35, 5,0.4)
    

    



