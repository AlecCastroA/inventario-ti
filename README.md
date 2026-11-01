# Inventario TI

![CI](https://github.com/AlecCastroA/inventario-ti/actions/workflows/ci.yml/badge.svg)

API REST para controlar el inventario de equipos de TI de una oficina pequeña: registrar equipos, consultar su estado, asignarlos a usuarios y darlos de baja.

> Proyecto individual del curso de Ingeniería de Software.

## Funcionalidades

- Registrar un equipo (tipo, marca/modelo, número de serie único).
- Listar equipos y filtrar por tipo o estado.
- Consultar el detalle de un equipo por ID.
- Asignar un equipo a un usuario.
- Dar de baja un equipo.
- Consultar el estado de la aplicación y el entorno activo.

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/equipos` | Registra un equipo |
| GET | `/equipos` | Lista equipos (filtros opcionales `tipo` y `estado`) |
| GET | `/equipos/{id}` | Detalle de un equipo |
| POST | `/equipos/{id}/asignar` | Asigna el equipo a un usuario |
| POST | `/equipos/{id}/baja` | Da de baja el equipo |
| GET | `/salud` | Estado de la API y entorno activo |

La documentación interactiva está en `/docs` cuando la API está en ejecución.

## Reglas de negocio

- El número de serie es único, sin distinguir mayúsculas de minúsculas.
- Solo se puede asignar un equipo en estado `disponible`.
- Un equipo asignado o disponible puede darse de baja; al darse de baja se libera al usuario.
- Un equipo dado de baja no puede asignarse ni darse de baja otra vez.

## Tecnología

Python 3.12, FastAPI, pytest, ruff y GitHub Actions. El almacenamiento es en memoria; SQLite queda como mejora futura.

## Requisitos

- Python 3.12 o superior
- Git (en Windows, Git Bash)

## Instalación

```bash
git clone https://github.com/AlecCastroA/inventario-ti.git
cd inventario-ti
python -m venv .venv
source .venv/Scripts/activate   # Git Bash en Windows; en Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

Con el script, que prepara el entorno virtual y las dependencias por ti:

```bash
bash scripts/ejecutar.sh desarrollo    # con recarga automática
bash scripts/ejecutar.sh produccion    # sin recarga
```

O manualmente, con el entorno virtual activo:

```bash
uvicorn app.main:app --reload
```

La API queda en `http://127.0.0.1:8000`.

## Pruebas y verificación

```bash
pytest
ruff check .
```

Estas mismas verificaciones se ejecutan automáticamente en GitHub Actions con cada push a `develop` o `main`.

## Estructura del proyecto

```
app/          código de la API (rutas, servicio, repositorio, modelos, configuración)
tests/        pruebas automáticas
docs/         diagramas y documentación técnica
scripts/      script de ejecución por entorno
.github/      workflow de integración continua
```

## Documentación técnica

- [Arquitectura y diagramas](docs/arquitectura.md)
- [Entornos y despliegue](docs/despliegue.md)

## Flujo de trabajo

- Ramas: `main` (estable), `develop` (integración) y `feature/*` (funcionalidades). Todo cambio entra a `develop` mediante Pull Request.
- Commits siguiendo [Conventional Commits](https://www.conventionalcommits.org/es/).

## Limitaciones conocidas

- Los datos se guardan en memoria y se pierden al reiniciar la API.
- No hay autenticación de usuarios.
- No hay despliegue público ni contenerización con Docker.