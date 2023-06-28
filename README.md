# SentencePiece

Forked from Google's [![sentencepiece](https://github.com/google/sentencepiece)] repository
Modified version to allow input seed vocabularies for unigram LM-based subword models

# Build and install

Note that this requires root access (via sudo) and a recent version of cmake installed.

```
  git clone https://github.com/mflechl/sentencepiece.git
  cd sentencepiece
  mkdir build
  cd build
  cmake ..
  make -j              # optional: make -j [nproc]
  sudo make install
```

# Run

## Standard sentencepiece use case

```
  cd sentencepiece
  mkdir run
  cd run
  wget https://gist.githubusercontent.com/provpup/2fc41686eab7400b796b/raw/b575bd01a58494dfddc1d6429ef0167e709abf9b/hamlet.txt
  spm_train --input=hamlet.txt --model_prefix test1 --vocab_size=1024 --character_coverage=1.0 --model_type=unigram &> log.txt
```

## With input vocabulary and subword frequencies

this assumes an input.subwords file with two columns, "frequency" "subword", e.g.
```
2093877 i
1712464 a
1528353 o
1308300 t_
```

```
  cd sentencepiece
  mkdir run
  cd run
  f=input.subwords
  python add_freq.py -v $f  -o $f.vocab --has_counts
  ln -s $f.vocab input.vocab
  ./run.sh corpus.txt subword_$f [desired final vocab size]
```


## With input vocabulary list
this assumes an input.subwords file with a list of subwords, e.g.
```
i
a
o
t_
```
and a corpus.txt file with the text corpus in plain format

```
  cd sentencepiece
  mkdir run
  cd run
  f=input.subwords
  python add_freq.py -v $f  -o $f.vocab -t corpus.txt
  ln -s $f.vocab input.vocab
  ./run.sh corpus.txt subword_$f [desired final vocab size]
```

When setting the total vocab size, consider also the special tokens (in this case, defined in user_defined_symbols_simple.txt)
