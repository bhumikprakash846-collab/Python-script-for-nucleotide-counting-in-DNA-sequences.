nucleotides=['A','G','C','T']
nucleotides_rna=['A','C','G','U']

def validateseq(dna_seq):
    tempseq=dna_seq.upper()
    s=input("is it dna sequence?(y/n):").lower()
    if s=='y':
        for n in tempseq:
            if n not in nucleotides:
                print("seq invalid",n)
        print(tempseq)
        return tempseq
    elif s=='n':
        for n in tempseq:
            if n not in nucleotides_rna:
                print("seq invalid",n)
        print(tempseq)
        return tempseq
    else:
        print("invalid")
        return None
    return tempseq

