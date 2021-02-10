import nltk
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
import os
import argparse
def TFouput(path_t, path_o, tokens, fdist):
    # Frequency
    with open(path_t,'w') as t:
        for f in fdist:
            t.write(str(f)+":"+str(fdist[str(f)]))
            t.write('\r')
    t.close()

    # Tokenize
    with open(path_o,'w') as q:
        for i in range(len(tokens)):
            q.write(str(tokens[i]))
            q.write('\r')
    q.close()

if __name__ == '__main__':


    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--corpus', default='reddit_sarcasm.txt',
                        help='path of the corpus file')
    parser.add_argument('--output', default='./output',
                        help='dir to output results')
    parser.add_argument('--wordonly', action='store_true',
                        help='tokens only include words')
    parser.add_argument('--exstop', action='store_true',
                        help='exclude stopwords')
    parser.add_argument('--stopwords',default='./stopwords.txt',
                        help='path to stopwords')
    parser.add_argument('--bigram', action='store_true',
                        help='output bigram or not')
    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)
    data=''
    f=open(args.corpus)
    line = f.readline()
    while line:
        data += line
        line = f.readline()
    f.close()

    token=[]
    bi_pair=[]
    fdist = FreqDist()
    bi_fdist = FreqDist()
    stop = []
    if args.exstop == True:
        sw = open(args.stopwords)
        st = sw.readline()
        while st:
            stop.append(st[:-1])
            st = sw.readline()
        sw.close()
    se = nltk.sent_tokenize(data)
    tokenizer = RegexpTokenizer(r'\b[a-zA-Z]+\b')
    for s in se:
        tok = tokenizer.tokenize(s) if args.wordonly == True else nltk.word_tokenize(s)
        temp=[]
        for wd in tok:
            if args.exstop == True and wd.lower() in stop :
                continue
            fdist[wd.lower()] += 1
            token.append(wd)
            temp.append(wd)
        bigram = nltk.bigrams(temp)
        bi_pair += bigram
    for bi in bi_pair:
        bi_fdist[str(bi)] += 1

    TFouput(os.path.join(args.output, 'token.txt'), os.path.join(args.output, 'output.txt'),
                token, fdist)
    if args.bigram == True:
        TFouput(os.path.join(args.output, 'token_bigram.txt'), os.path.join(args.output, 'output_bigram.txt'), bi_pair,
                bi_fdist)

