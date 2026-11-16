# # 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos nece-
# # sarios para resolver las tareas, listadas a continuación:

# # a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi-
# # dor, router, switch, impresora;

# # b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
# # Red Hat, Debian, Arch;
# # c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
# # Red Hat, Fedora hasta la impresora;
# # d. encontrar el árbol de expansión mínima;
# # e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
# # f. indicar desde que computadora del switch 01 es el camino más corto
# # al servidor “MongoDB”;

# # [230]

# # g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
# # h. debe utilizar un grafo no dirigido.

# from graph import Graph

# # h. debe utilizar un grafo no dirigido
# g = Graph(is_dir=False)

# # a. cada nodo además del nombre del equipo deberá almacenar su tipo:
# # pc, notebook, servidor, router, switch, impresora
# equipos = [
#     ("Red Hat", "notebook"),
#     ("Debian", "notebook"),
#     ("Arch", "notebook"),
#     ("Manjaro", "pc"),
#     ("Fedora", "pc"),
#     ("Ubuntu", "pc"),
#     ("Mint", "pc"),
#     ("Parrot", "pc"),
#     ("Guaraní", "servidor"),
#     ("MongoDB", "servidor"),
#     ("Router 1", "router"),
#     ("Router 2", "router"),
#     ("Router 3", "router"),
#     ("Switch 1", "switch"),
#     ("Switch 2", "switch"),
#     ("Impresora", "impresora"),
# ]

# for nombre, tipo in equipos:
#     g.add_vertex(nombre, tipo)

# # Carga de aristas -> (peso, origen, destino)
# g.add_edge(17, "Switch 1", "Debian")
# g.add_edge(18, "Switch 1", "Ubuntu")
# g.add_edge(22, "Switch 1", "Impresora")
# g.add_edge(80, "Switch 1", "Mint")
# g.add_edge(29, "Switch 1", "Router 1")
# g.add_edge(37, "Router 1", "Router 2")
# g.add_edge(43, "Router 1", "Router 3")
# g.add_edge(25, "Router 2", "Red Hat")
# g.add_edge(9, "Router 2", "Guaraní")
# g.add_edge(50, "Router 2", "Router 3")
# g.add_edge(61, "Router 3", "Switch 2")
# g.add_edge(40, "Switch 2", "Manjaro")
# g.add_edge(12, "Switch 2", "Parrot")
# g.add_edge(5, "Switch 2", "MongoDB")
# g.add_edge(56, "Switch 2", "Arch")
# g.add_edge(3, "Switch 2", "Fedora")


# #barrido en profundidad 
# # Red Hat, Debian, Arch
# print("Barridos desde las notebooks")
# for nb in ["Red Hat", "Debian", "Arch"]:
#     print(f"Profundidad desde {nb}")
#     g.deep_show(nb)
#     print(f"Amplitud desde {nb}:")
#     g.amplitude_show(nb)


# # Manjaro, Red Hat, Fedora
# print("Camino más corto hasta Impresora")
# for origen in ["Manjaro", "Red Hat", "Fedora"]:
#     exist_path = g.exist_path(origen, "Impresora")
#     if exist_path:
#         paths = g.dijkstra(origen)
#         destination = "Impresora"
#         peso_total = None
#         camino_completo = []

#         while paths.size() > 0:
#             value = paths.pop()
#             if value[0] == destination:
#                 if peso_total is None:
#                     peso_total = value[1]
#                 camino_completo.append(value[0])
#                 destination = value[2]

#         camino_completo.reverse()
#         print(f"Desde {origen} el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}")


# # d. encontrar el árbol de expansión mínima
# print("Árbol de expansión mínima")
# min_tree = g.kruskal("Router 1")
# print(min_tree)

# peso_total = 0
# for edge in min_tree.split(";"):
#     origin, destination, weight = edge.split("-")
#     print(f"origin {origin} destination {destination}")
#     peso_total += int(weight)
# print(f"peso total: {peso_total}")


# # e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”
# print("PC más cercana a Guaraní")
# mejor_pc = None
# menor_peso = None
# mejor_camino = []

# for vertex in g:
#     if vertex.other_values == "pc":
#         exist_path = g.exist_path(vertex.value, "Guaraní")
#         if exist_path:
#             paths = g.dijkstra(vertex.value)
#             destination = "Guaraní"
#             peso_total = None
#             camino_completo = []

#             while paths.size() > 0:
#                 value = paths.pop()
#                 if value[0] == destination:
#                     if peso_total is None:
#                         peso_total = value[1]
#                     camino_completo.append(value[0])
#                     destination = value[2]

#             camino_completo.reverse()

#             if menor_peso is None or peso_total < menor_peso:
#                 menor_peso = peso_total
#                 mejor_pc = vertex.value
#                 mejor_camino = camino_completo

# print(f"Desde {mejor_pc} el camino mas corto es: {"-".join(mejor_camino)} con un costo de {menor_peso}")


