import pytest
from pattern_count import PatternCount


class TestPatterCount:
    # test case for print details of Snack
    def test_details_i(self):
        """ tests that the class initiates the correct values when texts are passed"""
        genome = "ATTCCTCTATCCTAATCATAATATCCATCATCAT"
        pattern = "AT"
        pc = PatternCount(genome, pattern)
        assert (genome, pattern) == (pc.genome, pc.pattern)

    def test_details_ii(self):
        """ tests that the class initiates the correct values when files are passed"""
        genome = "./genome.txt"
        pattern = "./pattern.txt"
        genome_text = "ATTCCTCTATCCTAATCATAATATCCATCATCAT"
        pattern_text = "AT"
        pc = PatternCount(genome, pattern)
        assert (genome_text, pattern_text) == (pc.genome, pc.pattern)

    def test_count(self):
        genome = "ATTCCTCTATCCTAATCATAATATCCATCATCAT"
        pattern = "AT"
        pc = PatternCount(genome, pattern)
        assert 8 == pc.count()

    def test_frequent(self):
        genome = "ATTCCTCTATCCTAATCATAATATCCATCATCAT"
        pattern = "AT"
        pattern_length = 2
        pc = PatternCount(genome, pattern, pattern_length)
        assert ["AT"] == pc.frequent()
