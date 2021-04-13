#!/usr/bin/env python3
import Bio
from Bio.Seq import Seq

print(Bio.__version__)

simple_sequence = Seq("AGTACACTGGT")
print(simple_sequence)
print(simple_sequence.complement())
print(simple_sequence.reverse_complement())


