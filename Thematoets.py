#Fozia Warsame Tentamen Thematoets
#opzet code

import re
import matplotlib.pyplot as plt

def inlezen_fasta(bestandsnaam):
    """Leest de fastafile in en maakt van de data 2 lijsten,
    voor de headers en eiwitsequenties

    :param bestandsnaam - str - fastafile met de eiwitten van e.elegans
    :return: headers: - list - alle headers van de eiwitten van e.elegans
             seqs: - list - alle eiwitsequenties van e.elegans
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
    """Leest het gffs file in en stopt de data in een 2D lijst,
    er zijn 9 kolommen

    :param bestandnaam: - str - gff3file met genoom data van e.elegans
    :return: genoom - 2D list - lijst met al de genoom data
    """

    genoom = []

    with open(bestandsnaam, "r") as bestand:
        for regel in bestand:
            regel = regel.rstrip().split("\t")
            genoom += [regel]

    #print(genoom[16])
    return genoom





def dictionary(headers, seqs):
    """Maakt van de lijsten een dictionary,
    key: headers, value: eiwitsequentie

    :param headers: - list - alle headers van de eiwitten van e.elegans
    :param seqs: - list - alle eiwitsequenties van e.elegans
    :return: eiwitten - dict - de eiwit data, keys: de headers, values:
     de eiwitsequenties
    """

    eiwitten = {}

    for i in range(len(headers)):
        eiwitten[headers[i]] = seqs[i]


    return eiwitten


def zinc_finger(eiwitten):
    """Zoekt in de eiwitsequenties naar de consensus patroon
    doormiddel van een regular expression

    :param eiwitten: - dict - alle eiwitten van e.elegans
    keys: de headers, values: de eiwitsequenties
    :return zinc: - list - alle eiwitten met een zinc finger
            zonder_zinc - list - alle eiwitten zonder zinc finger
    """

    zinc = []
    zonder_zinc = []

    for key, value in eiwitten.items():
        match = re.search(r"[^BJOUX].C[^BJOUX]{2}C[^BJOUX]{2}C[^BJOUX]{5}C[^BJOUX]{2}C[^BJOUX]{2}C[^BJOUX].", value)
        if match:
            zinc.append(value)
        else:
            zonder_zinc.append(key, value)
    print("Het aantal eiwitten die een zinc finger bevatten: ", len(zinc))
    print("Het aantal eiwitten die geen zinc finger bevatten: ", len(zonder_zinc))
    return zinc, zonder_zinc

    #ALLEEN DE SEQS WORDEN IN LIJST GESTOPT NIET DE HEADERS


def taartdiagram(zinc, zonder_zinc, eiwitten):
    """Geeft in een grafiek weer hoeveel eiwitten/genen van e.elegans
    het zinc patroon hebben doormiddel van matplotlib

    :param eiwitten: - dict - alle eiwitten van e.elegans
    keys: de headers, values: de eiwitsequenties
    :param zinc: - list - alle eiwitten met een zinc finger
    :return: grafiek - plot - hoeveelheid eiwitten met zinc patroon
    """

    test = len(zinc)
    lol = len(zonder_zinc)
    totaal = len(eiwitten)

    ok = int(test / totaal * 100)
    ko = int(lol / totaal * 100)
    proteins = [ok, ko]
    groep = ["met zinc", "zonder zin"]


    plt.pie(proteins, labels=groep, autopct="%1.f%%")
    plt.show()



def genes(genoom):
    """Zoekt in de genoom lijst naar alle genen en stopt die
    in een aparte lijst

    :param genoom: - 2D list - lijst met al de genoom data
    :return: genen - list - lijst met alle genen
    """

    genen = []

    # Filtert in de genoom data naar alle genen en stopt die in een lijst
    for i in genoom:
        if len(i) < 2:
            # Regels die we niet nodig hebben, bestaan uit weinig
            # kolommen die wordenn eruit gefiltert
            continue
        if "gene" in i[2]:
            genen.append(i)

    return genen



def lengte(genen):
    """Berekent per gen de lengte door start positie - stop positie en
    de gemiddelde lengte van een gen van e.elegans

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

    #Berekent de langste en kortste gen
    langste = max(lengtes)
    kortste = min(lengtes)
    #Berekent de gemiddelde lengte van een gen en rond het af
    gem = round((sum(lengtes) / len(lengtes)), 0)

    #Zoekt naar de index van het langste gen om te achterhalen
    #welk (nummer) gen het is
    pos = 0
    for x in lengtes:
        pos +=1
        if x == langste:
            #Zoekt door de genen lijst naar het gen en laat het
            #chromosoom zien waar het gen bijhoort
            chr_langste = genen[pos][0]

    # Zoekt naar de index van het kortste gen om te achterhalen
    # welk (nummer) gen het is
    pos = 0
    for x in lengtes:
        pos +=1
        if x == kortste:
            # Zoekt door de genen lijst naar het gen en laat het
            # chromosoom zien waar het gen bijhoort
            chr_kortste = genen[pos][0]

    print("De gemiddelde lengte van een gen van C.elegans is", gem)
    print("Het langste gen is", langste, "en ligt op chromosoom", chr_langste)
    print("Het kortste gen is", kortste, "en ligt op chromosoom", chr_kortste)


    return lengtes


def chromosoom(genen):
    """Kijkt naar het aantal genen per chromosoom

    :param genen: - list - lijst met alle genen
    :return:
    """
    chr = []
    count = 0
    test = []
    for gen in genen:
        if gen[0] == gen[0]:
            count += 1
        else:
            test.append(count)
            count = 0

        chr.append(gen[0])

    print(test)

    lol = list(set(chr))
    print(lol)



def strand(genen):
    """Kijkt naar hoeveel genen er op forward en reverse zitten,
    en maakt een dict ervan. keys: forward, reverse; values: genen

    :param genen:
    :return:
    """

    strand = []
    aantal = []

    for gen in genen:
       strand += gen[6]

    strands = list(set(strand))

    for i in strands:
        aantal.append(strand.count(i))

    plt.plot(strands, aantal)
    plt.show()


def boxplot(lengtes):
    """Maakt een boxplot van de lengtes van alle genen van C.elegans

    :param lengtes: - list - alle lengtes van de genen
    :return:
    """

    plt.hist(lengtes)
    plt.show()






if __name__ == '__main__':
    #fastafile = "Caenorhabditis_elegans.cds_pep.all.fa"
    #headers, seqs = inlezen_fasta(fastafile)
    #eiwitten = dictionary(headers, seqs)
    #zinc, zonder_zinc = zinc_finger(eiwitten)
    #taartdiagram(zinc, zonder_zinc, eiwitten)
    gff3file = "Caenorhabditis_elegans.gff3"
    genoom = inlezen_gff3(gff3file)
    genen = genes(genoom)
    #lengtes = lengte(genen)
    #chromosoom(genen)
    strand(genen)
    #boxplot(lengtes)
