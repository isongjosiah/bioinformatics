import pytest
from pattern_count import PatternCount


class TestPatterCount:
    # test case for print details of Snack
    def test_details_i(self):
        """ tests that the class initiates the correct values when texts are passed"""
        genome = "ATTCCTCTATCCTAATCATAATATCCATCATCAT"
        pattern = "AT"
        pc = PatternCount(genome, pattern, 0)
        assert (genome, pattern) == (pc.genome, pc.pattern)

    def test_details_ii(self):
        """ tests that the class initiates the correct values when files are passed"""
        genome = "./genome.txt"
        pattern = "./pattern.txt"
        genome_text = "ATTCCTCTATCCTAATCATAATATCCATCATCAT"
        pattern_text = "AT"
        pc = PatternCount(genome, pattern, 0)
        assert (genome_text, pattern_text) == (pc.genome, pc.pattern)

    def test_count(self):
        genome = "ATTCCTCTATCCTAATCATAATATCCATCATCAT"
        pattern = "AT"
        pc = PatternCount(genome, pattern, 0)
        assert 9 == pc.count()

    def test_frequent(self):
        genome = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
        pattern = ""
        pattern_length = 4
        pc = PatternCount(genome, pattern, pattern_length)
        assert ["GCAT", "CATG"] == pc.frequent()


