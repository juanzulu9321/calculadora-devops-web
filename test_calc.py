cat <<'EOF' > test_calc.py
import pytest
from calc import suma, resta, multiplicar, dividir

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 3) == 2

def test_multiplicar():
    assert multiplicar(2, 3) == 6

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)
EOF

