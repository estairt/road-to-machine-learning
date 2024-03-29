from borracho import BorrachoTradicional, BorrachoSaltarin
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho("Seba")
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def graficar(x, y):
    grafica = figure(title="Camino aleatorio ",
                     x_axis_label="pasos", y_axis_label="distancia recorrida")
    grafica.line(x, y, legend_label="distanica media")

    show(grafica)


def main(distancia_de_caminata, numero_de_intentos, tipo_de_borrado):
    distancias_media_por_caminata = []

    for pasos in distancia_de_caminata:
        distancias = simular_caminata(
            pasos, numero_de_intentos, tipo_de_borrado)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distanacia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borrado.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Distancia media {distancia_media}')
        print(f'Distancia maxima {distanacia_maxima}')
        print(f'Distancia minima {distancia_minima}')

    graficar(distancia_de_caminata, distancias_media_por_caminata)


if __name__ == "__main__":
    distancia_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancia_de_caminata, numero_de_intentos, BorrachoSaltarin)
