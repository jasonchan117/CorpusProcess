# NLP assignment 1 Part 1: Corpus processing  

This is part1 implementation in the assignment of CSI5386[W] Natural Language Processing 2021"[
Corpus analysis and word embeddings](http://www.site.uottawa.ca/~diana/csi5386/A1_2021/A1_2021.htm)" .

## Requirements
- Python 3.7
- nltk 3.5


## Output tokenization results and its frequency
In below explaination, I will use `./reddit_sarcasm.txt` for example.

### 1. Output output.txt and token.txt
- **Execution**: Process the corpus by below command.
    ```bash
    python process.py --corpus ./reddit_sarcasm.txt --output output/all
    ```
    - `--corpus` telling the path to the text.
    - `--output` telling the path to the output directory for the results.

### 2. Output output.txt and token.txt with word only
- **Execution**: Process the corpus by below command.
    ```bash
    python process.py --corpus ./reddit_sarcasm.txt --output output/wordonly --wordonly
    ```
    - `--wordonly` telling the program to extract word 


### 3. Exclude stopwords
- **Execution**: Process the corpus by below command.
    ```bash
    python process.py --corpus ./reddit_sarcasm.txt --output output/wordonly --wordonly --exstop --stopwords ./stopwords.txt
    ```
    - `--exstop` telling the program to exclude stop word
    - `--stopwords` telling the program the path of stop word list
         
### 4. Compute bigram and output
- **Execution**: Process the corpus by below command.
    ```bash
    python process.py --corpus ./reddit_sarcasm.txt --output output/wordonly --wordonly --exstop --stopwords ./stopwords.txt --bigram
    ```
    - `--bigram` telling the program to output bigram result

### 5. Compute diversity
- **Execution**: Process the corpus by below command.
    ```bash
    python diversity.py --tokens output/all/output.txt --types output/all/token.txt
    ```
    - `--tokens` telling the program to the path of output file of tokenization
    - `--types` telling the program the path of corresponding frequency file
   