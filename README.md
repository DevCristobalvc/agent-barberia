# agent-barberia — Tests del agente

Suite de tests para las tools y el agente de [api-barberia](https://github.com/DevCristobalvc/api-barberia) en aislamiento, sin necesidad de levantar el servidor completo.

## Propósito

- Validar cada tool de forma independiente antes de integrar
- Simular conversaciones completas desde terminal
- Facilitar el desarrollo del agente sin depender del webhook de WhatsApp

## Prerequisitos

- Python 3.12+
- Supabase configurado con datos de prueba (ver [setup de api-barberia](https://github.com/DevCristobalvc/api-barberia/blob/main/docs/setup.md))
- `api-barberia` clonado en el directorio hermano

## Estructura esperada de directorios

```
barberia/
├── api-barberia/   ← Las tools importan desde aquí
└── agent-barberia/ ← Este repo
```

## Instalar dependencias

```bash
cd agent-barberia
# Usar el venv de api-barberia (comparten dependencias)
../api-barberia/.venv/Scripts/pip install pytest
```

## Correr tests

```bash
# Tests de todas las tools
pytest tests/test_tools.py -v

# Test específico
pytest tests/test_tools.py::TestAvailabilityTool -v
```

## Chat interactivo con el agente

Simula una conversación real sin WhatsApp:

```bash
../api-barberia/.venv/Scripts/python test_agent_local.py

# Ejemplo de conversación:
Tú: quiero un corte para mañana
SofIA: Claro ✂️ Tenemos disponible a Carlos (10:00, 11:30)...
```

## Documentación

- [Cómo probar las tools](docs/tools-testing.md)
- [Arquitectura del agente](https://github.com/DevCristobalvc/api-barberia/blob/main/docs/architecture.md)

## Repos relacionados

- **Backend + Agente**: [api-barberia](https://github.com/DevCristobalvc/api-barberia)
- **Frontend + Dashboard**: [BarberIA](https://github.com/DevCristobalvc/BarberIA)
