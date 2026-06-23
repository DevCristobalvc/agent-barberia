# Cómo probar las tools del agente

Las tools son funciones Python puras decoradas con `@tool`. Se pueden invocar directamente sin el LLM usando `.invoke({...})`.

## Requisitos

- Supabase con datos cargados (`supabase_schema.sql`)
- Variables de entorno en `../api-barberia/.env`

## Ejecutar suite completa

```bash
# Desde agent-barberia/
../api-barberia/.venv/Scripts/pytest tests/test_tools.py -v
```

## Probar una tool específica

```python
# Script rápido en Python
import sys
sys.path.insert(0, "../api-barberia")

from app.tools.availability import get_availability

result = get_availability.invoke({
    "shop_id": "00000000-0000-0000-0000-000000000001",
    "service_duration": 30,
    "date_str": "2025-06-25"
})
print(result)
# → {"Carlos Mendoza": {"slots": ["09:00", "09:30", ...]}, ...}
```

## Probar el agente completo (sin WhatsApp)

```bash
../api-barberia/.venv/Scripts/python test_agent_local.py
```

Este script:
1. Carga el grafo LangGraph completo
2. Simula la memoria de conversación
3. Permite chatear desde la terminal como lo haría un cliente de WhatsApp

## Casos de prueba importantes

| Escenario | Tool esperada |
|---|---|
| "Quiero un corte" | `list_services` + `get_availability` |
| "Reserva para mañana a las 10" | `create_booking` |
| "Cancela mi cita" | `search_customer` + `cancel_booking` |
| "¿Cuánto cuesta el fade?" | `list_services` |
| "¿Qué barberos tienen?" | `list_barbers` |
| "Quiero con Carlos" | `get_availability` (con `barber_id`) |

## IDs de prueba (datos semilla)

```
shop_id:   00000000-0000-0000-0000-000000000001
barber_id: 10000000-0000-0000-0000-000000000001  (Carlos)
           10000000-0000-0000-0000-000000000002  (Miguel)
           10000000-0000-0000-0000-000000000003  (Roberto)
service_id: 20000000-0000-0000-0000-000000000001  (Corte Clásico, 30min)
```
