import sys, os


class PatternCount:
    def __init__(self, genome: str, pattern: str):

        if os.path.isfile(genome):
            self.genome = open(genome).read().strip()
        else:
            self.genome = genome

        if os.path.isfile(pattern):
            self.pattern = open(pattern).read().strip()
        else:
            self.pattern = pattern

    # count counts how many times the pattern appears in the genome
    def count(self) -> int:
        # the index to stop the loop at.
        end_index = len(self.genome) - len(self.pattern)
        count = 0
        for index in range(0, end_index):
            if self.genome[index:index + len(self.pattern)] == self.pattern:
                count += 1

        return count


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("[Usage]: python patter_count.py genome [file|text] pattern [file|text]")
        sys.exit()

    # get genome and pattern
    genome = sys.argv[1]
    pattern = sys.argv[2]

    pc = PatternCount(genome, pattern)
    print(pc.count())
