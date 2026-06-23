"""
Tests standalone de las tools del agente.
Cada tool se puede probar sin LLM — solo con datos de la BD.
Requiere un Supabase con datos de prueba (ver supabase_schema.sql).
"""
import pytest
import sys
import os

# Apunta al api-barberia para importar las tools
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "api-barberia"))

SHOP_ID = "00000000-0000-0000-0000-000000000001"
TEST_PHONE = "+57 999 000 1111"


class TestAvailabilityTool:
    def test_get_availability_returns_dict(self):
        from app.tools.availability import get_availability
        from datetime import date, timedelta

        tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        result = get_availability.invoke({
            "shop_id": SHOP_ID,
            "service_duration": 30,
            "date_str": tomorrow,
        })
        assert isinstance(result, dict)

    def test_get_availability_with_barber(self):
        from app.tools.availability import get_availability
        from datetime import date, timedelta

        tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        result = get_availability.invoke({
            "shop_id": SHOP_ID,
            "service_duration": 30,
            "date_str": tomorrow,
            "barber_id": "10000000-0000-0000-0000-000000000001",
        })
        assert isinstance(result, dict)


class TestCustomerTools:
    def test_search_nonexistent_customer(self):
        from app.tools.customers import search_customer
        result = search_customer.invoke({"shop_id": SHOP_ID, "phone": "+57 000 000 0000"})
        assert result is None

    def test_create_and_search_customer(self):
        from app.tools.customers import create_customer, search_customer
        created = create_customer.invoke({
            "shop_id": SHOP_ID,
            "name": "Test Cliente",
            "phone": TEST_PHONE,
        })
        assert created["name"] == "Test Cliente"

        found = search_customer.invoke({"shop_id": SHOP_ID, "phone": TEST_PHONE})
        assert found is not None
        assert found["phone"] == TEST_PHONE


class TestShopInfoTools:
    def test_list_services(self):
        from app.tools.shop_info import list_services
        result = list_services.invoke({"shop_id": SHOP_ID})
        assert isinstance(result, list)
        assert len(result) > 0

    def test_list_barbers(self):
        from app.tools.shop_info import list_barbers
        result = list_barbers.invoke({"shop_id": SHOP_ID})
        assert isinstance(result, list)
        assert len(result) > 0

    def test_get_shop_information(self):
        from app.tools.shop_info import get_shop_information
        result = get_shop_information.invoke({"shop_id": SHOP_ID})
        assert result.get("name") == "BarberIA Demo"


class TestBookingTools:
    def test_list_today(self):
        from app.tools.bookings import list_today
        result = list_today.invoke({"shop_id": SHOP_ID})
        assert isinstance(result, list)
