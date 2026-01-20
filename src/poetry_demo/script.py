def calcola_media(numeri):
    if not numeri:
        raise ValueError("La lista non può essere vuota")
    return sum(numeri) / len(numeri)
