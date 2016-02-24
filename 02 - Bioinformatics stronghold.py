#!/usr/bin/python

#01 - Counting DNA Nucleotides

string = open('rosalind_dna.txt', 'r')
sequence = string.readline()
print sequence
print sequence.count("A"), sequence.count("C"), sequence.count("G"), sequence.count("T")

#The elegant way
'''
def qt(s):
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")
'''
'''
file = open('./rosalind1.txt', 'r')
string = file.read()
freq = {'A': 0, 'C': 0, 'G': 0, 'U': 0}
for i in string:
    freq[i] = freq[i] + 1

print freq['A'], freq['C'], freq['G'], freq['U']
'''
