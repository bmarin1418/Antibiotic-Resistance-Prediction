import ftplib
import os, sys

'''
function: best_protein
input: id number of genome, name of biotic, print flag
output: the best protein sequence to feed into our neural network
'''
def best_protein(genome_id, biotic, do_print):
    file_nm = genome_id + ".PATRIC.ffn"
    if not os.path.isfile('./sequences/' + file_nm):
        print("file not found downloading...") if do_print else lambda:None
        conn = ftplib.FTP('ftp.patricbrc.org')
        conn.login()
        print("logged in...") if do_print else lambda:None
        conn.cwd('/patric2/genomes/' + genome_id + '/')
        print("downloading...") if do_print else lambda:None
        conn.retrbinary('RETR ' + file_nm, open('./sequences/' + file_nm, 'wb').write)
        conn.quit()
        print("downloaded...") if do_print else lambda:None
    else:
        print("file found...") if do_print else lambda:None

    file_name = "./sequences/" + file_nm
    file_string = ""
    f = open(file_name, "r")
    for line in f:
        file_string += (line)
    temp_split = file_string.split(">")
    found_biotic = False
    first_match = ""
    second_match = ""
    print("searching for best protein...")
    for sub_seq in temp_split:
        if biotic.lower() in sub_seq.split("]")[0].lower():
            if do_print:
                print("found specific antibiotic sequence!")
                print("\ntitle: \n")
                print(sub_seq.split("]")[0].rstrip())
                print("\nprotein: ")
            #first_match += temp_split.split("]")[1].rstrip()
            return sub_seq.split("]")[1].rstrip()
        if "antibiotic" in sub_seq.split("]")[0].lower():
            if do_print:
                print("found generic antibiotic sequence!")
                print("title: ")
                print(sub_seq.split("]")[0].rstrip())
                print("protein: ")
            #second_match += temp_split.split("]")[1].rstrip()
            return sub_seq.split("]")[1].rstrip()

    if first_match:
        return first_match
    else:
        return second_match


if __name__ == "__main__":
    # pass genome_id, biotic name to best_protein function
    # returns the best protein to use as input to the neural net
    # example call: python best_protein 1400870.3, ofloxacin
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("usage: python best_protein.py genome_id biotic_name print_bool")
        print("example call: python best_protein.py 1400870.3 ofloxacin 1")
    elif len(sys.argv) == 4:
        print(best_protein(sys.argv[1], sys.argv[2], sys.argv[3]))
