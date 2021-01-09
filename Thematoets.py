#Fozia Warsame Tentamen Thematoets
#opzet code

def inlezen_fasta(bestandsnaam):
    """Leest de fastafile in en maakt van de data een dictionary
    key: headers, value: eiwitsequentie

    :param bestandsnaam - str - fastafile met de eiwitten van e.elegans
    :return: eiwitten - dict - de eiwit data, keys: de headers, values:
     de eiwitsequenties
    """



def inlezen_gff3(bestandnaam):
    """Leest het gffs file in en stopt de data in een 2D lijst,
    er zijn 9 kolommen, kolom 9 krijgt aparte lijst

    :param bestandnaam: - str - gff3file met genoom data van e.elegans
    :return: elegans - 2D list - lijst met al de genoom data
    """



def zinc_finger(eiwitten):
    """Zoekt in de seqs naar de patroon doormiddel van regularex

    :param eiwitten: - dict - alle eiwitten van e.elegans
    keys: de headers, values: de eiwitsequenties
    :return zinc: - list - alle eiwitten met zinc patroon
    """

    #loopt langs dict.items bij values kijken naar regex
    #gebruik for loop en if



def taartdiagram(eiwitten, zinc):
    """Geeft in een grafiek weer hoeveel eiwitten/genen van e.elegans
    het zinc patroon hebben doormiddel van matplotlib

    :param eiwitten: - dict - alle eiwitten van e.elegans
    keys: de headers, values: de eiwitsequenties
    :param zinc: - list - alle eiwitten met zinc patroon
    :return: grafiek - plot - hoeveelheid eiwitten met zinc patroon
    """

    #len nemen van list en len nemen van dict.items



def lengte(elegans):
    """Zoekt in de lijst naar de genen en berekent per gen
    de lengte door start positie - stop positie en
    de gemiddelde lengte van een gen van e.elegans

    :param elegans: - 2D list - lijst met al de genoom data
    :return: lengtes - list - alle lengtes van de genen van e.elegans
    """

    #zoek in de kolom met namen naar "gene", met if "gene" in de kolom
    #start = daarna zoek in kolom/index met start positie
    #stop = kolom/index start positie
    #len = start - stop, voeg toe aan lijst lengtes





if __name__ == '__main__':
    fastafile =
    gff3file =
    eiwitten = inlezen_fasta(fastafile)
    elegans = inlezen_gff3(gff3file)
    zinc = zinc_finger(eiwitten)
    taartdiagram(eiwitten, zinc)
    lengtes = lengte(elegans)
