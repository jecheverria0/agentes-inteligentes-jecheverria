# Problema 3: Sistema Experto para Diagnóstico Simple (Basado en Conocimiento)
def diagnostico():
    sintomas = input("Ingrese sus síntomas separados por coma: ").lower()
    if "fiebre" in sintomas and "tos" in sintomas:
        print("Posible diagnóstico: Gripe")
    elif "dolor de cabeza" in sintomas and "náuseas" in sintomas:
        print("Posible diagnóstico: Migraña")
    else:
        print("No se puede determinar el diagnóstico. Consulte a un médico.")