import sys, os, re, math

def text_from_file(fname):
    f = open('txt/' + fname)
    text = f.read()
    f.close()
    return text.replace('\n', ' ')

pattern = re.compile(r'''
  ((?:\w+\s+){3})
  (
    [1-9][0-9]*|
    one|two|three|four|five|six|seven|eight|nine|ten|
    eleven|twelve|thirteen|fourteen|fifteen|
    sixteen|seventeen|eighteen|nineteen|
    (?: (?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)
      (?:\s+|-)
      (?:one|two|three|four|five|six|seven|eight|nine)
    )|
    hundred|thousand
  )
  (\s(?:\w+\s+)?)
  (participant|subject|volunteer|patient|student|player|user|people)s?
  ((?:\s+\S+){3})
''', re.VERBOSE | re.IGNORECASE | re.ASCII)

from word2number.w2n import word_to_num as w2n

for fname in os.listdir('txt'):
  text = text_from_file(fname)
  for match in re.finditer(pattern, text):
    context = match.group(0)
    word = match.group(2)
    num = w2n(word)
    print(num, word, fname, context, sep='\t')


