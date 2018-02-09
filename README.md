# Introduction
The script `donation-analytics.py`  is developed to analyze the contributions from repeat donors and donation amount in a given percentile.

# Input files
`percentile.txt`,  holds a single value -- (1-100).
`itcont.txt`, has a line for each campaign contribution that was made on a particular date from a donor.

# Output files
`repeat_donors.txt`, contain the same number of lines or records as the input data file.


# Run the script

Although the script can be run in native python environment on most systems ( Windows, Linux, Mac)  without installing other dependencies. While, all the dependent packages can be installed on python2.7 or python 3.5 via :

```
pip install numpy, math, datetime, os, sys
```
then cd to the default dictionary and run

```
./run.sh 
```
The output file `repeat-donors.txt` should be stored in the folder `output`.
