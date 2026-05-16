# Problème du Sac à dos
# Module : Recherche Opérationnelle 2026

def knapsack(poids, valeurs, capacite, noms):
    n = len(poids)
    dp = [[0] * (capacite + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(capacite + 1):
            dp[i][c] = dp[i-1][c]
            if poids[i-1] <= c:
                avec = dp[i-1][c - poids[i-1]] + valeurs[i-1]
                if avec > dp[i][c]:
                    dp[i][c] = avec

    objets_choisis = []
    c = capacite
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i-1][c]:
            objets_choisis.append(noms[i-1])
            c -= poids[i-1]

    return dp[n][capacite], objets_choisis

# Données
noms     = ['Objet A', 'Objet B', 'Objet C']
poids    = [2, 3, 4]
valeurs  = [3, 4, 5]
capacite = 5

# Résolution
valeur_max, choix = knapsack(poids, valeurs, capacite, noms)

# Résultats
print("=== Résultat du Sac à dos ===")
print(f"Capacité du sac  : {capacite} kg")
print(f"Objets choisis   : {choix}")
print(f"Valeur maximale  : {valeur_max}")