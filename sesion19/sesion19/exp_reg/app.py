import re

#print(re.search('python', 'Me gusta mucho aprender python ya que me permitira ganarme la vida como developer python'))
#print(re.findall('python', 'Me gusta mucho aprender python ya que me permitira ganarme la vida como developer python'))
#print(re.match('python', 'python Me gusta mucho aprender python ya que me permitira ganarme la vida como developer'))
for match in re.finditer('python', 'Me gusta mucho aprender python ya que me permitira ganarme la vida como developer python'):
    #print(match.start(), match.end())
    #print(match)
    pass

#print(r"\tHola\nAdios")

pattern = re.compile(r'\d')
sentence = "En el summary test de Python Essential 1 he sacado un 8"

#print(pattern.findall(sentence))


pattern = re.compile(r'\D')
#print(pattern.findall(sentence))

pattern = re.compile(r'\w')
#print(pattern.findall(sentence))

pattern = re.compile(r'La sandia')

match = pattern.match('La sandia que compre el otro dia estaba muy dulce')

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())


sentece = "Mi correo es ricardo@gmail.com y el correo de mi hermano es hermano@gmail.com"
pattern = re.compile(r'[A-Z]\w+')

print(pattern.findall(sentece))



