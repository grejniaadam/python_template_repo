"""Glowny modul programu."""
from src.logic import kalkulator


def main():
    """Uruchamia program."""
    wynik = kalkulator(5)
    print(wynik)


if __name__ == "__main__":
    main()