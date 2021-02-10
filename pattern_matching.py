def pattern_matching(genome :str, pattern :str) -> list:
    index = []
    for i in range(len(genome)):
        if genome[i:i+len(pattern)] == pattern:
            index.append(str(i))
    output = " ".join(index)
    return output


#read the vibro cholerae genome and check for a pattern
file_path = './Vibrio_cholerae.txt'
pattern = 'CTTGATCAT'

with open(file_path) as f:
    data = f.read()
    print(pattern_matching(data, pattern))
