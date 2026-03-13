text = "Hello i'm a string"
result = text[4]

print (result)

text_2 = "hello i'm another string"
result_2 = text[-4]
print(result_2)

text_3 = "hello i'm the third string"

result_3 = text_3[0:4]
print(result_3)

text_4 = "hello i'm the fourth string"
result_4 = text_4.index("h", 4, 15)

print(result_4)

# para buscar de derecha a izquierda:

text_5 = "hello i'm the fifth string"
result_5 = text_5.rindex("h")
print(result_5)