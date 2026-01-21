from src.poetry_demo.mate import somma

def test_somma_numeri_interi():
    assert somma(2, 2) == 4
    assert somma(10, -5) == 5