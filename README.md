# easypwd
Some password utils.

Codes implemented in Python will not use external packages if possible.
curver.py etc. have to import matplotlib.
## INDEX

- compare plaintext passwords line by line: **plainpwdcmp**
- get training set and testing set from a corpus: **split2.py**
- sample some passwords from a corpus: **samp.py**
- draw guess-crack figure: **gutify.py & curver.py**
- remove unwanted passwords: **cleaning.py**
- get min_auto of a password dataset: **minrank.py**
- remove passwords in training set and testing set: **havemenot.py**
- remove unwanted passwords from result set: **re2cracked.py**
- convert format of output from hashcat: **hashkitty.py**
- convert format of output from LSTM: **lstm.py**
- convert format of output from Monte Carlo 15 paper: **mc15conv.py**
- count frequencies of passwords, characters, or segments split by splitter: **freq.py**


## 1. plainpwdcmp

Compare plaintext passwords with specified targets

### usage
- -i: guesses file, one password per line, or (password, probability) per line
- -t: passwords to be cracked in plaintext, one password per line
- -o: results will be saved in this file
- -p: guesses file in format of (password, probability), bool
- -s: splitter in results file, "\t" by default
- -d: delim in guesses file, "\t" by default

### outputs
outputs are organized as follows:

pwd | prob(optional) | appearance | guess_number | cracked_num | cracked_ratio

## 2. split2.py

Split dataset into training set and testing set.

### usage
- -c: corpus to be parsed
- -s: training set path to be saved
- -t: testing set path to be saved
- -a: training set takes a / (a + b) percent
- -b: testing set takes b / (a + b) percent
- -l: passwords whose length being less than this will be ignored
- -u: passwords whose length being greater than this will be ignored.

### outputs
Removed invalid passwords (unprintable ASCII, too short length, etc.) will be saved if any.

## 3. gutify.py

### usage

The usage of gutify is to some extent a long story.

**Required**
- -f: Guess number and cracked number stored here
- -s: Save results here
- -t: Testing set will be used to obtain its size

**Optional for -f**
- --gc-split: How to split items of a line in guess number and cracked number file
- --idx-guess: guess number is at idx-guess, start from 0
- --idx-pwd: password is at idx-pwd, start from 0
- --need-sort: need to sort the data in the file

**Optional for line style**
- --upper: Max guess number
- --lower: Min guess number
- --color: Color of the line
- --line-style: solid, dash, dot, or dot_dash
- --marker: the marker on the line
- --line-width: the width of the line

**Optional for showing text at rightmost as a label**
- --show-text: show text or not
- --text-x: x axis position
- --text-y: y axis position
- --text-fontsize: fontsize

**Option for updating arguments**
- --force-update: re-read the files. if not specify this flag, read data from `-s` and ignore `--lower`, `--upper`


### outputs

A json file contains following items:
- label
- total number of passwords in test set, to calc the crack ratio
- color of this curve
- marker of points of curve
- line_width
_ line_style, solid or other
- guesses_list
_ cracked_list

## 4. curver.py

### usage

**Required**
- -f: json files generated by gutify.py
- -s: save the picture here, should be a path can be accessed
**Optional for saved file**
- --suffix: can be .pdf or .png

**Optional for label**
- -x: what does x axis mean
- -y: what does y axis mean
- --xlabel-weight: normal, bold
- --ylabel-weight: normal, bold
- --xlabel-size: font size of x label
- --ylabel-size: font size of y label

**Optional for axis**
- --xlim-low: x value less than this will not be displayed
- --xlim-high: x value larger than this will not be displayed
- --ylim-low: y value less than this will not be displayed
- --ylim-high: y value larger than this will not be displayed
- --xticks-val: ticks for x axis
- --xticks-text: text for x axis, may use $10^{2}$ to represent 100
- --yticks-val: ticks for y axis
- --yticks-val: text for y axis
- --tick-size: font size of ticks

**Optional for legend**
- --legend-loc: where you put the legend
- --legend-fontsize: font size of legend
- --legend-handle-length: length of legend handle, i.e., figure corresponding to text in legend

**Optional for figure**
- --xscale: linear, log, symlog, logit
- --yscale: same with xscale
- --tight: tight layout of figure

**Optional for vlines**
- --vlines: x value for vlines
- --vline-width: line width for vlines
- --vline-color: colors for vlines
- --vline-style: solid, dash, dot, dot_dash for vlines
- --vline-label: labels for vlines. set it to empty if you dont need

**Optional for grid**
- --hide-grid: hide grid
- --grid-linestyle: {solid,dash,dot_dash,dot}
- --no-boarder [{left,bottom,top,right} ]

This is a relatively easy utils to draw curves.

If you want some additional functions, rewrite it.

### outputs
A picture

## 5. cleaning.py
filter valid passwords from a dataset.

### usage
- -d: a dataset, one password per line
- -o: output, save filtered passwords here
- -p: RegEx to filter valid passwords

### output
Filtered passwords, a password per line.

## 6. minrank.py
Min_auto from existing guess-number-and-cracked-number results.

### usage
- -t: testing set
- -m: scored results for the testing set
- -s: save Min_auto here
- --split: how to split a line in scored results

### output
Min_auto

## 7. hashkitty.py
Convert pwd:guess number file generated 
by hashcat debug mode to my format.

### usage
- -r: hashcat result file, format plainpwd:crack_pos
- -t: testing set for hashcat result
- -s: save converted result here

### output
hashcat result in my format


## 8. freq.py

Count frequencies of password dataset.

### usage
- -f: password file
- -s: save frequencies
- --splitter: `whole` for passwords, `chr` for characters, splitter for segments
- --start: the index of the first element
- --step: index of the next element = current index + step
- --sample: sample n passwords to count frequenices
- --end: `\n` or `\r\n`, specify the end of a line in saved file

