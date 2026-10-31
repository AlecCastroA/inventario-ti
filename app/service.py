from app.models import Equipo, TipoEquipo
from app.repository import EquipoRepository


class SerieDuplicadaError(Exception):
    """Ya existe un equipo con ese número de serie."""


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