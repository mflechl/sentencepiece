import math
import argparse

norm = True


def ToLogProb(voc):
  sum = 0.0;
  for ele in voc:
    sum += ele['cnt']

  logsum = math.log(sum)

  for ele in voc:
      if ele['cnt'] != 0:
        ele['cnt'] = math.log(ele['cnt']) - logsum

  return voc


#############################################################################

#txt_fname = 'hamlet.txt'
#voc_fname = 'no_input_voc.vocab'
#out_fname = 'vocab_with_freq.vocab'

parser = argparse.ArgumentParser()
parser.add_argument("-t", metavar="txt_fname", default='hamlet.txt')
parser.add_argument("-v", metavar="voc_fname", default='no_input_voc.vocab')
parser.add_argument("-o", metavar="out_fname", default='out.vocab')
parser.add_argument("--has_counts", action="store_true")

args = parser.parse_args()
txt_fname = args.t
voc_fname = args.v
out_fname = args.o
has_counts = args.has_counts

print(args)


with open(voc_fname) as f:
  if has_counts:
    voc = [ { 'cnt': int( line.split()[0] ), 'token': line.split()[1].replace('_', '▁') } for line in f ]
  else:
    voc = [ { 'token': line.split()[0] } for line in f ]
#    voc = [ line.split()[0] for line in f ]

if not has_counts:
  text = ''
  with open(txt_fname) as f:
    for line in f:
      if line.strip() == '': continue
      #        text += line.lower()
      text += line


  cnt = []
  total_count = 0
  for ele in voc:
    cnt1 = text.count(ele['token'].replace('▁',' '))
    if norm: cnt1 *= len(ele['token'])
    ele['cnt'] = cnt1
    total_count += cnt1

print(voc[0:5])
voc = ToLogProb( voc )

with open(out_fname, 'w') as out_f:
    for ele in voc:
        out_f.write( f'{ele["token"]}\t{ele["cnt"]}\n' )

#check = 0
#for n in voc: check += n['cnt']
#print(check, total_count)
