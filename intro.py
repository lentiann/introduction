
numri1 = 5
numri2 = 5

mosha = 18
qyteti = "Tirana"

shuma = numri1 + numri2
zbritja = numri1 - numri2
shumezimi = numri1 * numri2
pjestimi = numri1 // numri2
modulo = numri1 % numri2
fuqia = numri1 ** numri2

names = ["John", "Doe1"]

# > , < , >= , <= , == , != Operatoret e krahasim (comparison operators)
# logic operators AND, OR, NOT 

# print(f"Shuma e numrave {numri1} dhe {numri2} eshte = {shuma}")
# print(f"zbritja e numrave {numri1} dhe {numri2} eshte = {zbritja}")
# print(f"shumezimi e numrave {numri1} dhe {numri2} eshte = {shumezimi}")
# print(f"pjestimi e numrave {numri1} dhe {numri2} eshte = {pjestimi}")
# print(f"modulo e numrave {numri1} dhe {numri2} eshte = {modulo}")
# print(f"fuqia e numrave {numri1} dhe {numri2} eshte = {fuqia}")

# if numri1 > numri2:
#     print(f"{numri1} eshte me i madh se {numri2}")
# elif numri1 < numri2:
#     print(f"{numri1} eshte me i vogel se {numri2}")
# else:
#     print(f"{numri1} eshte i barabarte me {numri2}")

# if (numri1 == numri2) or (mosha == 17 and qyteti == "Durres"):
#     print("Te gjitha kushtet jane te plotesuara")


# match mosha:
#     case 18 | 19:
#         print("Ju jeni te lejuar per te hyre brenda")
#     case 17:
#         print("Ju duhet te prisni edhe nje vit")   
#     case _:
#         print("Na vie keq nuk mundeni te hyjni ne lokal")

match names:
    case ["John", "Doe"]:
        print("Emri i personit eshte John Doe")
    case ["Jane", "Doe"]:
        print("Emri i personit eshte Jane Doe")
    case _:
        print("Emri i personit nuk njihet")