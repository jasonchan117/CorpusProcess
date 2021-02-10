import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--tokens', required=True,
                    help='path of the output file')
parser.add_argument('--types', required=True,
                    help='path of the tokens file')
args = parser.parse_args()

count1 = len(open(args.tokens,'r').readlines())
count2 = len(open(args.types,'r').readlines())

print(float(count2/count1))