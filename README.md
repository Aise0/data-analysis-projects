# Analysis of tweets about corona

This project includes the analysis of tweets from "202005171549_corona_tweets.csv" file.
The csv file is read into a Pandas Dataframe and perform the operations using Pandas.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

The original csv file can be found through this link: https://drive.google.com/file/d/1OT_iwB-5lysuX-tcN0ZlmZ78RhMbpQoJ/view?usp=sharing

### Prerequisites

What things you need to install the software and how to install them:

Python: https://realpython.com/installing-python

```
brew install python3
```

Additional: 
Not an requisite but the best IDE to run the code is Jupyter Notebook

To install Jupyter Notebook, go to https://jupyter.org/install


### Installing

To install pandas from PyPI:

```
pip install pandas
```

To install numpy:

```
pip install numpy
```

To install matplotlib:

```
pip install matplotlib
```

### Importing


Pandas:

```
import pandas as pd
```

Numpy:


```
import numpy as np
```

Counter:

```
from collections import Counter
```

Matplotlib:

```
import matplotlib.pyplot as plt
```

### Examples

Pandas:

```
f = pd.read_csv('202005171549_corona_tweets.csv')
```

Counter:

```
word_counter = Counter()
```

Matplotlib:

```
length_of_tweets.hist(bins=50) 
plt.title('Text lengths of tweets')
plt.xlabel('Number of tweets')
plt.ylabel('Length of tweets')
plt.show()
```

## Acknowledgments

* Done as an assignment for Computational Social Sciences (SOCI354) course at Koç University.
* Via Ali Hürriyetoglu's guidance and instructions.