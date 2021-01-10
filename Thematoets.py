#Fozia Warsame Tentamen Thematoets
#opzet code

import re

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


def dna(eiwitten):

    code = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
            'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
            'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
            'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
            'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
            'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
            'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
            'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
            'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
            'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
            'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
            'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
            'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
            'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
            'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
            'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'}

    translatie = {"F": "TTT", "S": "TCT", "Y": "TAT", "C": "TGT",
                  "F": "TTC", "S": "TCC", "Y": ""

    }

    dna = ""

    for key, value in eiwitten.items():
        for i in value:
            amino = code[i]
            dna += amino

    print(dna)





def zinc_finger(eiwitten):
    """Zoekt in de eiwitsequenties naar de consensus patroon
    doormiddel van een regular expression

    :param eiwitten: - dict - alle eiwitten van e.elegans
    keys: de headers, values: de eiwitsequenties
    :return zinc: - list - alle eiwitten met een zinc finger
    """

    zinc = []

    for key, value in eiwitten.items():
        match = re.search(r".*C.{2}C.{2}C.{5}C.{2}C.{2}C.*", value)
        if match:
            return True
        else:
            return False

    #.*C.{2}C.{2}C.{5}C.{2}C.{2}C.*




def taartdiagram(eiwitten, zinc):
    """Geeft in een grafiek weer hoeveel eiwitten/genen van e.elegans
    het zinc patroon hebben doormiddel van matplotlib

    :param eiwitten: - dict - alle eiwitten van e.elegans
    keys: de headers, values: de eiwitsequenties
    :param zinc: - list - alle eiwitten met zinc patroon
    :return: grafiek - plot - hoeveelheid eiwitten met zinc patroon
    """

    #len nemen van list en len nemen van dict.items



def lengte(genoom):
    """Zoekt in de lijst naar de genen en berekent per gen
    de lengte door start positie - stop positie en
    de gemiddelde lengte van een gen van e.elegans

    :param genoom: - 2D list - lijst met al de genoom data
    :return: lengtes - list - alle lengtes van de genen van e.elegans
    """

    #zoek in de kolom met namen naar "gene", met if "gene" in de kolom
    #start = daarna zoek in kolom/index met start positie
    #stop = kolom/index start positie
    #len = start - stop, voeg toe aan lijst lengtes

    lengtes = []
    genen = []

    for i in genoom:
        if len(i) < 2:
            continue
        if "gene" in i[2]:
            genen.append(i)

    for gen in genen:
        start = int(gen[3])
        stop = int(gen[4])
        lengte = stop - start
        lengtes.append(lengte)

    langste = max(lengtes)
    korste = min(lengtes)
    gem = sum(lengtes) / len(lengtes)

    pos = 0
    for x in lengtes:
        pos +=1
        if x == langste:
            positie = genen[pos][0]

    pos = 0
    for x in lengtes:
        pos +=1
        if x == korste:
            positie = genen[pos][0]

    print(gem)
    print("Het langste gen is", langste, "en ligt op chromosoom", positie)









if __name__ == '__main__':
    #fastafile = "Caenorhabditis_elegans.cds_pep.all.fa"
    #headers, seqs = inlezen_fasta(fastafile)
    #eiwitten = dictionary(headers, seqs)
    #dna(eiwitten)
    #zinc = zinc_finger(eiwitten)
    #taartdiagram(eiwitten, zinc)
    gff3file = "Caenorhabditis_elegans.gff3"
    genoom = inlezen_gff3(gff3file)
    lengtes = lengte(genoom)
