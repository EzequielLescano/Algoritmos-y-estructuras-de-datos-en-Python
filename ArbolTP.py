# # 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# # se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# # a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# # leano que indica si es un héroe o un villano, True y False respectivamente;

# # b. listar los villanos ordenados alfabéticamente;
# # c. mostrar todos los superhéroes que empiezan con C;
# # d. determinar cuántos superhéroes hay el árbol;
# # e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# # encontrarlo en el árbol y modificar su nombre;
# # f. listar los superhéroes ordenados de manera descendente;
# # g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# # los villanos, luego resolver las siguiente tareas:
# # I. determinar cuántos nodos tiene cada árbol;
# # II. realizar un barrido ordenado alfabéticamente de cada árbol.

# from tree import BinaryTree


# arbolConTodo = BinaryTree()

# personajes = [
#     ("Iron Man", True),
#     ("Thanos", False),
#     ("Captain America", True),
#     ("Loki", False),
#     ("Doctor Stranje", True),  # Stranje
#     ("Thor", True),
#     ("Ultron", False),
#     ("Captain Marvel", True),
#     ("Red Skull", False),
#     ("Hulk", True),
#     ("Hela", False),
#     ("Black Widow", True),
#     ("Cyclops", True),
#     ("Green Goblin", False),
#     ("Spider-Man", True),
#     ("Mysterio", False),
#     ("Clint Barton", True),
#     ("Winter Soldier", False),
# ]

# # a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# # leano que indica si es un héroe o un villano, True y False respectivamente;
# for nombre, quees in personajes:
#     arbolConTodo.insert_node(nombre, quees)
#     def mostrar_todo(root):
#         if root is not None:
#             mostrar_todo(root.left)
#             print(f"Nombre: {root.value} | Es héroe: {root.other_values}")
#             mostrar_todo(root.right)


# # b. listar los villanos ordenados alfabéticamente;
# def listaVillano(root):
#     if root is not None:
#         listaVillano(root.left)
#         if not root.other_values:
#             print(root.value)
#         listaVillano(root.right)


# # c. mostrar todos los superhéroes que empiezan con C;
# def heroeConC(root):
#     if root is not None:
#         heroeConC(root.left)
#         if (root.other_values == True) and root.value.startswith("C"):
#             print(root.value)
#         heroeConC(root.right)


# # d. determinar cuántos superhéroes hay en el árbol;
# def contar_heroes(root):
#     if root is None:
#         return 0
#     izquierda = contar_heroes(root.left)
#     actual = 1 if root.other_values else 0
#     derecha = contar_heroes(root.right)
#     return izquierda + actual + derecha


# # e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# # encontrarlo en el árbol y modificar su nombre;
# def buscar_proximidad(root, texto, encontrados):
#     if root is not None:
#         buscar_proximidad(root.left, texto, encontrados)
#         if texto.lower() in root.value.lower():
#             encontrados.append(root)
#         buscar_proximidad(root.right, texto, encontrados)


# def corregir_nombre(arbol, nombre_viejo, nombre_nuevo):
#     nuevo_arbol = BinaryTree()

#     def _reconstruir(root):
#         if root is not None:
#             _reconstruir(root.left)
#             if root.value == nombre_viejo:
#                 nuevo_arbol.insert_node(nombre_nuevo, root.other_values)
#             else:
#                 nuevo_arbol.insert_node(root.value, root.other_values)
#             _reconstruir(root.right)

#     _reconstruir(arbol.root)
#     return nuevo_arbol


# # f. listar los superhéroes ordenados de manera descendente;
# def listar_heroes_descendente(root):
#     if root is not None:
#         listar_heroes_descendente(root.right)
#         if root.other_values:
#             print(root.value)
#         listar_heroes_descendente(root.left)


# # g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# # los villanos, luego resolver las siguientes tareas:
# def generar_bosque(root, arbol_heroes, arbol_villanos):
#     if root is not None:
#         generar_bosque(root.left, arbol_heroes, arbol_villanos)
#         if root.other_values:
#             arbol_heroes.insert_node(root.value, root.other_values)
#         else:
#             arbol_villanos.insert_node(root.value, root.other_values)
#         generar_bosque(root.right, arbol_heroes, arbol_villanos)


# # g.I. determinar cuántos nodos tiene cada árbol;
# def contar_nodos(root):
#     if root is None:
#         return 0
#     return 1 + contar_nodos(root.left) + contar_nodos(root.right)


# # g.II. realizar un barrido ordenado alfabéticamente de cada árbol.
# def barrido_alfabetico(root):
#     if root is not None:
#         barrido_alfabetico(root.left)
#         print(root.value)
#         barrido_alfabetico(root.right)


