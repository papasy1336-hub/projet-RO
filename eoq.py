# Problème EOQ - Gestion de stock
# Module : Recherche Opérationnelle 2026
import math
import matplotlib.pyplot as plt
import numpy as np

# Données
D = 1200  # Demande annuelle
S = 50    # Coût de commande
H = 2     # Coût de stockage

# Calcul EOQ
EOQ = math.sqrt((2 * D * S) / H)
N = D / EOQ
CT = (D/EOQ)*S + (EOQ/2)*H

# Affichage
print("=== Résultat EOQ ===")
print(f"Quantité optimale (EOQ) : {EOQ:.2f} unités")
print(f"Nombre de commandes/an  : {N:.2f}")
print(f"Coût total minimal      : {CT:.2f} MRU")

# Graphique
Q = np.linspace(10, 500, 200)
cout_commande = (D/Q) * S
cout_stockage = (Q/2) * H
cout_total = cout_commande + cout_stockage

plt.plot(Q, cout_commande, label="Coût commande", color="blue")
plt.plot(Q, cout_stockage, label="Coût stockage", color="red")
plt.plot(Q, cout_total, label="Coût total", color="green")
plt.axvline(x=EOQ, color="black", linestyle="--", label=f"EOQ={EOQ:.0f}")
plt.xlabel("Quantité Q")
plt.ylabel("Coût (MRU)")
plt.title("Optimisation EOQ")
plt.legend()
plt.grid(True)
plt.savefig("graphique_eoq.png")
plt.show()