#counting number of nucleotides for RNA

from validateseq import validateseq
def countnucrna(seq):
    seq=seq.replace("\n","")
    temp={"A":0,"C":0,"G":0,"U":0}
    for n in seq:
        temp[n] += 1
    print(temp["A"],temp["C"],temp["G"],temp["U"])

countnucrna(validateseq("""GAUGGAACUUGACUACGUAAAUU"""))
