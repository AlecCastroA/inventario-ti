import os


def obtener_entorno() -> str:
    """Devuelve el entorno activo: desarrollo, prueba o produccion."""
    return os.getenv("APP_ENV", "desarrollo")