import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("filename", help="Name of file to count repeated sections in")
parser.add_argument("-l", "--limit", help="Maximum number of results to display", type=int)
parser.add_argument("-m", "--min", help="Minimum length of sequences to consider", type=int)

args = parser.parse_args()

def countSectionRepeats(str, minLength, sectionCounts={}):
  for length in range(minLength, math.ceil(len(str) / 2)):
    for i in range(len(str) - length):
      sectionCounts[str[i:i+length]] = sectionCounts.get(str[i:i+length], 0) + 1
  
  return {sect: sectionCounts[sect] for sect in sectionCounts if sectionCounts[sect] > 1}

fileText = open(args.filename).read()
repeatedSections = countSectionRepeats(fileText, args.min)
repeatedSections = [(sect, repeatedSections[sect]) for sect in repeatedSections]
repeatedSections = sorted(repeatedSections, key=lambda s: len(s[0]) * repeatedSections[s[1]])

for i in range(min(len(repeatedSections), args.limit)):
  print(repeatedSections[i][0])
