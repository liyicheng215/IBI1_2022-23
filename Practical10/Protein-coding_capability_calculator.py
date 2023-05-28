def capacity(sequence):
    sequence = sequence.upper()  # change the sequence to upper case
    start_codon = 'ATG'
    stop_codon = 'TGA'
    length = len(sequence)

    start_position = sequence.find(start_codon)
    stop_position = sequence.rfind(stop_codon)

    if start_position == -1 or stop_position == -1:  # if no start or stop codon, return 'unclear'
        return 'unclear'

    coding_length = stop_position - start_position + 3
    coding_percent = coding_length / length  # calculate the coding percentage

    if coding_percent > 0.5:  # judge the coding capacity
        coding_capacity = 'protein-coding'
    elif coding_percent < 0.1:
        coding_capacity = 'non-coding'
    else:
        coding_capacity = 'unclear'
    return "coding percentage: " '{:.2%}'.format(coding_percent), coding_capacity


# Example for test
a = capacity('atgtgaaaaattatgtttgagtggggggagagagagag')
print(a)
