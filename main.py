import pandas as pd
from msilib.schema import tables
import requests
from bs4 import BeautifulSoup
#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>
# we can see how many tables were found by checking the length of the tables list
print(len(tables))
# to find most densly populated countries
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
print(tables[table_index].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data
population_data=pd.read_html(str(tables[5]), flavor='bs4')

population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0] #The function read_html always returns a list of DataFrames so we must pick the one we want out of the list

print(population_data_read_html)
dataframe_list = pd.read_html(url, flavor='bs4')
print(dataframe_list[5])

