import numpy as np
import pandas as pd


avg_ocean_depth = pd.Series({
                    'Arctic': 1205,
                    'Atlantic': 3646,
                    'Indian': 3741,
                    'Pacific': 4080,
                    'Southern': 3270
})

max_ocean_depth = pd.Series({
                    'Arctic': 5567,
                    'Atlantic': 8486,
                    'Indian': 7906,
                    'Pacific': 10803,
                    'Southern': 7075
})

ocean_depths = pd.DataFrame({
        'Avg': avg_ocean_depth,
        'Max': max_ocean_depth
})

print("Describe()")
print(ocean_depths.describe())
print("\n")

user_data = {'first_name': ['Sammy', 'Jesse', np.nan, 'Jamie'],
        'last_name': ['Shark', 'Octopus', np.nan, 'Mantis shrimp'],
        'online': [True, np.nan, False, True],
        'followers': [987, 432, 321, np.nan]}

df = pd.DataFrame(user_data, columns = ['first_name', 'last_name', 'online', 'followers'])
print("DF")
print(df)
print("\n")

print("Dropped")
df_drop_missing = df.dropna()
print(df_drop_missing)
print("\n")

df_fill = df.fillna(0)
print("Filled")
print(df_fill)
print("\n")
