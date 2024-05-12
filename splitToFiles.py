from hebrew import Hebrew
import re

output_file = open('output.txt', 'w', encoding='utf-8')


filename = 'tehilim.txt'
with open(filename, 'r', encoding='utf-8') as input_file:
  string = input_file.read() 


matches = re.findall('\(.\)|\(..\)|\(...\)', string) # (א) | (יב) | (קיב)
for i in matches:
  string = string.replace(i, '\n')

matches = re.findall('.*פרק.*' , string) # (קיב) תהילים, *פרק* א'
for i in matches:
  string = string.replace(i, '')

matches = re.findall('\(כתיב:.*\)' , string) # שׁוֹרְרָי (כתיב: הושר)
for i in matches:
  string = string.replace(i, '')

# after i removed things, now convert to text only

string = string.replace(':','') # replace all : with none
string = string.replace('ה\'','יהוה') # replace all ' with none

string = str(Hebrew(string).text_only())

list_perakim = string.split('\n\n')

for i in range(1,151):
  filename = './Prakim/Perek' + str(i) + '.txt'
  with open(filename, 'w', encoding='utf-8') as input_file:
    if i > 1:
      list_perakim[i] = '\n'.join(list_perakim[i].split('\n')[1:]) # remove the first line
    input_file.write(list_perakim[i])

output_file.write(string)



