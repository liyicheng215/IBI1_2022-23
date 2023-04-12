import re

stop_codon = input("Please enter one of the three stop codons (TAA, TAG, or TGA): ")
filename = f"{stop_codon}_stop_genes.fa"
Input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
Output = open(filename, 'w')
content1 = Input.read()
# Read the contents of the input file and store them in a variable
content2 = ""
# Initialize an empty string to store the content
for line in content1.split("\n"):  # pick out the name and combine the sequence into one line into content2
    if line.startswith(">"):
        content2 += "\n" + line.split(" ")[0] + "\n"
    else:
        content2 += line
for i in range(len(content2.split("\n"))):
    if content2.split("\n")[i].endswith(stop_codon):
        # find the line ends with TGA and write this line and the line before this line to the output file，
        # also use re to find the corresponding stop codon number
        N = re.findall(stop_codon, content2.split("\n")[i])
        Output.write(content2.split("\n")[i - 1] + " coding sequences number: " + str(len(N)) + "\n" +
                     content2.split("\n")[i] + "\n")
Input.close()
Output.close()
