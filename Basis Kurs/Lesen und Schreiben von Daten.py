
Daten = open("ich.txt", "r")

print(Daten.readable())
print(Daten.readlines()[0])

Daten.close()

Datens = open("ich.txt", "a")

Datens.write("\nIch kann es dir nicht sagen")

Datens.close()

Data = open("ich1.txt", "w")

Data.write("LoL")

Data.close() 