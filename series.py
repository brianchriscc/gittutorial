from string import ascii_lowercase
import numpy as np
import pandas as pd

a = list(ascii_lowercase)
a = pd.Series(a,index = range(26))
print(a)
