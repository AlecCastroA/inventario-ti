import pytest
from fastapi.testclient import TestClient

from app.main import app, get_service
from app.repository import EquipoRepository
from app.service import EquipoService


@pytest.fixture
def client():
    repositorio = EquipoRepository()
    app.dependency_overrides[get_service] = lambda: EquipoService(repositorio)
    yield TestClient(app)
    app.dependency_overrides.clear()


def _equipo(**cambios):
    datos = {
        "tipo": "laptop",
        "marca_modelo": "Lenovo ThinkPad T14",
        "numero_serie": "SN-001",
    }
    datos.update(cambios)
    return datos


def test_registrar_equipo_devuelve_201_y_estado_disponible(client):
    respuesta = client.post("/equipos", json=_equipo())
    assert respuesta.status_code == 201
    cuerpo = respuesta.json()
    assert cuerpo["id"] == 1
    assert cuerpo["estado"] == "disponible"
    assert cuerpo["asignado_a"] is None


def test_registrar_serie_duplicada_devuelve_409(client):
    client.post("/equipos", json=_equipo())
    respuesta = client.post("/equipos", json=_equipo(numero_serie="sn-001"))
    assert respuesta.status_code == 409


def test_registrar_con_serie_vacia_devuelve_422(client):
    respuesta = client.post("/equipos", json=_equipo(numero_serie="   "))
    assert respuesta.status_code == 422


def test_registrar_con_tipo_invalido_devuelve_422(client):
    respuesta = client.post("/equipos", json=_equipo(tipo="tostadora"))
    assert respuesta.status_code == 422