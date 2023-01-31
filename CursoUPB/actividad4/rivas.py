def miperrito(alfa):

    if alfa== "rivas":
        print("Eñ rivas es el mejor")
        return True
    elif alfa== "julian":
        print("el chino julian merece la pena, completamente")
        return True
    else:
        print("escriba otro nombre")
        return False

def main():
    alfa= str(input("A quien quieres dedicar un mensaje:"))
    print(alfa)
    miperrito(alfa)

main()