#final project
#need to do if python installed
#pip3 install matplotlib scipy
#pip3 install pandas
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stat

# For first test idk if we should drop Nans or not, 223388 rows vs 187308 rows is a good difference
og_df = pd.read_csv('mlb_elo.csv')

# Check the number of entries before cleaning
print(f"Number of entries before clean (rows): {og_df.shape[0]}")

# print(og_df.isnull().sum())

column_to_drop = 'playoff'
og_df = og_df.drop(columns=[column_to_drop])

# print(og_df.head())
# Dropping rows with NaN values in any row
og_df = og_df.dropna()

og_df.reset_index(drop=True, inplace=True)

# Check the number of entries after cleaning
print(f"Number of entries after clean (rows): {og_df.shape[0]}")


# print(og_df.info())
# print(og_df.head())
# print(og_df.dtypes)

# summary_stats = og_df.describe()
# print(summary_stats)
# missing_values = og_df.isnull().sum()
# print(missing_values)
# print(f"Number of entries (rows): {og_df.shape[0]}")
# print(f"Number of features (columns): {og_df.shape[1]}")

#####################################
# Null Hypothesis: The mean score of home teams (score1) is greater than or equal to the mean score of away teams (score2).
# Alternative Hypothesis: The mean score of home teams (score1) is less than the mean score of away teams (score2).
# Alpha Value 0.05

# Perform Chi-Squared to compare scores between home and away teams
table = pd.crosstab(og_df['score1'], og_df['score2'])
# Perform chi-squared test
_, p_value, _, _ = stat.chi2_contingency(table)
# Why am i getting p-value 0?
print(f"P-value: {p_value}")



