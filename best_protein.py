from collections import defaultdict
import ftplib
import os

def best_protein(genome_id, biotic):
    file_nm = genome_id + '.PATRIC.ffn'
    if no os.pat.isfile('./sequences/' + file_nm):
        conn = ftplib.FTP('ftp.patricbrc.org')
        conn.login()
        conn.cwd('/patric2/genomes/' + genome_id + '/')
        conn.retribinary('RETR ' + file_nm, open('./sequences/' + file_nm, 'wb').write)
        conn.quit()

    file_name = "./sequences/" + genome_id
    f = open(file_name, "r")
    temp_split = f.split(">")
    found_biotic = False
    first_match = ""
    second_match = ""
    for sub_seq in temp_split:
        if biotic.lower() in temp_split.split("]")[0].lower():
            first_match += temp_split.split("]")[1].rstrip()
        if "antibiotic" in temp_split.split("]")[0].lower():
            second_match += temp_split.split("]")[1].rstrip()

    if first_match:
        return first_match
    else:
        return second_match


if __name__ == "__main__":
    best_protein(argv[1], argv[2])
