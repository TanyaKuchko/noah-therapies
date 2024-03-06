import pandas as pd


patient_df = pd.read_csv('/Users/tanya_kuchko/Downloads/Patient_data1234.csv', encoding='latin1')
patient_df['symptoms'] = patient_df['symptoms'].astype(str)
patient_df['symptoms'] = patient_df['symptoms'].apply(lambda x: x.replace('[', ''))
patient_df['symptoms'] = patient_df['symptoms'].apply(lambda x: x.replace(']', ''))
patient_df['symptoms'] = patient_df['symptoms'].apply(lambda x: x.replace("'", ''))
new_columns = patient_df['symptoms'].str.split(',', expand=True)
column_names = ['symptom1', 'symptom2', 'symptom3', 'symptom4', 'symptom5', 'symptom6', 'symptom7']
new_columns.columns = column_names
patient_df[new_columns.columns] = new_columns

patient_df.drop(columns=['Unnamed: 0'], inplace=True)

patient_df['interests'] = patient_df['interests'].astype(str)
patient_df['interests'] = patient_df['interests'].apply(lambda x: x.replace('[', ''))
patient_df['interests'] = patient_df['interests'].apply(lambda x: x.replace(']', ''))
patient_df['interests'] = patient_df['interests'].apply(lambda x: x.replace("'", ''))
new_columns = patient_df['interests'].str.split(',', expand=True)
column_names = ['interest1', 'interest2', 'interest3', 'interest4', 'interest5', 'interest6', 'interest7', 'interest8']
new_columns.columns = column_names
patient_df[new_columns.columns] = new_columns

patient_df['healthGoals'] = patient_df['healthGoals'].astype(str)
patient_df['healthGoals'] = patient_df['healthGoals'].apply(lambda x: x.replace('[', ''))
patient_df['healthGoals'] = patient_df['healthGoals'].apply(lambda x: x.replace(']', ''))
patient_df['healthGoals'] = patient_df['healthGoals'].apply(lambda x: x.replace("'", ''))
new_columns = patient_df['healthGoals'].str.split(',', expand=True)
column_names = ['healthGoals1', 'healthGoals2', 'healthGoals3', 'healthGoals4', 'healthGoals5', 'healthGoals6']
new_columns.columns = column_names
patient_df[new_columns.columns] = new_columns

columns_list = ['ACNE_OR_SKIN_PROBLEMS', 'BLADDER_WEAKNESS', 'CONCENTRATION_PROBLEMS', 'BACK_PAIN', 'CRAMPS', 'DEPRESSIVE_MOODS', 'DIZZINESS_AND_CIRCULATORY_PROBLEMS', 'DRY_MUCOUS_MEMBRANES_OF_MOUTH', 'FATIGUE', 'FLATULENCE', 'HAIR_LOSS', 'HEADACHE_OR_MIGRAINE', 'HEAVY_MENSTRUAL_BLEEDING', 'HOT_FLASHES', 'JOINT_PAIN', 'MOOD_SWINGS', 'MUSCLE_OR_BONE_PAIN', 'NAUSEA_AND_VOMITING', 'OTHER', 'SHORTNESS_OF_BREATH', 'SLEEP_PROBLEMS', 'STOMACH_OR_DIGESTIVE_PROBLEMS', 'STRESS_NERVOUSNESS']
interests_list = ['BREATHING', 'DISEASE_INFORMATION', 'EXERCISE_AND_FITNESS', 'NATURAL_MEDICINE', 'NUTRITION', 'RELAXATION', 'SKIN_HEALTH', 'THERAPY_ORGANIZATION']
goals_list = ['ALLEVIATE_DISCOMFORT', 'INCREASE_PERFORMANCE', 'LIVE_LONGER', 'REDUCE_STRESS', 'REGENERATION_DETOX', 'THERAPY_SUPPORT']

for col_name in columns_list:
    new_col_name = col_name
    patient_df[new_col_name] = patient_df['symptoms'].str.contains(col_name).isin(columns_list).astype(int)
for col_name in interests_list:
    new_col_name = col_name
    patient_df[new_col_name] = patient_df['interests'].str.contains(col_name).isin(columns_list).astype(int)
for col_name in goals_list:
    new_col_name = col_name
    patient_df[new_col_name] = patient_df['healthGoals'].str.contains(col_name).isin(columns_list).astype(int)

patient_df.symptoms.fillna("", inplace=True)
patient_df.interests.fillna("", inplace=True)
patient_df.healthGoals.fillna("", inplace=True)

patient_df.symptoms = patient_df.symptoms.apply(lambda x: x.strip())
patient_df.interests = patient_df.interests.apply(lambda x: x.strip())
patient_df.healthGoals = patient_df.healthGoals.apply(lambda x: x.strip())

for idx, row in patient_df.iterrows():
    tmp = patient_df.loc[idx, "symptoms"].split(",")
    tmp_ = []
    for i in tmp:
        tmp_.append(i.strip())

    patient_df.loc[idx, "symptoms"] = ",".join(tmp_)

for idx, row in patient_df.iterrows():
    tmp = patient_df.loc[idx, "interests"].split(",")
    tmp_ = []
    for i in tmp:
        tmp_.append(i.strip())

    patient_df.loc[idx, "interests"] = ",".join(tmp_)

for idx, row in patient_df.iterrows():
    tmp = patient_df.loc[idx, "healthGoals"].split(",")
    tmp_ = []
    for i in tmp:
        tmp_.append(i.strip())

    patient_df.loc[idx, "healthGoals"] = ",".join(tmp_)

for idx, row in patient_df.iterrows():
    tmp = patient_df.loc[idx, "symptoms"].split(",")
    tmp_ = []
    for i in tmp:
        tmp_.append(i.strip())

    patient_df.loc[idx, "symptoms"] = ",".join(tmp_)

for idx, row in patient_df.iterrows():
    tmp = patient_df.loc[idx, "interests"].split(",")
    tmp_ = []
    for i in tmp:
        tmp_.append(i.strip())

    patient_df.loc[idx, "interests"] = ",".join(tmp_)

for idx, row in patient_df.iterrows():
    tmp = patient_df.loc[idx, "healthGoals"].split(",")
    tmp_ = []
    for i in tmp:
        tmp_.append(i.strip())

    patient_df.loc[idx, "healthGoals"] = ",".join(tmp_)

patient_df.interests[0].split(',')

patient_age = pd.read_csv('/Users/tanya_kuchko/Downloads/Patient_age.csv')
df_patients_merged = pd.merge(patient_df, patient_age, on=["patientId"], how="left")
new_columns = patient_df['healthWheels'].str.split(',', expand=True)
df_patients_merged[new_columns.columns] = new_columns
patient_df.drop(columns=['id'], inplace=True)
print(df_patients_merged.info())
df_patients_merged.to_csv('/Users/tanya_kuchko/Downloads/df.csv', index=False)
