import math
import sys
import re

def countSectionRepeats(str, minLength, sectionCounts={}):
  for length in range(minLength, math.ceil(len(str) / 2)):
    for i in range(len(str) - length):
      sectionCounts[str[i:i+length]] = sectionCounts.get(str[i:i+length], 0) + 1
  
  return {sect: sectionCounts[sect] for sect in sectionCounts if sectionCounts[sect] > 1}

fileText = open(sys.argv[1]).read()
repeatedSections = countSectionRepeats(fileText, int(sys.argv[2]))
repeatedSections = [(sect, repeatedSections[sect]) for sect in repeatedSections]
repeatedSections = sorted(repeatedSections, key=lambda s: len(s[0]) * repeatedSections[s[1]])

for i in range(min(len(repeatedSections), int(sys.argv[3]))):
  print(repeatedSections[i][0])
