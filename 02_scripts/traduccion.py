# Diccionario del código genético (ADN -> aminoácido, código de una letra)
codigo_genetico = {
'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
'ATT':'I','ATC':'I','ATA':'I','ATG':'M',
'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*',
'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
'TGT':'C','TGC':'C','TGA':'*','TGG':'W',
'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
'GGT':'G','GGC':'G','GGA':'G','GGG':'G',
}
def traducir(secuencia_adn):
"""Traduce ADN a proteína leyendo de 3 en 3 letras (codones)
desde el principio del texto que se le entregue."""
secuencia_adn = secuencia_adn.upper().replace(" ", "").replace("\n", "")
proteina = ""
for i in range(0, len(secuencia_adn) - 2, 3):
codon = secuencia_adn[i:i+3]
aminoacido = codigo_genetico.get(codon, "?")
if aminoacido == "*":
break # codón de parada: aquí termina la proteína
proteina += aminoacido
return proteina
# 1) Busque el primer "ATG" en su secuencia y pegue DESDE AHÍ en la variable de
abajo
# (copie el fragmento de su gen, tomado del archivo FASTA de la Semana 1)
mi_secuencia = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
print("Secuencia de ADN: ", mi_secuencia)
print("Proteína traducida:", traducir(mi_secuencia))
