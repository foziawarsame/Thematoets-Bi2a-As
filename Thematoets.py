#Thematoets
#Fozia Warsame Bin1-c
#13-01-2021


import re
import matplotlib.pyplot as plt

def inlezen_fasta(bestandsnaam):
    """Leest het fasta bestand in en maakt van de data 2 lijsten,
    voor de headers en eiwitsequenties

    :param bestandsnaam - str - fasta file met de eiwitten van C.elegans
    :return: headers: - list - alle headers van de eiwitten van C.elegans
             seqs: - list - alle eiwitsequenties van C.elegans
    """

    headers = []
    seqs = []
    string = ""

    with open(bestandsnaam, "r") as bestand:
        for regel in bestand:
            regel = regel.strip()
            if ">" in regel:
                if string != "":
                    #Voegt de volledige sequentie toe aan de list
                    seqs.append(string)
                    #Maakt de string weer leeg voor de volgende sequentie
                    string = ""
                #De headers worden aan een aparte list toegevoegt
                headers.append(regel)
            else:
                #Maakt van de lossen sequentie stukken een lange string
                string += regel.strip()
        #Voegt de laaste sequentie toe aan de list
        seqs.append(string)

    return headers, seqs


def inlezen_gff3(bestandsnaam):
    """Leest het gff3 bestand in en stopt de data in een 2D lijst,
    er zijn 9 kolommen

    :param bestandnaam: - str - gff3 file met genoom data van C.elegans
    :return: genoom - 2D list - lijst met al de genoom data
    """

    genoom = []

    with open(bestandsnaam, "r") as bestand:
        for regel in bestand:
            #Verwijdert alle enters en split op tabs
            regel = regel.rstrip().split("\t")
            #Voegt de regel als list toe aan een list waardoor je 2D list krijgt
            genoom += [regel]


    return genoom



def dictionary(headers, seqs):
    """Maakt van de lijsten een dictionary,
    key: headers, value: eiwitsequentie

    :param headers: - list - alle headers van de eiwitten van C.elegans
    :param seqs: - list - alle eiwitsequenties van C.elegans
    :return: eiwitten - dict - de eiwit data, keys: de headers, values:
     de eiwitsequenties
    """

    eiwitten = {}

    for i in range(len(headers)):
        #Voegt de elementen in de lijsten toe aan een dictionary
        eiwitten[headers[i]] = seqs[i]


    return eiwitten


def zinc_finger(eiwitten):
    """Zoekt in de eiwitsequenties naar de consensus patroon
    doormiddel van een regular expression

    :param eiwitten: - dict - alle eiwitten van C.elegans
           keys: de headers, values: de eiwitsequenties
    :return zinc: - list - alle headers van eiwitten met een zinc finger
    """

    zinc = []
    zonder_zinc = []

    for key, value in eiwitten.items():
        match = re.search(r"[^BJOUX].C[^BJOUX]{2}C[^BJOUX]{2}C[^BJOUX]{5}C[^BJOUX]{2}C[^BJOUX]{2}C[^BJOUX].", value)
        #Zoekt in de dictionary values naar de eiwitten met een zinc finger
        if match:
            #Bij een match wordt de header van het eiwit met zinc finger in een lijst gestopt
            zinc.append(key)
        else:
            #Alle headers van eiwitten zonder zinc finger worden in een lijst gestopt
            zonder_zinc.append(key)

    print("Het aantal eiwitten die een zinc finger bevatten: ", len(zinc))
    print("Het aantal eiwitten die geen zinc finger bevatten: ", len(zonder_zinc))

    return zinc



def genes(genoom):
    """Zoekt in de genoom lijst naar alle genen en stopt die
    in een aparte lijst

    :param genoom: - 2D list - lijst met al de genoom data
    :return: genen - 2D list - lijst met alle genen van C.elegans
    """

    genen = []

    #Filtert in de genoom data naar alle genen en stopt die in een lijst
    for i in genoom:
        # Regels die we niet nodig hebben, bestaan uit weinig
        # kolommen die wordenn eruit gefiltert
        if len(i) < 2:
            #Gaat naar de volgende if statement als de lengte te klein is
            continue
        if "gene" in i[2]:
            #Zoekt naar de genen en voegt ze toe aan een lijst
            genen.append(i)

    return genen



def lengte(genen):
    """Berekent per gen de lengte door start positie - stop positie

    :param genen - list - lijst met alle genen
    :return: lengtes - list - alle lengtes van de genen van C.elegans
    """

    lengtes = []

    #Zoekt in de genen naar de start en stop positie om de lengte te
    #bepalen en voegt alle lengtes van de genen aan een lijst
    for gen in genen:
        start = int(gen[3])
        stop = int(gen[4])
        lengte = stop - start
        lengtes.append(lengte)

    return lengtes

