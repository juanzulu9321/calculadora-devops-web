cat <<'EOF' > calc.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("División por cero no permitida")
    return a / b
EOF

