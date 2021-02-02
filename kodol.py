nyilt_szoveg = input("Nyílt szöveg: ")

if nyilt_szoveg == "":
    print("hiba")

if len(nyilt_szoveg.strip()) > 255:
    print("hiba")

nyilt_szoveg = nyilt_szoveg.upper()

magyar_angol_szotar = {"Á":"A", "É":"E", "Ű":"U", "Ú":"U", "Ü":"U", "Ó":"O", "Ö":"O", "Ő":"O", "Í":'I'}

for i in range(len(nyilt_szoveg)):
    if nyilt_szoveg[i] in magyar_angol_szotar:
        nyilt_szoveg = nyilt_szoveg.replace(nyilt_szoveg[i], magyar_angol_szotar[nyilt_szoveg[i]])

print("Szöveg átalakítása: ", nyilt_szoveg)

kulcsszo = input("Kulcsszo: ")


##### #### ## ## ##### ## ## #### #### ## ## #### ### ### ###



if kulcsszo == "":
    print("hiba")

kulcsszo = kulcsszo.strip()

if len(kulcsszo) > 5:
    print("hiba")

kulcsszo = kulcsszo.upper()
print("Kulcsszó nagybetűssé alakítása: ", kulcsszo)
kulcsszo_osszefuzve = []

for i in range(len(nyilt_szoveg)):
    kulcsszo_osszefuzve.append(kulcsszo[i % len(kulcsszo)])

txt = open(r'..\kodol_feladat\Vtabla.dat', 'r')
sor = txt.readline()
vtabla = []

while sor !="":
    vtabla.append(sor.strip())
    sor = txt.readline()

txt.close()
kodolt = []

for i in range(len(nyilt_szoveg)):
    for sor in vtabla:
        if sor[0] == nyilt_szoveg[i]:

            index = 0
            while vtabla[0][index] != kulcsszo_osszefuzve[i]:
                index += 1

            kodolt.append(sor[index])

txt = open(r'..\kodol_feladat\kodolt.dat', 'w')
txt.write("".join(kodolt))
txt.close()

input("Enter megnyomására bezáródik a program...")