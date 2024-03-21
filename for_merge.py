import pandas as pd


patients = pd.read_csv('/Users/tanya_kuchko/Downloads/Patients_final.csv')
matomo = pd.read_csv('/Users/tanya_kuchko/Downloads/MATOMO_final.csv', low_memory=False, thousands=",")
df_patients_merged = pd.merge(patients, matomo, on=["userId"], how="left")
df_patients_merged.to_csv('/Users/tanya_kuchko/Downloads/Patients_matomo.csv', index=False)
print(df_patients_merged)

df_matomo_merged = pd.merge(matomo, patients, on=["userId"], how="left")
df_matomo_merged.to_csv('/Users/tanya_kuchko/Downloads/MATOMO_patients_merged.csv', index=False)
print(matomo.head(10))

