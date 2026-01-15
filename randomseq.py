#random sequence
from validateseq import validateseq
import random
nucleotides=["A","C","G","T"]
randDNAStr=''.join(random.choice(nucleotides) for n in range(12))
d=validateseq(randDNAStr)

