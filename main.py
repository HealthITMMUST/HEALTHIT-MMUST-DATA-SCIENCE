import pandas as pd
import matplotlib.pyplot as plt

# reading the csv file
data_frame = pd.read_csv("data_science_salaries.csv")

# reading the tp five lines
first_five_lines = data_frame.head(10)
# print(first_five_lines)

last_five_lines = data_frame.tail(5)
# print(last_five_lines)

# describing the data 
data_description = data_frame.describe()
# print(data_description)

# reading elements of a single column
column_1 = data_frame["job_title"][0: 28]
# print(column_1)

# counting the elements of a single column
count = data_frame["company_size"].value_counts()
# print(count)

# manipulating the data 
salary = data_frame["salary"]
salary_in_usd = data_frame["salary_in_usd"]
data_frame["Total"] = salary + salary_in_usd
# data_frame.to_csv('output.csv', index=False)


# iloc integer location 

new_data_frame = data_frame.iloc[0: 15]
new_data_frame.to_csv('output.csv', index=False)

new_data_frame.plot(kind='bar',
        x="job_title",
        y="salary",
        color='green')

# to plot a graph
plt.show()
