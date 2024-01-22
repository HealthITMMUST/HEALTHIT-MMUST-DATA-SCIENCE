import pandas as pd

fifa21messy=pd.read_csv("./HEALTHIT-MMUST-DATA-SCIENCE/datasets/fifa21_raw_data.csv");

# # Remove the unnecessary newline characters from all columns that have them.
# # check columns with new char "\n"

fifa21messy.columns[fifa21messy.astype('str').apply(lambda col:col.str.contains('\\n').any())]

print(fifa21messy)

# # Remove the unnecessary newline
fifa21messy["hits"]=fifa21messy.Hits.str.replace('\n','',regex=False)
print(fifa21messy)


# lis = [ 1, 2, 4]

# numbers = list(map(lambda x : x+1, lis))
# print(numbers)