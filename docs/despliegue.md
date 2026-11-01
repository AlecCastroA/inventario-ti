# Gestión de entornos y despliegue

## Entornos

| Aspecto | Desarrollo | Prueba | Producción |
|---|---|---|---|
| Dónde se ejecuta | Equipo del desarrollador | Runner de GitHub Actions | Equipo o servidor destino (despliegue local) |
| Qué se ejecuta | `bash scripts/ejecutar.sh desarrollo` (con recarga automática) | `ruff`, `pytest` y validación del script en el pipeline | `bash scripts/ejecutar.sh produccion` (sin recarga) |
| Quién tiene acceso | El desarrollador | El pipeline y quien tenga acceso al repositorio | El técnico de soporte y el supervisor de TI |
| Valor de `APP_ENV` | `desarrollo` (por defecto) | `prueba` | `produccion` |
| Datos | En memoria, descartables | En memoria, nuevos en cada prueba | En memoria; se pierden al reiniciar (limitación conocida) |

La configuración que cambia entre entornos es `APP_ENV`, la recarga automática (solo en desarrollo), el punto de ejecución y la interfaz de red en la que escucha la API. El código es el mismo en los tres.

## Despliegue: guía reproducible

Requisitos: Python 3.12 o superior y Git. En Windows, usar Git Bash.

```bash
git clone https://github.com/AlecCastroA/inventario-ti.git
cd inventario-ti
bash scripts/ejecutar.sh produccion
```

El script crea el entorno virtual si no existe, instala las dependencias, define `APP_ENV` y arranca la API.

## Verificación

- `http://127.0.0.1:8000/salud` debe responder `{"estado":"ok","entorno":"produccion"}`.
- `http://127.0.0.1:8000/docs` muestra la documentación interactiva.

## Ejecución en desarrollo

```bash
bash scripts/ejecutar.sh desarrollo
```

Con recarga automática: `/salud` responde `"entorno":"desarrollo"`.

## Alcance del despliegue

El despliegue es local, mediante script. No hay hosting público ni base de datos persistente; ambos, junto con la contenerización con Docker, quedan como mejoras futuras.