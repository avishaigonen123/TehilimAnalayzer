from hebrew import Hebrew
import re

res_file = open('res_file.txt', 'w', encoding='utf-8')

dict_acrostics = dict(zip(range(1,151),''))

def calc_acrostic(inx, data):
  res = ''
  for i in data.split('\n'):
    if len(i) <= inx:
      res += ' '    
    else:
      res += i[inx]
  return res


def simple_interface():

  inx = int(input('Please enter inx: '))
  perek = input('Please enter perek number: ')
  data = ''
  filename = './Prakim/Perek' + perek + '.txt'
  with open(filename, 'r', encoding='utf-8') as input_file:
    data = input_file.read()
    acrostics = calc_acrostic(inx, data.replace(' ', ''))

  print(f'Perek{perek}, inx is {inx}: {acrostics}\ndata: \n{data}')


def main():
  inx = 0

  for i in range(1,151):
    filename = './Prakim/Perek' + str(i) + '.txt'
    with open(filename, 'r', encoding='utf-8') as input_file:
      dict_acrostics[i] = calc_acrostic(inx, input_file.read().replace(' ', ''))

  for i in range(1,151):
    res_file.write(f'Perek{i}, inx is {inx}: {dict_acrostics[i]} \n')

if __name__ == '__main__':
  main()