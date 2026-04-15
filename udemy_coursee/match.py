serie = "N-02"

# if serie == "N-01":
#     print("Samsung")
# elif serie == "N-02":
#     print("Nokia")
# elif serie == "N-03":
#     print("Mootorola")
# else:
#     print("No se encontro")

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Mootorola")
    case _:
        print("No se encontro")
    