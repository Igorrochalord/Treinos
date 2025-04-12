def tabuada():
    for i in range (0,11):
        print(f"Tabuada do {i}")
        for j in range (0,11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
        print(" ")
if __name__ == "__main__":
    tabuada()