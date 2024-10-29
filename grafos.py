import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

G = nx.Graph()

estados = ["Aguascalientes", "Jalisco", "Zacatecas", "San Luis Potosí", "Guanajuato", "Michoacán", "Querétaro"]
G.add_nodes_from(estados)

costos = {
    ("Aguascalientes", "Jalisco"): 100,
    ("Aguascalientes", "Zacatecas"): 150,
    ("Jalisco", "Zacatecas"): 200,
    ("Jalisco", "San Luis Potosí"): 120,
    ("Zacatecas", "San Luis Potosí"): 180,
    ("San Luis Potosí", "Guanajuato"): 110,
    ("Guanajuato", "Michoacán"): 130,
    ("Michoacán", "Querétaro"): 140,
    ("Querétaro", "San Luis Potosí"): 160,
}

for (estado1, estado2), costo in costos.items():
    G.add_edge(estado1, estado2, weight=costo)

def calcular_costo(recorrido):
    costo_total = 0
    for i in range(len(recorrido) - 1):
        if G.has_edge(recorrido[i], recorrido[i + 1]):
            costo_total += G[recorrido[i]][recorrido[i + 1]]['weight']
        else:
            return float('inf')
    return costo_total

def recorrido_sin_repetir():
    min_costo = float('inf')
    mejor_recorrido = None
    for perm in permutations(estados):
        costo = calcular_costo(perm)
        if costo < min_costo:
            min_costo = costo
            mejor_recorrido = perm
    return mejor_recorrido, min_costo

def recorrido_con_repeticion():
    max_costo = float('-inf')
    mejor_recorrido = None
    for estado in estados:

        for perm in permutations(estados + [estado], len(estados) + 1):
            costo = calcular_costo(perm)
            if costo > max_costo:
                max_costo = costo
                mejor_recorrido = perm
    return mejor_recorrido, max_costo

def mostrar_relaciones():
    print("Relaciones entre los estados y sus costos:")
    print("| Estado 1            | Estado 2            | Costo de Traslado |")
    print("|---------------------|---------------------|--------------------|")
    
    for (estado1, estado2), costo in costos.items():
        print(f"| {estado1:<20} | {estado2:<20} | {costo:<18} |")

mostrar_relaciones()

recorrido_a, costo_a = recorrido_sin_repetir()
recorrido_b, costo_b = recorrido_con_repeticion()

print(f"\nRecorrido sin repetir: {recorrido_a} con costo: {costo_a}")
print(f"Recorrido con repetición: {recorrido_b} con costo: {costo_b}")

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Grafo de Estados y Costos")
plt.show()
