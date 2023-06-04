import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import math

def decimal_range(start, stop, increment):
    while start < stop:
        yield start
        start = round(start+increment,3)

        
# Funktion, die die DGL definiert
def dT_dt(t, T):
    return -k * (T - T_umgebung)

# Anfangsbedingungen
T0 = 80  # Anfangstemperatur der Kaffetasse
t0 = 0   # Anfangszeitpunkt

# Parameter
k = 0.05           # Wärmeaustauschkonstante
T_umgebung = 25    # Umgebungstemperatur

# Bereich, über den wir die Lösung berechnen möchten
t_span = (t0, 500)  # Startzeitpunkt und Endzeitpunkt

for i in decimal_range(0.01,1.0,0.01):
    k=i
    # Lösung der DGL
    solution = solve_ivp(dT_dt, t_span, [T0])

    # Zeitpunkte, an denen die Temperatur berechnet wurde
    t = solution.t

    # Temperaturwerte zu den entsprechenden Zeitpunkten
    T = solution.y[0]

    # Plot der Temperaturänderung
    plt.plot(t, T)
    plt.xlabel('Zeit in Sekunden')
    plt.ylabel('Temperatur in °C')
    plt.title('Temperatur der Kaffetasse, k = ' + str(k))
    plt.grid(True)
    plt.savefig("img"+str(i)+".png")
    plt.close()