# # f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”
# print("Computadora del Switch 1 más cercana a MongoDB")
# mejor_comp = None
# menor_peso_mongo = None
# mejor_camino_mongo = []

# pos_sw1 = g.search("Switch 1", "value")
# if pos_sw1 is not None:
#     for edge in g[pos_sw1].edges:
#         pos_vecino = g.search(edge.destination, "value")
#         vecino = g[pos_vecino]
#         if vecino.other_values in ["pc", "notebook"]:
#             exist_path = g.exist_path(vecino.value, "MongoDB")
#             if exist_path:
#                 paths = g.dijkstra(vecino.value)
#                 destination = "MongoDB"
#                 peso_total = None
#                 camino_completo = []

#                 while paths.size() > 0:
#                     value = paths.pop()
#                     if value[0] == destination:
#                         if peso_total is None:
#                             peso_total = value[1]
#                         camino_completo.append(value[0])
#                         destination = value[2]

#                 camino_completo.reverse()

#                 if menor_peso_mongo is None or peso_total < menor_peso_mongo:
#                     menor_peso_mongo = peso_total
#                     mejor_comp = vecino.value
#                     mejor_camino_mongo = camino_completo

# print(f"Desde {mejor_comp} el camino mas corto es: {"-".join(mejor_camino_mongo)} con un costo de {menor_peso_mongo}")


# # g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b
# print("Cambio de conexión de Impresora a Router 2 y barridos")
# g.delete_edge("Switch 1", "Impresora")
# g.add_edge(22, "Router 2", "Impresora")

# for nb in ["Red Hat", "Debian", "Arch"]:
#     print(f"\nProfundidad desde {nb}:")
#     g.deep_show(nb)
#     print(f"\nAmplitud desde {nb}:")
#     g.amplitude_show(nb)




# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

from graph import Graph

# Implementar sobre un grafo no dirigido
g = Graph(is_dir=False)

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
ambientes = [
    "cocina",
    "comedor",
    "cochera",
    "quincho",
    "baño 1",
    "baño 2",
    "habitación 1",
    "habitación 2",
    "sala de estar",
    "terraza",
    "patio",
]

for ambiente in ambientes:
    g.add_vertex(ambiente)

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;
# (Como el grafo es no dirigido, cada g.add_edge suma 1 arista a ambos extremos)
# Grado de cada vértice resultante:
# - comedor: 5 aristas (cocina, sala de estar, patio, baño 1, habitación 1)
# - patio: 5 aristas (comedor, quincho, cochera, terraza, baño 2)
# - cocina: 3 aristas (comedor, quincho, cochera)
# - cochera: 3 aristas (cocina, patio, sala de estar)
# - quincho: 3 aristas (cocina, patio, terraza)
# - baño 1: 3 aristas (comedor, habitación 1, habitación 2)
# - baño 2: 3 aristas (patio, habitación 2, terraza)
# - habitación 1: 3 aristas (comedor, baño 1, habitación 2)
# - habitación 2: 3 aristas (baño 1, habitación 1, baño 2)
# - sala de estar: 3 aristas (comedor, cochera, terraza)
# - terraza: 3 aristas (quincho, patio, baño 2, sala de estar -> 4 aristas)

g.add_edge(4, "cocina", "comedor")
g.add_edge(6, "cocina", "quincho")
g.add_edge(8, "cocina", "cochera")

g.add_edge(5, "comedor", "sala de estar")
g.add_edge(7, "comedor", "patio")
g.add_edge(3, "comedor", "baño 1")
g.add_edge(6, "comedor", "habitación 1")

g.add_edge(9, "cochera", "patio")
g.add_edge(7, "cochera", "sala de estar")

g.add_edge(5, "quincho", "patio")
g.add_edge(10, "quincho", "terraza")

g.add_edge(2, "baño 1", "habitación 1")
g.add_edge(4, "baño 1", "habitación 2")

g.add_edge(3, "habitación 1", "habitación 2")

g.add_edge(2, "habitación 2", "baño 2")

g.add_edge(8, "baño 2", "patio")
g.add_edge(6, "baño 2", "terraza")

g.add_edge(11, "sala de estar", "terraza")
g.add_edge(9, "patio", "terraza")


# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
print("Árbol de expansión mínima")
min_tree = g.kruskal("cocina")
print(min_tree)

peso_total = 0
for edge in min_tree.split(";"):
    origin, destination, weight = edge.split("-")
    print(f"origin {origin} destination {destination} {weight}")
    peso_total += int(weight)
print(f"Se necesitan {peso_total} metros de cable para conectar todos los ambientes.")


# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
print(" d. Camino más corto desde habitación 1 hasta sala de estar ")
exist_path = g.exist_path("habitación 1", "sala de estar")

if exist_path:
    paths = g.dijkstra("habitación 1")
    destination = "sala de estar"
    peso_total = None
    camino_completo = []

    while paths.size() > 0:
        value = paths.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]

    camino_completo.reverse()
    print(f"El camino mas corto es: {"-".join(camino_completo)} y se necesitan {peso_total} metros de cable de red.")