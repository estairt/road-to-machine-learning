
class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._idntificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(
                f'La region {region} no es valida en {self._pais}')


if __name__ == '__main__':
    casilla = CasillaDeVotacion(122, ['Santiago', 'Melipilla'])
    print(casilla.region)
    casilla.region = 'Santiago'
    print(casilla.region)