def waarden(genen, lengtes):
    """Bepaald de kortste en langste gen van C.elegans en laat het chromosoom
    zien waar ze op liggen. Berekent ook de gemiddelde lengte van een gen

    :param lengtes: - list - alle lengtes van de genen van C.elegans
            genen:  - list - lijst met alle genen
    :return: extreme waarden - str - min, max en gemiddelde
    """

    #Bepaald de langste en kortste lengtes van een gen
    langste = max(lengtes)
    kortste = min(lengtes)
    #Berekent de gemiddelde lengte van één gen en rond het af
    gem = round((sum(lengtes) / len(lengtes)), 0)

    #Zoekt naar de index van het langste gen om te achterhalen
    #welk (nummer) gen het is
    pos = 0
    for x in lengtes:
        pos += 1
        if x == langste:
            #Zoekt door de genen lijst naar het langste gen en laat het
            #chromosoom zien waar het gen bijhoort
            chr_langste = genen[pos][0]

    #Zoekt naar de index van het kortste gen om te achterhalen
    #welk (nummer) gen het is
    pos = 0
    for x in lengtes:
        pos +=1
        if x == kortste:
            #Zoekt door de genen lijst naar het kortste gen en laat het
            #chromosoom zien waar het gen bijhoort
            chr_kortste = genen[pos][0]

    print("De gemiddelde lengte van een gen van C.elegans is", gem)
    print("Het langste gen is", langste, "en ligt op chromosoom", chr_langste)
    print("Het kortste gen is", kortste, "en ligt op chromosoom", chr_kortste)


def boxplot(lengtes):
    """Maakt een boxplot van de lengtes van alle genen van C.elegans

    :param lengtes: - list - alle lengtes van de genen
    :return: de grafiek - plot - unieke lengtes en hoevaak ze voorkomen
    """

    #Maakt een lijst van alle unieke lengtes
    unieke_len = list(set(lengtes))

    aantal_len = []

    for i in unieke_len:
        #Kijkt hoevaak een bepaalde lengte voorkomt en voegt die toe aan
        #een lijst om te kunnen gebruiken voor de grafiek
        aantal_len.append(lengtes.count(i))

    plt.boxplot(unieke_len, aantal_len)
    #Voegt een titel toe
    plt.title("Lengte van genen C.elegans")
    #Voegt x en y labels toe
    plt.xlabel("Genen")
    plt.ylabel("Lengtes")
    #Laat de grafiek zien
    plt.show()

def chromosoom(genen):
    """Berekent het aantal genen per chromosoom en laat het zien in een dictionary,
    key: chromosoom, value: aantal genen

    :param genen: - 2D list - lijst met alle genen
    :return: aantal_chr: - list - het aantal genen per chromosoom
             uniek_chr: - list - de unieke chromosomen
    """

    chr = []
    for gen in genen:
        #Voegt alle chromosomen waar genen opstaan toe aan een lijst
        chr.append(gen[0])

    #Maakt een lijst van alle unieke chromosomen
    unieke_chr = list(set(chr))

    aantal_chr = []

    for i in unieke_chr:
        #Telt per chromosoom hoevaak die voorkomt, dus hoeveel genen
        #per chromosoom en voegt het aantal toe aan een lijst
        aantal_chr.append(chr.count(i))


    chr_gen = {}

    for i in range(len(unieke_chr)):
        #Voegt de elementen in de lijsten toe aan een dictionary,
        #keys: de verschillende chromosomen, values: het aantal genen
        chr_gen[unieke_chr[i]] = aantal_chr[i]

    print("Het aantal genen per chromosoom: ", chr_gen)

    return aantal_chr, unieke_chr


def taartdiagram(aantal_chr, unieke_chr):
    """Maakt een taartdiagram van het aantal genen per chromosoom

    :param aantal_chr: - list - het aantal genen per chromosoom
    :param unieke_chr: - list - de unieke chromosomen
    :return: grafiek - plot - een taartdiagram
    """

    #Maakt een taartdiagram van de data
    plt.pie(aantal_chr, labels= unieke_chr, autopct="%1.f%%")
    #Voegt een titel toe
    plt.title("Percentage genen per chromosoom")
    #Voegt een legenda toe
    plt.legend(unieke_chr, loc="upper right")
    #Laat de taartdiagram zien
    plt.show()




