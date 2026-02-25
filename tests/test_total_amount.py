# pytest fixture example
import pytest

@pytest.fixture
def sample_orders():
    return [
        {"id": 1, "amount": 100.0},
        {"id": 2, "amount": 250.5},
        {"id": 3, "amount": 0.0},
    ]

def total_amount(orders):
    return sum(o["amount"] for o in orders)

def test_total_amount(sample_orders):
    assert total_amount(sample_orders) == 350.5
