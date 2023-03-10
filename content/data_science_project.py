# -*- coding: utf-8 -*-
"""Data-Science project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-nA9SAWV1pwLLD97eoS6cd5Ug_cQ5nVh

**Can use this to share findings or test your data set work**
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np

"""# Filters the dataset
Ends up fixing the columns within the .xlsx formatting
"""

import pandas as pd
import altair as alt
from altair import Chart, X, Y, Color, Scale

names = ['Outcomes & Factors Rankings', 'Outcomes & Factors SubRankings', 'Additional Measure Data', 'Ranked Measure Data']

def filter_dataset(name):
  """Cleans up our dataset"""
  rank_data = pd.read_excel('/content/2022 County Health Rankings Data - v1 (1).xlsx', sheet_name=name, header=[0, 1])

  return rank_data

all_data_sets = []

for i in range(4):
  all_data_sets.append(filter_dataset(names[i]))

ranks = all_data_sets[0]
sub_ranks = all_data_sets[1]
additional_data = all_data_sets[2]
ranked_data = all_data_sets[3]

"""# Question 2
Trevor Smith
```
Does excessive drinking ratings lead to larger amounts of people having poor
mental health days?
```
"""

import pandas as pd
import altair as alt
from altair import Chart, X, Y, Color, Scale
from google.colab import drive
drive.mount('/content/drive')

names = ['Outcomes & Factors Rankings', 'Outcomes & Factors SubRankings', 'Additional Measure Data', 'Ranked Measure Data']

def filter_dataset(name):
  """Cleans up our dataset"""
  rank_data = pd.read_excel('/content/drive/MyDrive/Data Science/2022 County Health Rankings Data - v1.xlsx', sheet_name=name, header=[0, 1])

  return rank_data

all_data_sets = []

for i in range(4):
  all_data_sets.append(filter_dataset(names[i]))

ranks = all_data_sets[0]
sub_ranks = all_data_sets[1]
additional_data = all_data_sets[2]
ranked_data = all_data_sets[3]

excessive_drinking_data = ranked_data['Excessive drinking']['% Excessive Drinking']
excessive_drinking_data = list(excessive_drinking_data)

poor_mental_health = ranked_data['Poor mental health days']['Average Number of Mentally Unhealthy Days']
poor_mental_health = list(poor_mental_health)

correlation = pd.DataFrame({'Excessive Drinking': excessive_drinking_data, 'Poor Mental Health': poor_mental_health})

Chart(correlation).mark_circle().encode( x='Excessive Drinking', y='Poor Mental Health', color='Poor Mental Health').interactive()

# Which 5 States have the counties with lowest mental health days?
# South Dakota
# North Dakota
# Virginia
# Wyoming
# Hawaii

#--------------------------------------------------------------------

# The graph above shows that as poor mental health lowers, so does the amount
# of excessive Drinking


correlation['Excessive Drinking'].corr(correlation['Poor Mental Health'])

"""# Question 3
Mitchell Martin
"""

compressed_data

compressed_data['Difference in Percentage'] = compressed_data['% Drive Alone to Work'] - compressed_data['% Driving Deaths with Alcohol Involvement']

n = alt.Chart(compressed_data).mark_rect().encode(
    alt.X('% Driving Deaths with Alcohol Involvement:Q', bin=alt.Bin(maxbins=160)),
    alt.Y('% Drive Alone to Work:Q', bin=alt.Bin(maxbins=160)),
    alt.Color('Difference in Percentage:Q', scale=alt.Scale(scheme='greenblue'))
)
n

"""Our findings show that there isn't much of a correlation with alcohol related driving deaths with people that drive alone to work. 


*   The average is ranges between (8% - 45%) of people dying while drinking and driving with around (70% - 90%) of people driving alone. 


"""

top_findings_data = compressed_data.dropna()

top_findings_data.sort_values(by=["Difference in Percentage"], ascending=False, inplace=True)

top_findings_data = top_findings_data[abs(top_findings_data['Difference in Percentage']) <= 30]

top_findings_data

q = alt.Chart(top_findings_data).mark_rect().encode(
    alt.X('% Driving Deaths with Alcohol Involvement:Q', bin=alt.Bin(maxbins=160)),
    alt.Y('% Drive Alone to Work:Q', bin=alt.Bin(maxbins=160)),
    alt.Color('Difference in Percentage:Q', scale=alt.Scale(scheme='greenblue'))
)
q

"""Our findings of the counties that had a difference in percentage of less than 20%. 


```
The difference refering to 
- % of Driving Deaths with Alcohol Involvement
- % of Driving Alone to Work
```
shows that not many counties have a strong correlation between the two categories.



