# FOZIA WARSAME 638928 Bin1-c

import re


def leesbestand(bestandsnaam):
    """Leest het bestand in scheidt het op headers en sequentie

    :param bestandsnaam: - str - het fasta bestand
    :return: seq - list - alle dna sequenties
    """

    header = ""
    seq = []
    dna = ""
    with open(bestandsnaam, "r") as bestand:
        bestand.readline()
        for regel in bestand:
            regel = regel.strip()
            if ">" in regel:
                # De header worden gescheden van de sequenties
                header += regel
                # Voegt de vollede sequentie toe aan de lijst
                seq.append(dna)
                # Maakt het weer leeg voor de volgende sequentie
                dna = ""

            else:
                # Maakt van de losse sequentie stukken één
                # lange string
                dna += regel

    return seq


class DNA:
    """Kijkt of het dna sequentie is, maakt er een mRNA sequentie van,
    berekent de lengte en het gc%
    """

    def __init__(self, seq):
        self.__sequentie = seq

    def setDNA(self, seq):
        """Kijkt doormiddel van een regular expression of het
        een DNA sequentie is
        :param seq - str - de sequentie
        """
        match = re.search(r"[^ATCGN]", seq)
        if match:
            print("dit is geen dna sequentie")
        else:
            self.__sequentie = seq

    def getDNA(self):
        """Return de DNA sequentie
        """
        return self.__sequentie

    def getTranscript(self):
        """Return mRNA sequnentie door T te vervangen door U
        """
        return self.__sequentie.replace("T", "U")

    def getLength(self):
        """Berekent en return de lengte van de sequentie
        """
        return len(self.__sequentie)

    def getGC(self):
        """Berekent en return het GC% van de sequentie
        """
        # Telt alle individuele letters
        a = self.__sequentie.count("A")
        t = self.__sequentie.count("T")
        c = self.__sequentie.count("C")
        g = self.__sequentie.count("G")

        totaal = a + t + c + g
        # Berekent het percentage en rond het af
        perc_gc = round(((g + c) / totaal) * 100, 0)

        return perc_gc


if __name__ == '__main__':
    bestandsnaam = "Felis_catus.Felis_catus_8.0.cdna.all.fa"
    seq = leesbestand(bestandsnaam)
    dna = DNA(seq)

    # Maakt van elke sequentie een object en voegt die toe
    # aan een lijst
    objecten = []
    for i in seq:
        objecten.append(DNA(i))

    # Voegt de GC% van elke sequentie(object) toe aan lijst
    gc_obj = []
    for obj in objecten:
        gc = obj.getGC()
        gc_obj.append(gc)

    # Zoekt naar positie van sequentie met hoogste GC%
    hoogste_gc = max(gc_obj)
    pos = gc_obj.index(hoogste_gc)

    # Returnt de mRNA sequentie en de lengte van de sequentie
    # de hoogste gc%
    trans = objecten[pos].getTranscript()
    length = objecten[pos].getLength()

    print("Gegevens van de sequentie met het hoogste GC%")
    print("mRNA sequentie: ", trans)
    print("Lengte: ", length)
    print("GC%: ", hoogste_gc)
