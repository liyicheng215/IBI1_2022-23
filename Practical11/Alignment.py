import pandas as pd

blosum62 = pd.read_excel('BLOSUM.xlsx', index_col=0)


def blosum(aa1, aa2):
    return blosum62.loc[aa1, aa2]


with open("ACE2_human.fa", "r") as seq1, open("ACE2_cat.fa", "r") as seq2, open("ACE2_mouse.fa", "r") as seq3:
    content1 = seq1.read()
    content2 = seq2.read()
    content3 = seq3.read()


    def get_seq(content):
        seq = content.split("\n")
        return seq


    human_seq = get_seq(content1)
    cat_seq = get_seq(content2)
    mouse_seq = get_seq(content3)


def compare(a, b):
    score = 0
    identical = 0
    a_name = a[0]
    b_name = b[0]
    a_seq = a[1]
    b_seq = b[1]
    for i in range(len(a_seq)):
        score += blosum(a_seq[i], b_seq[i])
        if a_seq[i] == b_seq[i]:
            identical += 1
    percentage = identical / len(a_seq)
    percent = '{:.2%}'.format(percentage)
    print(f"{a_name} {a_seq} \n{b_name} {b_seq} \nscore: {score} \npercentage of identical amino acids: {percent}\n")


compare(human_seq, cat_seq)
compare(mouse_seq, cat_seq)
compare(human_seq, mouse_seq)
