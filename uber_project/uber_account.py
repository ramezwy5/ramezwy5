import pandas as pd
import glob
import os

# merging the files
joined_files = \
    os.path.join("C:\\Users\\Kaaper\\Documents\\Python_Scripts\\uber_project\\Augst\\w_7_11", "statement*.csv")
joined_list = glob.glob(joined_files)

# create dataframe concatenated week csv data files
df = pd.concat(map(pd.read_csv, joined_list), axis=0, ignore_index=True)
# add gas expenses fuel charge
df['Expenses Fuel Charge'][0] = int(input("enter gas expenses: "))
wgas = df['Expenses Fuel Charge'][0]
# convert data from str to int


def numeric_serrise(df, column):
    for i in range(len(df)):
            if type(df[column][i]) != float:
                df[column][i] = df[column][i].replace("$", "")
    df[column]=pd.to_numeric(df[column])
    # df[column] = df[column].astype(float)
    total = round(df[column].sum(), 2)
    return total


# total earn
total = numeric_serrise(df,'Total')
# print("weekly total : {}".format(total))  # Total sum return day_total

# toll refunds
toll = numeric_serrise(df, 'Refunds Toll')
# print("toll : {}".format(toll))

day_earn = round(total-(toll+wgas), 2)
maintane = round(day_earn * 0.25, 2)
dgross = round(day_earn - maintane, 2)
# credit payment is 75% of from gross
credit = round(dgross*0.75, 2)
net_gross = round(dgross-credit, 2)
# gross to earn ratio
ratio = round(dgross/total, 2)

print("week total earn: ${}".format(total))
print("Toll compensation: ${}".format(toll))
print("week net earn: ${}".format(day_earn))
print("25% maintenance: ${}".format(maintane))
print("weekly credit payment is: ${}\nnet gross per week is: ${}".format(credit, net_gross))
print("ratio of gross to earn: {}%".format(ratio*100))