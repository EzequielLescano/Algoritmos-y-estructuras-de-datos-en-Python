from list import list
# Dada una lista de superhéroes de comics, de los cuales se conoce su
# nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, 
# implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:

# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

# class Superheroe:
#     def __init__(self, name, anio, casa, bio):
#         self.name = name
#         self.anio = anio
#         self.casa = casa
#         self.bio = bio

#     def __str__(self):
#         return f"[{self.casa}] {self.name} ({self.anio}) - {self.bio}"

# # Funciones de criterio para ordenar o buscar en la List customizada
# def by_name(item):
#     return item.name

# def by_casa(item):
#     return item.casa

# def by_anio(item):
#     return item.anio

# lista_superheroes=Superheroe()
# # a. eliminar el nodo que contiene la información de Linterna Verde;
# lista_superheroes.delete_value("Linterna Verde", "name")
# # b. mostrar el año de aparición de Wolverine;
# indice = lista_superheroes.search("Wolverine", "name")
# if indice is not None:
#     print(f"Año de aparición de Wolverine: {lista_superheroes[indice].anio}")
# else:
#     print("Wolverine no se encuentra en la lista.")

# # c. cambiar la casa de Dr. Strange a Marvel;
# indice = lista_superheroes.search("Dr. Strange", "name")
# if indice is not None:
#     lista_superheroes[indice].casa = "Marvel"
#     print("Se ha actualizado la casa de Dr. Strange a Marvel.")
# else:
#     print("Dr. Strange no se encuentra en la lista.")
    
# # d. mostrar el nombre de aquellos superhéroes que en su biografía mencionan la palabra “traje” o “armadura”;
# print("Superhéroes con 'traje' o 'armadura' en su biografía:")
# lista_superheroes.filter_contain_on_bio(["traje", "armadura"])

# # e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
# print("Superhéroes con aparición anterior a 1963:")
# for heroe in lista_superheroes:
#     if heroe.anio < 1963:
#         print(f"- {heroe.name} ({heroe.casa})")

# # f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# for nombre in ["Capitana Marvel", "Mujer Maravilla"]:
#     indice = lista_superheroes.search(nombre, "name")
#     if indice is not None:
#         print(f"Casa de {nombre}: {lista_superheroes[indice].casa}")
#     else:
#         print(f"{nombre} no se encuentra en la lista.")
        
# # g. mostrar toda la información de Flash y Star-Lord;
# for nombre in ["Flash", "Star-Lord"]:
#     indice = lista_superheroes.search(nombre, "name")
#     if indice is not None:
#         print(lista_superheroes[indice])
#     else:
#         print(f"{nombre} no se encuentra en la lista.")
        
# # h. listar los superhéroes que comienzan con la letra B, M y S;
# for letra in ["B", "M", "S"]:
#     print(f"\nSuperhéroes que comienzan con '{letra}':")
#     lista_superheroes.filter_start_with(letra)

# # i. determinar cuántos superhéroes hay de cada casa de comic;
# conteo_casas = {}
# for heroe in lista_superheroes:
#     casa = heroe.casa
#     conteo_casas[casa] = conteo_casas.get(casa, 0) + 1

# print("Cantidad de superhéroes por casa:")
# for casa, cantidad in conteo_casas.items():
#     print(f"- {casa}: {cantidad}")
    
#_---------------------------#

# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver

# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;

# [115]

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;


# class Pokemon:
#     def __init__(self, nombre, nivel, tipo, subtipo):
#         self.nombre = nombre
#         self.nivel = nivel
#         self.tipo = tipo
#         self.subtipo = subtipo

#     def __str__(self):
#         return f"Pokémon: {self.nombre} | Nivel: {self.nivel} | Tipo: {self.tipo}/{self.subtipo}"

# class Entrenador:
#     def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
#         self.nombre = nombre
#         self.torneos_ganados = torneos_ganados
#         self.batallas_perdidas = batallas_perdidas
#         self.batallas_ganadas = batallas_ganadas
#         self.pokemons = List() # Lista interna de Pokémons (lista de listas)

#     def __str__(self):
#         return f"Entrenador: {self.nombre} | Torneos: {self.torneos_ganados} | Ganadas: {self.batallas_ganadas} | Perdidas: {self.batallas_perdidas}"
# # a. Obtener la cantidad de Pokémons de un determinado entrenador;
# def cantidad_pokemons(entrenador):
#     return entrenador.pokemons.size()


# # b. Listar los entrenadores que hayan ganado más de tres torneos;
# def entrenadores_mas_de_tres_torneos(lista_entrenadores):
#     print("--- Entrenadores con más de 3 torneos ganados ---")
#     for entrenador in lista_entrenadores:
#         if entrenador.torneos_ganados > 3:
#             print(f"- {entrenador.nombre} ({entrenador.torneos_ganados} torneos)")


# # c. El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# def pokemon_mayor_nivel_campeon(lista_entrenadores):
#     if lista_entrenadores.size() == 0:
#         return None
    
#     # Buscamos al entrenador con más torneos ganados
#     campeon = lista_entrenadores[0]
#     for entrenador in lista_entrenadores:
#         if entrenador.torneos_ganados > campeon.torneos_ganados:
#             campeon = entrenador
            
#     print(f"\nEntrenador con más torneos ganados: {campeon.nombre} ({campeon.torneos_ganados} torneos)")
    
