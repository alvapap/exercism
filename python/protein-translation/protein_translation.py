def proteins(strand) -> []:
    codon_protein = (("AUG", "Methionine"), ("UUU", "UUC", "Phenylalanine"), ("UUA", "UUG", "Leucine"),\
        ("UCU", "UCC", "UCA", "UCG", "Serine"), ("UAU", "UAC", "Tyrosine"), ("UGU", "UGC", "Cysteine"),\
        ("UGG", "Tryptophan"), ("UAA", "UAG", "UGA", "STOP"))

    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    result = []
    for j in codons:
        for s in codon_protein:
            if j in s:
                if s[-1] != "STOP" and s[-1] not in result:
                    result.append(s[-1])
                else:
                    return result
    return result