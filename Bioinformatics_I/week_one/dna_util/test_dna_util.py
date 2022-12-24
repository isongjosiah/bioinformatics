import pytest
from dna_util import DNAUtil


class TestDNAUtil:
    def test_reverse_complement(self, benchmark):
        genome = "ATGCT"
        du = DNAUtil(genome)
        result = benchmark(du.reverse_complement)
        assert "TCGTA" == result

    def test_reverse_complement_optimzied(self, benchmark):
        genome = "ATGCT"
        du = DNAUtil(genome)
        result = benchmark(du.reverse_complement_optimized)
        assert "TCGTA" == result
