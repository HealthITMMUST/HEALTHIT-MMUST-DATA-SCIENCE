import pandas as pd;

# DataFrames are designed for handling structured, tabular data with multiple variables, while Series are more suited for representing and manipulating single columns of data.

fifa21messy=pd.read_csv("./HEALTHIT-MMUST-DATA-SCIENCE/datasets/fifa21_raw_data.csv");

# shape of the data
# Overview of data and composition
# print(fifa21messy.shape,"\n")
# print(fifa21messy.dtypes,"\n")
# print(fifa21messy.head(5))

# Drop unneeded columns
# print(fifa21messy.drop(columns=['Name','photoUrl','playerUrl'],inplace=True))

# check for duplicates
# print(fifa21messy.duplicated().sum())

# drop duplicate
# print(fifa21messy.drop_duplicates())

# convert height and weight into numerical form
print(fifa21messy.dtypes[['Height','Weight']])

print(fifa21messy[['Height','Weight']])

def hwConvert(x):

    if x.endswith('lbs') == True:
        x = x.replace("lbs","")
        a = str(round(int(x)*.453592))
        return a + 'kg'
    else:
        x = x.replace("\'", " ").replace("\"", "").split()
        a = int(x[0])*12 + int(x[1])
        fin = str(round(a*2.54)) + 'cm'
        return fin

# print numerical values of height, weight
fifa21messy['Weight'] = fifa21messy['Weight'].map(hwConvert)
fifa21messy['Height'] = fifa21messy['Height'].map(hwConvert)
print(fifa21messy[['Height','Weight']])


# print(hwConvert(f"56'11"""))
# print(fifa21messy.dtypes[['Height','Weight']])

# print(fifa21messy[['Height','Weight']])