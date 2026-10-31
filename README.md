# Inventario TI

API REST para controlar el inventario de equipos de TI de una oficina pequeña: registrar equipos, consultar su estado, asignarlos a usuarios y darlos de baja.

> Proyecto individual del curso de Ingeniería de Software. Estado: en desarrollo.

## Funcionalidades previstas

- Registrar un equipo (tipo, marca/modelo, número de serie único, estado).
- Listar y filtrar equipos por tipo o estado.
- Consultar el detalle de un equipo por ID.
- Asignar un equipo a un usuario.
- Dar de baja un equipo.

## Tecnología

Python, FastAPI, pytest, ruff, GitHub Actions y Docker.

## Flujo de trabajo

- Ramas: `main` (estable), `develop` (integración) y `feature/*` (funcionalidades).
- Commits siguiendo Conventional Commits.