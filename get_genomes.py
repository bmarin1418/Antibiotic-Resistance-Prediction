from collections import defaultdict

def get_genomes_tested():
    genomes_tested_by = defaultdict(lambda: set())

    # col: 0: genome id, 1: genome_name, 2: taxon_id, 3: antibiotic, ect
    # we want a dictionary where key: antibiotic val: set(genome_ids that are tested agains the antibiotic key)
    tsf = open("./PATRIC_genomes_AMR.tsv", "r")
    for line in tsf:
        temp = line.split('\t')
        genome_id = temp[0]
        antibiotic = temp[3]
        genomes_tested_by[antibiotic].add(str(genome_id)) if str(genome_id).strip() != "genome_id" else lambda:None
        #print("Adding ", str(genome_id), " to : ", antibiotic) if str(genome_id).strip() != "genome_id" else lambda:None

    return genomes_tested_by