def strands(genen):
    """Kijkt naar hoeveel genen er op de forward(+) en reverse(-) strand zitten,
    en maakt een dict ervan. keys: forward, reverse; values: genen

    :param genen: - 2D list - alle genen van C.elegans
    :return: strands - dict - positie van de genen in een dictionary
             keys: forward(+), reverse(-); values: de genen
    """

    positie = []

    strands ={}

    for gen in genen:
        #Zoekt per gen of die op de forward of reverse strand staat
        #en voegt die toe aan een lijst
        positie += gen[6]

    for i in range(len(positie)):
        #Voegt de elementen in de lijst toe aan een dictionary
        strands[positie[i]] = genen[i]

    return strands



def zoeken(zinc, genen):
    """Zoekt in de lijst met genen naar de genen die coderen voor
    de eiwitten met een zinc finger

    :param zinc: - list - alle headers van eiwitten met een zinc finger
    :param genen: - 2D list - alle genen van C.elegans
    :return gen_zinc: - list - alle genen die coderen voor zinc finger eiwitten
    """

    #Split de string(headers), zodat elk deel van van de header een aparte element wordt
    zincfinger = []
    for i in zinc:
        i = i.split()
        #Voegt de gesplite headers weer toe aan een lijst
        zincfinger.append(i)

    #Zoekt naar de gennamen in de header van de zinc finger eiwitten
    gen_naam = []
    for i in zincfinger:
        naam = i[3]
        #Voegt alle gennamen toe aan een lijst
        gen_naam.append(naam)

    #Genen die voor een eiwit met zinc finger coderen
    gen_zinc = []

    #Zoekt in naar de naam in de genen lijst en voegt het gen toe aan een lijst
    for i in gen_naam:
        for gen in genen:
            #Index met informatie over het gen dus ook naam
            if i in gen[8]:
                gen_zinc.append(gen)

    print("Genen die coderen voor een eiwit met een zinc finger: ", gen_naam)

    return gen_zinc


def vergelijken(gen_zinc, lengtes):
    """Berekent de lengte van de genen met zinc finger eiwitten en de gemiddelde lengte van
    alle genen van C.elegans

    :param gen_zinc: - list - lijst met alle genen die coderen voor zinc finger eiwitten
    :param lengtes: - list - alle lengtes van de genen
    :return: lengte_zinc: - list - alle lengtes van zinc finger genen
            gemiddelde: - int - de gemiddelde lengte van een gen
    """

    lengte_zinc = []

    # Zoekt in de genen naar de start en stop positie om de lengte te
    # bepalen en voegt alle lengtes van de genen toe aan een lijst
    for gen in gen_zinc:
        start = int(gen[3])
        stop = int(gen[4])
        lengte = stop - start
        lengte_zinc.append(lengte)

    #Berekent de gemiddelde lengte van één gen van C.elegans
    gemiddelde = round((sum(lengtes) / len(lengtes)), 0)

    print("De lengtes van genen die coderen voor een zinc finger eiwit: ", lengte_zinc)

    return lengte_zinc, gemiddelde


def staafdiagram(lengte_zinc, gemiddelde):
    """Vergelijkt de zinc gen lengtes met de gemiddelde gen lengte van C.elegans
    door de gegevens in een staafdiagram te laten zien

    :param lengte_zinc: - list - alle lengtes van zinc finger genen
            gemiddelde: - int - de gemiddelde lengte van een gen
    :return: staafdiagram - plot - de lengtes van zinc finger genen en het gemiddelde van alle genen
    """
    #Maakt van de range een list zodat je de x waarden hebt
    xwaarden = [*range(1,len(lengte_zinc)+1)]
    #Maakt een horizontale lijn om de gemiddelde lengte te laten zien
    plt.hlines(y=gemiddelde, xmin=1, xmax=(max(xwaarden)), colors= "r", label= 'gemiddelde lengte')
    #Maakt een staafdiagram
    plt.bar(xwaarden, lengte_zinc)
    #Voegt x en y labels en titel toe
    plt.ylabel("Lengte")
    plt.xlabel("Genen")
    plt.title("Lengtes van 'zinc finger' genen")
    #Laat de grafiek zien
    plt.show()


if __name__ == '__main__':
    fastafile = "Caenorhabditis_elegans.cds_pep.all.fa"
    headers, seqs = inlezen_fasta(fastafile)
    eiwitten = dictionary(headers, seqs)
    zinc = zinc_finger(eiwitten)
    gff3file = "Caenorhabditis_elegans.gff3"
    genoom = inlezen_gff3(gff3file)
    genen = genes(genoom)
    lengtes = lengte(genen)
    waarden(genen, lengtes)
    boxplot(lengtes)
    aantal_chr, uniek_chr = chromosoom(genen)
    taartdiagram(aantal_chr, uniek_chr)
    strands = strands(genen)
    gen_zinc = zoeken(zinc, genen)
    lengte_zinc, gemiddelde = vergelijken(gen_zinc, lengtes)
    staafdiagram(lengte_zinc, gemiddelde)

