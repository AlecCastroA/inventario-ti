from app.models import Equipo, TipoEquipo


class EquipoRepository:
    def __init__(self) -> None:
        self._equipos: dict[int, Equipo] = {}
        self._siguiente_id = 1

    def agregar(
        self, tipo: TipoEquipo, marca_modelo: str, numero_serie: str
    ) -> Equipo:
        equipo = Equipo(
            id=self._siguiente_id,
            tipo=tipo,
            marca_modelo=marca_modelo,
            numero_serie=numero_serie,
        )
        self._equipos[equipo.id] = equipo
        self._siguiente_id += 1
        return equipo

    def obtener(self, equipo_id: int) -> Equipo | None:
        return self._equipos.get(equipo_id)

    def obtener_por_serie(self, numero_serie: str) -> Equipo | None:
        for equipo in self._equipos.values():
            if equipo.numero_serie.lower() == numero_serie.lower():
                return equipo
        return None

    def listar(self) -> list[Equipo]:
        return list(self._equipos.values())