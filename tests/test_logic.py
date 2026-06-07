"""Testy programu."""
from src.logic import kalkulator


def test_kalkulator():
    """Sprawdza mnozenie."""
    assert kalkulator(5) == 10