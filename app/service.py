from app.models import Equipo, EstadoEquipo, TipoEquipo
from app.repository import EquipoRepository


class SerieDuplicadaError(Exception):
    """Ya existe un equipo con ese número de serie."""

class EquipoNoEncontradoError(Exception):
    """No existe un equipo con ese ID."""

class EquipoNoDisponibleError(Exception):
    """El equipo no está disponible para asignarse."""

class EquipoService:
    """Reglas de negocio del inventario."""

    def __init__(self, repositorio: EquipoRepository) -> None:
        self._repo = repositorio

    def registrar(
        self, tipo: TipoEquipo, marca_modelo: str, numero_serie: str
    ) -> Equipo:
        if self._repo.obtener_por_serie(numero_serie) is not None:
            raise SerieDuplicadaError(numero_serie)
        return self._repo.agregar(tipo, marca_modelo, numero_serie)

    def listar(
        self,
        tipo: TipoEquipo | None = None,
        estado: EstadoEquipo | None = None,
    ) -> list[Equipo]:
        equipos = self._repo.listar()
        if tipo is not None:
            equipos = [e for e in equipos if e.tipo == tipo]
        if estado is not None:
            equipos = [e for e in equipos if e.estado == estado]
        return equipos

    def obtener(self, equipo_id: int) -> Equipo:
        equipo = self._repo.obtener(equipo_id)
        if equipo is None:
            raise EquipoNoEncontradoError(equipo_id)
        return equipo

    def asignar(self, equipo_id: int, usuario: str) -> Equipo:
        equipo = self.obtener(equipo_id)
        if equipo.estado != EstadoEquipo.DISPONIBLE:
            raise EquipoNoDisponibleError(equipo.estado.value)
        equipo.estado = EstadoEquipo.ASIGNADO
        equipo.asignado_a = usuario
        return self._repo.actualizar(equipo)