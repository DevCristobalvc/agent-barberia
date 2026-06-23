"""
Script para probar el agente localmente sin WhatsApp.
Simula una conversación completa desde la terminal.
"""
import asyncio
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "api-barberia"))

SHOP_ID = "00000000-0000-0000-0000-000000000001"
PHONE = "+57 300 999 8888"


async def chat():
    from app.services.agent_service import agent_service

    print("=" * 50)
    print("BarberIA — Test de agente local")
    print(f"Shop: {SHOP_ID} | Teléfono simulado: {PHONE}")
    print("Escribe 'exit' para salir")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nTú: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSaliendo...")
            break

        if user_input.lower() in ("exit", "quit", "salir"):
            break
        if not user_input:
            continue

        print("SofIA: ", end="", flush=True)
        response = await agent_service.process_message(SHOP_ID, PHONE, user_input)
        print(response)


if __name__ == "__main__":
    asyncio.run(chat())
