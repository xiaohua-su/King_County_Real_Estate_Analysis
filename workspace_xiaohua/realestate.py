import pandas as pd
import numpy as np
import scipy.stats as stats

pd.set_option('display.float_format', lambda x: '%.10f' % x)

df = pd.read_csv('~/Documents/Flatiron/projects/phase2project/Phase2-Real--Estate/data/kc_house_data.csv')

#think that view might be important so we fill the nulls there for now

df_copy = df.copy()
df_copy['view'] = df_copy['view'].fillna(value = 'NO_RECORD')

'''is there a difference between those that have a view versus those that don't'''

summary_of_view = df_copy.groupby('view').mean()
'''from the df summary, we notice that there is a difference in price between price for those that are excellent
compared to those that have a view written as none. Further investigation will be performed to determine if this
difference is statistically significant'''

''' Subsetting the data into different views
 - number of rows: none = 19422, avg = 957, good = 508, fair = 330, excellent = 317, norecord = 17
 - likely need to convert this to a function of some kind if we can'''
df_average = df_copy[df_copy['view'] == 'AVERAGE']
df_excellent = df_copy[df_copy['view'] == 'EXCELLENT']
df_fair = df_copy[df_copy['view'] == 'FAIR']
df_good = df_copy[df_copy['view'] == 'GOOD']
df_none = df_copy[df_copy['view'] == 'NONE']
df_no_record = df_copy[df_copy['view'] == 'NO_RECORD']

fvalue, pvalue = stats.f_oneway(df_average['price'], df_excellent['price'], df_fair['price'],
                                df_good['price'] , df_none['price'])

#print(summary_of_view)
'''pvalue is small proving that there is a significant in pricing between these view. This test does not tell us which
view is significant and or if some of the views are not significant between each other. Ad-Hoc tests will need to be
performed to determine which views are.'''

' Is there a difference between grades'

grade_count = df_copy.grade.value_counts()
'''issue here that there are many different grade and some of them have very little that can skew the perception
#such as poor having 1, mansion having 13, low = 27, luxury having 87'''

summary_of_grade = df_copy.groupby('grade').mean()

#print(summary_of_grade.price)
#excluding the three mentioned above for now, further discussion required
df_10 = df_copy[df_copy['grade'] == '10 Very Good']
df_11 = df_copy[df_copy['grade'] == '11 Excellent']
df_12 = df_copy[df_copy['grade'] == '12 Luxury']
df_4 = df_copy[df_copy['grade'] == '4 Low']
df_5 = df_copy[df_copy['grade'] == '5 Fair']
df_6 = df_copy[df_copy['grade'] == '6 Low Average']
df_7 = df_copy[df_copy['grade'] == '7 Average']
df_8 = df_copy[df_copy['grade'] == '8 Good']
df_9 = df_copy[df_copy['grade'] == '9 Better']

f_value_grade, p_value_grade = stats.f_oneway(df_10['price'], df_11['price'], df_12['price'],
                                df_4['price'] , df_5['price'], df_6['price'], df_7['price'],df_8['price'],
                                              df_9['price'])

print(p_value_grade)
'''There is a significant difference in price betweeen grades but we don't know which one is significant.\
Further testing required to determine which is important'''