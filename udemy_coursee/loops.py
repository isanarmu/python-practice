# and | or | not
num1 = 5
num2= 10
text = "hola que tal"
mi_bool = num1 != num2 and num1 < num2
mi_bool_2 = num1 != num2 or num1 < num2
mi_bool_3 = "hola" in text or "python" in text
mi_bool_4 = "hola" and "eeeee" not in text
print(mi_bool_2)
print(f"está hola en texto ?: {mi_bool_3}")
print(f"no está hola en texto ?: {mi_bool_4}")