def contar_formaciones(palabra: str, cadena: str):
    contador = 0
    palabra_objetivo = list(palabra)

    for letra in cadena:
        letra_objetivo = palabra_objetivo.pop(0)
        if letra == letra_objetivo:
            if len(palabra_objetivo) == 0:
                contador += 1
                palabra_objetivo = list(palabra)
        else:
            # palabra_objetivo = list(palabra)
            palabra_objetivo.insert(0, letra_objetivo)

    return contador


cadena = "dadadadddaa"
palabra_objetivo = "ada"
resultado = contar_formaciones(palabra_objetivo, cadena)
print(resultado)