# print("Muestra todo")
# mostrar_todo(arbolConTodo.root)

# print("Villano por alfabeto")
# listaVillano(arbolConTodo.root)

# print("heroes iniciado en C")
# heroeConC(arbolConTodo.root)

# print(f"Cantidad de superhéroes: {contar_heroes(arbolConTodo.root)}")

# print("Busqueda por proximidad")
# similares = []
# buscar_proximidad(arbolConTodo.root, "Stran", similares)
# for nodo in similares:
#     print(f"Encontrado: {nodo.value}")
#     arbolConTodo = corregir_nombre(arbolConTodo, nodo.value, "Doctor Strange")
#     print("Corregido a: Doctor Strange")

# print("Superhéroes ordenados de manera descendente")
# listar_heroes_descendente(arbolConTodo.root)

# print("Bosque de Héroes y Villanos")
# arbol_heroes = BinaryTree()
# arbol_villanos = BinaryTree()
# generar_bosque(arbolConTodo.root, arbol_heroes, arbol_villanos)

# print(f"Nodos en árbol de héroes: {contar_nodos(arbol_heroes.root)}")
# print(f"Nodos en árbol de villanos: {contar_nodos(arbol_villanos.root)}")

# print("Barrido alfabético de Héroes:")
# barrido_alfabetico(arbol_heroes.root)

# print("Barrido alfabético de Villanos:")
# barrido_alfabetico(arbol_villanos.root)


# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# [169]
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

from tree import BinaryTree

arbol_criaturas = BinaryTree()

datos_criaturas = [
    ("Ceto", None),
    ("Tifón", "Zeus"),
    ("Equidna", "Argos Panoptes"),
    ("Dino", None),
    ("Pefredo", None),
    ("Enio", None),
    ("Escila", None),
    ("Caribdis", None),
    ("Euríale", None),
    ("Esteno", None),
    ("Medusa", "Perseo"),
    ("Ladón", "Heracles"),
    ("Águila del Cáucaso", None),
    ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"),
    ("León de Nemea", "Heracles"),
    ("Esfinge", "Edipo"),
    ("Dragón de la Cólquida", None),
    ("Cerbero", None),
    ("Cerda de Cromión", "Teseo"),
    ("Ortro", "Heracles"),
    ("Toro de Creta", "Teseo"),
    ("Jabalí de Calidón", "Atalanta"),
    ("Carcinos", None),
    ("Gerión", "Heracles"),
    ("Cloto", None),
    ("Láquesis", None),
    ("Átropos", None),
    ("Minotauro de Creta", "Teseo"),
    ("Harpías", None),
    ("Argos Panoptes", "Hermes"),
    ("Aves del Estínfalo", None),
    ("Talos", "Medea"),
    ("Sirenas", None),
    ("Pitón", "Apolo"),
    ("Cierva de Cerinea", None),
    ("Basilisco", None),
    ("Jabalí de Erimanto", None),
]

for criatura, derrotador in datos_criaturas:
    info = {
        "derrotado_por": derrotador,
        "descripcion": "Descripción Genérica :D",
        "capturada": None,
    }
    arbol_criaturas.insert_node(criatura, info)


# a. listado inorden de las criaturas y quienes la derrotaron;
def listado_inorden(root):
    if root is not None:
        listado_inorden(root.left)
        derrotador = root.other_values["derrotado_por"] or None
        print(f" {root.value} | Derrotada por: {derrotador}")
        listado_inorden(root.right)


# b. se debe permitir cargar una breve descripción sobre cada criatura;
def cargar_descripcion(arbol: BinaryTree, criatura: str, descripcion: str):
    nodo = arbol.search(criatura)
    if nodo is not None:
        nodo.other_values["descripcion"] = descripcion
    else:
        print(f"No se encontró: {criatura}")


# c. mostrar toda la información de la criatura Talos;
def mostrar_info_criatura(arbol: BinaryTree, criatura: str):
    nodo = arbol.search(criatura)
    if nodo is not None:
        print(f"Criatura: {nodo.value}")
        print(f"  Derrotada por: {nodo.other_values["derrotado_por"] or None}")
        print(f"  Capturada por: {nodo.other_values["capturada"] or None}")
        print(f"  Descripción: {nodo.other_values["descripcion"]}")
    else:
        print(f"No se encontró a {criatura}")


# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
def top_3_derrotadores(root):
    conteo = {}

    def contar(nodo):
        if nodo is not None:
            contar(nodo.left)
            derrotador = nodo.other_values["derrotado_por"]
            if derrotador is not None:
                if derrotador in conteo:
                    conteo[derrotador] += 1
                else:
                    conteo[derrotador] = 1
            contar(nodo.right)

    contar(root)


    for puesto in range(1, 4):
        if len(conteo) == 0:
            return

        mayor_heroe = None
        mayor_cantidad = -1

        for heroe in conteo:
            if conteo[heroe] > mayor_cantidad:
                mayor_cantidad = conteo[heroe]
                mayor_heroe = heroe

        print(f"{puesto}. {mayor_heroe}: {mayor_cantidad} criaturas")
        del conteo[mayor_heroe]  # Lo sacamos del diccionario para buscar el siguiente mayor

# e. listar las criaturas derrotadas por Heracles;
def listar_derrotadas_por(root, heroe: str):
    if root is not None:
        listar_derrotadas_por(root.left, heroe)
        if root.other_values["derrotado_por"] == heroe:
            print(f"- {root.value}")
        listar_derrotadas_por(root.right, heroe)


# f. listar las criaturas que no han sido derrotadas;
def listar_no_derrotadas(root):
    if root is not None:
        listar_no_derrotadas(root.left)
        if root.other_values["derrotado_por"] is None:
            print(f"- {root.value}")
        listar_no_derrotadas(root.right)


# h. modificar nodos indicando quién las capturó;
def registrar_captura(arbol: BinaryTree, criatura: str, captor: str):
    nodo = arbol.search(criatura)
    if nodo is not None:
        nodo.other_values["capturada"] = captor
    else:
        print(f"No se encontró a {criatura} para registrar captura")


# i. se debe permitir búsquedas por coincidencia;
def buscar_por_coincidencia(root, texto: str):
    if root is not None:
        buscar_por_coincidencia(root.left, texto)
        if texto.lower() in root.value.lower():
            print(f"- {root.value} (Derrotada por: {root.other_values["derrotado_por"] or "Nadie"})")
        buscar_por_coincidencia(root.right, texto)


# l. modificar el nombre de una criatura manteniendo el orden del árbol;
def renombrar_criatura(arbol: BinaryTree, nombre_viejo: str, nombre_nuevo: str):
    nodo = arbol.search(nombre_viejo)
    if nodo is not None:
        datos_guardados = nodo.other_values
        arbol.delete_node(nombre_viejo)
        arbol.insert_node(nombre_nuevo, datos_guardados)
    else:
        print(f"No se encontró a {nombre_viejo}")


# n. muestre las criaturas capturadas por Heracles.
def listar_capturadas_por(root, captor: str):
    if root is not None:
        listar_capturadas_por(root.left, captor)
        if root.other_values["capturada"] == captor:
            print(f"- {root.value}")
        listar_capturadas_por(root.right, captor)


print("Listado inorden de criaturas y quién las derrotó")
listado_inorden(arbol_criaturas.root)

cargar_descripcion(arbol_criaturas, "Talos", "infor de prueba 1")
cargar_descripcion(arbol_criaturas, "Cerbero", "infor de prueba 2")
cargar_descripcion(arbol_criaturas, "Medusa", "info de prueba 3")

print("Información completa de Talos")
mostrar_info_criatura(arbol_criaturas, "Talos")

print("Top 3 héroes/dioses con más criaturas derrotadas")
top_3_derrotadores(arbol_criaturas.root)

print("e. Criaturas derrotadas por Heracles")
listar_derrotadas_por(arbol_criaturas.root, "Heracles")

print("Criaturas que no han sido derrotadas")
listar_no_derrotadas(arbol_criaturas.root)

for criatura in ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]:
    registrar_captura(arbol_criaturas, criatura, "Heracles")

print("Búsqueda por coincidencia: Creta")
buscar_por_coincidencia(arbol_criaturas.root, "Creta")

arbol_criaturas.delete_node("Basilisco")
arbol_criaturas.delete_node("Sirenas")
print("Basilisco y Sirenas eliminados del árbol")

nodo_aves = arbol_criaturas.search("Aves del Estínfalo")
if nodo_aves is not None:
    nodo_aves.other_values["derrotado_por"] = "Heracles"
    nodo_aves.other_values["descripcion"] = "descripción para Aves"
print("Aves del Estinfalo actualizado")

renombrar_criatura(arbol_criaturas, "Ladón", "Dragón Ladón")

print("Listado por nivel del árbol")
arbol_criaturas.by_level()

print("Criaturas capturadas por Heracles")
listar_capturadas_por(arbol_criaturas.root, "Heracles")