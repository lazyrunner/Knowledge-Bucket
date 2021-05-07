import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen

# create the url
url = "https://www.moneycontrol.com/financials/coalindia/cash-flowVI/CI11/"

suffix_count = 1
tag = ""

final_df = pd.DataFrame()

while True:

    # create the url
    final_url = url + str(suffix_count) + "#CI11"

    # fetch the url
    fetched_url = urlopen(final_url).read()
    soup = BeautifulSoup(fetched_url, 'lxml')

    # check if the tag is not available
    tags = soup.find_all(attrs={'class':'mctable1'})

    if tags.__len__() == 0:
        break

    table = soup.find('table', attrs={'class':'mctable1'})
    sheet_df = pd.read_html(str(table))[0]

    # remote the last column
    sheet_df = sheet_df.iloc[:, :-1]

    # make the first column an index
    sheet_df = sheet_df.set_index(0)

    # make the first row as header of the data frame
    new_header = sheet_df.iloc[0]
    sheet_df = sheet_df[1:]
    sheet_df.columns = new_header

    #get the list of indices
    idx = sheet_df.index

    # drop the first row
    sheet_df.drop(index=idx[0], inplace=True)

    final_df = pd.concat([final_df, sheet_df], axis=1)

    final_url = ""
    suffix_count += 1

print(final_df)



