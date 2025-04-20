#MapPlot.py
#Name: Fatima Davila
#Date:4/20
#Assignment:lab 10

import coffee
import pandas
import matplotlib.pyplot as plt 

coffee = coffee.get_coffee()

#print(coffee[0]["Data"]["Scores"]["Total"])
years = []
scores = []
for bean in coffee:
    year = bean["Year"]
    score = bean["Data"]["Scores"]["Total"]
    if score != 0:
    #print(bean["Year"])
        years.append(year)
        scores.append(score)
    print(year, score)
print(years)
df = pandas.DataFrame({"Year": years, 
                        "Score": scores})
print(df)
#df.plot(kind = 'scatter', x = 'year', y = 'score')
plt.plot(years, scores, 'ro')
plt.savefig("output")