"""

compressed_data.groupby('States').mean()

"""# Question 4
Mitchell Martin

```
Do high physical inactivity rates found within the rankings tend to 
correlate with high adult obesity rates?
```
"""

import pandas as pd
import altair as alt
from altair import Chart, X, Y, Color, Scale

def remove_unnamed(df):
  """Solution found on https://stackoverflow.com/questions/40839609/rename-unnamed-multiindex-columns-in-pandas-dataframe"""
  for i, columns in enumerate(df.columns.levels):
    new_columns = columns.tolist()
    for j, row in enumerate(new_columns):
      if "Unnamed: " in row:
        new_columns[j] = ""
    if pd.__version__ < "0.21.0":
      df.columns.set_levels(new_columns, level=i, inplace=True)
    else:
      df = df.rename(columns=dict(zip(columns.tolist(), new_columns)),
                     level=i)
  return df

import pandas as pd

names = ['Outcomes & Factors Rankings', 'Outcomes & Factors SubRankings', 'Additional Measure Data', 'Ranked Measure Data']

def filter_dataset(name):
  """Cleans up our dataset"""
  rank_data = pd.read_excel('/content/2022 County Health Rankings Data - v1 (1).xlsx', sheet_name=name, header=[0, 1])

  return rank_data

all_data_sets = []

for i in range(4):
  all_data_sets.append(remove_unnamed(filter_dataset(names[i])))

ranks = all_data_sets[0]
sub_ranks = all_data_sets[1]
additional_data = all_data_sets[2]
ranked_data = all_data_sets[3]

inactive_data = ranked_data['Physical inactivity']['% Physically Inactive']
inactive_data = list(inactive_data)

obesity_data = ranked_data['Adult obesity']['% Adults with Obesity']
obesity_data = list(obesity_data)

correlation = pd.DataFrame({'Inactive rates': inactive_data, 'Obesity rates': obesity_data})

Chart(correlation).mark_circle().encode(
    x='Inactive rates',
    y='Obesity rates',
    color='Obesity rates'
)

"""The scatter plot shows that countries tend
to have obesity rates between 25% to 45% which
correlates with the inactivity rates containing 
approximately the same percentage. (20% - 45%)
"""

correlation['Inactive rates'].corr(correlation['Obesity rates'])

"""The correlation between both rates also shows that there is 
a correlation of nearly 80% between the two data sets.

#Question 5
Trevor Smith
```
What are the top 20 counties with the lowest high school completion rates 
grouped by each state and does this correlate to the number of teen births rates?
```
"""

import pandas as pd
import altair as alt
from altair import Chart, X, Y, Color, Scale
from google.colab import drive
drive.mount('/content/drive')

names = ['Outcomes & Factors Rankings', 'Outcomes & Factors SubRankings', 'Additional Measure Data', 'Ranked Measure Data']

def filter_dataset(name):
  """Cleans up our dataset"""
  rank_data = pd.read_excel('/content/drive/MyDrive/Data Science/2022 County Health Rankings Data - v1.xlsx', sheet_name=name, header=[0, 1])

  return rank_data

all_data_sets = []

for i in range(4):
  all_data_sets.append(filter_dataset(names[i]))

ranks = all_data_sets[0]
sub_ranks = all_data_sets[1]
additional_data = all_data_sets[2]
ranked_data = all_data_sets[3]

teen_birth_data = ranked_data['Teen births']['Teen Birth Rate']
teen_birth_data = list(teen_birth_data)

school_completed = ranked_data['High school completion']['% Completed High School']
school_completed = list(school_completed)

correlation = pd.DataFrame({'Birth rates': teen_birth_data, 'Completion rates': school_completed})

Chart(correlation).mark_circle().encode( x='Birth rates', y='Completion rates', color='Completion rates').interactive()

# Top 20 counties with the lowest high school completion rates, grouped by state:
# Texas: Kenedy, Presidio, Hudspeth, Starr, Maverick, Gaines, Culberson, Frio, Garza, La Salle, Moore, Zapata, Brooks, Hidalgo
# Ohio: Holmes
# Indiana: LaGrange
# Idaho: Clark
# Mississippi: Issaquena
# Kentucky: Clay
# Georgia: Atkinson

#Texas holds almost 3/4's of the lowest 20 Highschool completion States, at 14 out of 20

#------------------------------------------------------------------------------------------

# The graph above shows that as the High School Completion rate drops, the Teen Birth rate
# Slowly rises. There is a correlation of almost 70%.

correlation['Birth rates'].corr(correlation['Completion rates'])