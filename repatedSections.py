import math
import re

def countSectionRepeats(str, minLength, sectionCounts={}):
  for length in range(minLength, math.ceil(len(str) / 2)):
    for i in range(len(str) - length):
      sectionCounts[str[i:i+length]] = sectionCounts.get(str[i:i+length], 0) + 1
  
  return {sect: sectionCounts[sect] for sect in sectionCounts if sectionCounts[sect] > 1}
