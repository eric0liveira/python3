try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Divisão por zero não existe")
finally:
    print("Execução finalizada")