#     if campeon.pokemons.size() == 0:
#         print("El entrenador campeon no tiene Pokémons.")
#         return
        
#     # Buscamos el Pokémon de mayor nivel de ese entrenador
#     mayor_nivel = campeon.pokemons[0]
#     for p in campeon.pokemons:
#         if p.nivel > mayor_nivel.nivel:
#             mayor_nivel = p
            
#     print(f"Pokémon de mayor nivel: {mayor_nivel}")


# # d. Mostrar todos los datos de un entrenador y sus Pokémons;
# def mostrar_entrenador_y_pokemons(entrenador):
#     print("\n--------------------------------------------------")
#     print(entrenador)
#     print("Lista de Pokémons:")
#     if entrenador.pokemons.size() == 0:
#         print("  (No tiene Pokémons registrados)")
#     for p in entrenador.pokemons:
#         print(f"  -> {p}")
#     print("--------------------------------------------------")


# # e. Mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# def entrenadores_alto_winrate(lista_entrenadores):
#     print("\n--- Entrenadores con más del 79% de batallas ganadas ---")
#     for entrenador in lista_entrenadores:
#         total_batallas = entrenador.batallas_ganadas + entrenador.batallas_perdidas
#         if total_batallas > 0:
#             porcentaje = (entrenador.batallas_ganadas / total_batallas) * 100
#             if porcentaje > 79:
#                 print(f"- {entrenador.nombre} ({porcentaje:.2f}% de victorias)")


# # f. Los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
# def entrenadores_tipos_especificos(lista_entrenadores):
#     print("\n--- Entrenadores con Fuego y Planta, o Agua/Volador ---")
#     for entrenador in lista_entrenadores:
#         tiene_fuego = False
#         tiene_planta = False
#         tiene_agua_volador = False
        
#         for p in entrenador.pokemons:
#             tipo = p.tipo.lower()
#             subtipo = p.subtipo.lower()
            
#             if tipo == "fuego" or subtipo == "fuego":
#                 tiene_fuego = True
#             if tipo == "planta" or subtipo == "planta":
#                 tiene_planta = True
#             if (tipo == "agua" and subtipo == "volador") or (tipo == "volador" and subtipo == "agua"):
#                 tiene_agua_volador = True
                
#         if (tiene_fuego and tiene_planta) or tiene_agua_volador:
#             print(f"- {entrenador.nombre}")


# # g. El promedio de nivel de los Pokémons de un determinado entrenador;
# def promedio_nivel_pokemons(entrenador):
#     cantidad = entrenador.pokemons.size()
#     if cantidad == 0:
#         return 0
#     suma_niveles = sum(p.nivel for p in entrenador.pokemons)
#     return suma_niveles / cantidad


# # h. Determinar cuántos entrenadores tienen a un determinado Pokémon;
# def entrenadores_con_pokemon(lista_entrenadores, nombre_pokemon):
#     contador = 0
#     for entrenador in lista_entrenadores:
#         for p in entrenador.pokemons:
#             if p.nombre.lower() == nombre_pokemon.lower():
#                 contador += 1
#                 break # Rompe para contar una sola vez por entrenador
#     return contador


# # i. Mostrar los entrenadores que tienen Pokémons repetidos;
# def entrenadores_con_pokemons_repetidos(lista_entrenadores):
#     print("\n--- Entrenadores con Pokémons repetidos ---")
#     for entrenador in lista_entrenadores:
#         nombres_pokemons = [p.nombre.lower() for p in entrenador.pokemons]
#         # Si la cantidad de nombres es distinta al set de nombres, hay repetidos
#         if len(nombres_pokemons) != len(set(nombres_pokemons)):
#             print(f"- {entrenador.nombre}")


# # j. Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# def entrenadores_con_pokemon_especifico(lista_entrenadores):
#     buscados = {"tyrantrum", "terrakion", "wingull"}
#     print("\n--- Entrenadores con Tyrantrum, Terrakion o Wingull ---")
#     for entrenador in lista_entrenadores:
#         encontrado = False
#         for p in entrenador.pokemons:
#             if p.nombre.lower() in buscados:
#                 encontrado = True
#                 break
#         if encontrado:
#             print(f"- {entrenador.nombre}")


# # k. Determinar si un entrenador “X” tiene al Pokémon “Y” (ingresados por teclado) y mostrar los datos de ambos;
# def verificar_entrenador_y_pokemon(lista_entrenadores):
#     print("\n--- Búsqueda de Entrenador y Pokémon ---")
#     nombre_ingresado = input("Ingrese el nombre del entrenador: ")
#     pokemon_ingresado = input("Ingrese el nombre del Pokémon: ")
    
#     entrenador_encontrado = None
#     pokemon_encontrado = None
    
#     for entrenador in lista_entrenadores:
#         if entrenador.nombre.lower() == nombre_ingresado.lower():
#             entrenador_encontrado = entrenador
#             for p in entrenador.pokemons:
#                 if p.nombre.lower() == pokemon_ingresado.lower():
#                     pokemon_encontrado = p
#                     break
#             break
            
#     if entrenador_encontrado and pokemon_encontrado:
#         print("\n¡Coincidencia encontrada!")
#         print(entrenador_encontrado)
#         print(pokemon_encontrado)
#     else:
#         print("\nEl entrenador no existe o no posee el Pokémon indicado.")