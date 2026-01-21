from src.poetry_demo.prova import sottrazione
from src.poetry_demo.mate import somma

def main():
    a = 10
    b = 5
    result = sottrazione(a, b)
    print(f"La sottrazione di {a} e {b} è: {result}")
    
    print(somma(1,2))

if __name__ == "__main__":
    main()