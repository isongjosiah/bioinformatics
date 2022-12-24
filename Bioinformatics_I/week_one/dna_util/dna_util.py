import os, argparse, sys


class DNAUtil:
    def __init__(self, genome: str):
        if os.path.isfile(genome):
            self.genome = open(genome).read().strip()
        else:
            self.genome = genome

    def reverse_complement(self) -> str:  # O(n)
        reverse_comp = ""
        for index in range(len(self.genome) - 1, -1, -1):
            reverse_comp += self.genome[index]
        return reverse_comp

    def reverse_complement_optimized(self) -> str:  # O(log(n))
        genome_list = list(self.genome)
        if len(self.genome) % 2 == 0:
            mid = int(len(self.genome) / 2)
            for index in range(0, mid):
                genome_list[index], genome_list[-(index + 1)] = genome_list[-(index + 1)], genome_list[index]
            return ''.join(genome_list)
        else:
            last_element = genome_list.pop()
            mid = int(len(genome_list) / 2)
        for index in range(0, mid):
            genome_list[index], genome_list[-(index + 1)] = genome_list[-(index + 1)], genome_list[index]

        genome_list.insert(0, last_element)
        return ''.join(genome_list)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("[Usage]: python dna_util.py genome [file|text] ")
        sys.exit()

    parser = argparse.ArgumentParser(
        description="[Usage]: python dna_util.py genome [file|text] ")
    parser.add_argument("-g", "--genome", help="the genome either as a file or text")

    args = parser.parse_args()

    input_genome = ""

    if args.genome:
        input_genome = args.genome

    du = DNAUtil(input_genome)
    print(du.reverse_complement_optimized())
