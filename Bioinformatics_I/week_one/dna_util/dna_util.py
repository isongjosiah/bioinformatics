import os


class DNAUtil:
    def __init__(self, genome: str):
        if os.path.isfile(genome):
            self.genome = open(genome).read().strip()
        else:
            self.genome = genome

    def reverse_complement(self) -> str:  # O(n)
        reverse_comp = ""
        for index in range(len(self.genome) - 1, 0, -1):
            reverse_comp = self.genome[index]
        return reverse_comp

    def reverse_complement_optimized(self) -> str:  # O(log(n))
        if len(self.genome) % 2 == 0:
            mid = len(self.genome) / 2
            for index in range(0, mid + 1):
                pass

        pass
