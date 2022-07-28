import string
import pandas as pd
import numpy as np
import logging
from string import ascii_lowercase

logging.getLogger().setLevel(logging.INFO)
'''ds = ['Physics','Maths','Chemistry']
#ds = pd.Series(ds,index=['Deals with objects','Deals with numbers','Deals with chemicals'],dtype='string')
ds = pd.Series(ds,index=pd.RangeIndex(0,3,1))
ds.name = 'My school subjects'
logging.info(ds)'''

'''actor_name = ['surya','Namik paul','Chris Hemsworth','mohan lal']
actor_age = [45,31,39,60]
actors = pd.Series(actor_age,index=actor_name,name='Actors')
#logging.info(actors)
#logging.info({name:age for name,age in zip(actor_name,actor_age)})
packed = zip(actor_name,actor_age)
logging.info(list(packed))'''

lower_case = list(ascii_lowercase)
lower_case = pd.Series(lower_case,index = list(range(26)))

logging.info(lower_case)