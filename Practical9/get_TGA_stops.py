Input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
Output = open('TGA_genes.fa', 'w')
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
    # find the line end with TGA and write this line and the line before this line to the output file
    if content2.split("\n")[i].endswith("TGA"):
        Output.write(content2.split("\n")[i-1] + "\n" + content2.split("\n")[i] + "\n")
Input.close()
Output.close()
