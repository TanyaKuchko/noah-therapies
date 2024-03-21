import pandas as pd


# matomo = pd.read_csv('/Users/tanya_kuchko/Downloads/MATOMO_FINAL.csv', low_memory=False, thousands=",")
# # matomo.set_index("idVisit", inplace=True)
#
# res_dfs = []
# for i in range(50):
#     event_action_field = f"ACTION {i} - Event Action"
#     duration_field = f"ACTION{i}time_duration(sec)"
#     userId = 'userId'
#     df = matomo[[userId, event_action_field, duration_field]].copy()
#     df.rename(columns={userId: "user", event_action_field: "event_action", duration_field: "duration"}, inplace=True)
#     res_dfs.append(df)
#
#
#
# flatten_df = pd.concat(res_dfs)  # drop index?
# # flatten_df = flatten_df.reset_index(drop=True)
# filtered_flatten_df = flatten_df.loc[flatten_df['duration'] > 10]
# print(filtered_flatten_df)
#
#
# def calculate(x):
#     res = {
#         "clicks_count": x["event_action"].count(),
#         "duration_sum": x["duration"].sum(),
#     }
#     return pd.Series(res, index=res.keys())
#
# filtered_flatten_df.to_csv('/Users/tanya_kuchko/Downloads/Articles111.csv')
#
# res_df = filtered_flatten_df.groupby(["user", "event_action"])[["event_action", "duration"]].apply(calculate)
# print(res_df.sort_values(by="duration_sum", ascending=False), "2" * 50)
# res_df.to_csv('/Users/tanya_kuchko/Downloads/Articles.csv')

# _____________________________________________________________________________________________________
# matomo = pd.read_csv('/Users/tanya_kuchko/Downloads/MATOMO_patients_merged.csv', low_memory=False, thousands=",")
# res_dfs = []
# for i in range(50):
#     event_action_field = f"ACTION {i} - Event Action"
#     duration_field = f"ACTION{i}time_duration(sec)"
#     action = f"ACTION {i} - Type"
#     # date = f"ACTION {i} - Date & Time"
#     age = 'age'
#     # basicCondition = 'basicCondition'
#     df = matomo[[action, age, event_action_field, duration_field]].copy()
#     df.rename(columns={action: "action", age: "age", event_action_field: "event_action", duration_field: "duration"}, inplace=True)
#     res_dfs.append(df)
#
# flatten_df = pd.concat(res_dfs)  # drop index?
# # flatten_df = flatten_df.reset_index(drop=True)
# filtered_flatten_df = flatten_df.loc[flatten_df['duration'] > 1]
# filtered_flatten_df1 = filtered_flatten_df.loc[filtered_flatten_df['action'] == 'event']
# filtered_flatten_df2 = filtered_flatten_df1[filtered_flatten_df1['age'].notna()]
# filtered_flatten_df2 = filtered_flatten_df2.copy()
# # filtered_flatten_df['date'] = pd.to_datetime(filtered_flatten_df['date'], format='%d/%m/%Y %H:%M:%S')
# # filtered_flatten_df.loc[:, 'date'] = filtered_flatten_df['date'].dt.date
# print(filtered_flatten_df2)
#
#
# def find_age(age):
#     if age < 25:
#         return "18 - 24"
#     elif age >= 25 and age < 35:
#         return "25 - 34"
#     elif age >= 35 and age <45:
#         return "35 - 44"
#     elif age >= 45 and age <55:
#         return "45 - 55"
#     else:
#         return "55+"
#
#
# filtered_flatten_df2['age_grad'] = filtered_flatten_df2['age'].apply(find_age)
#
#
#
# def calculate(x):
#     res = {
#         "clicks_count": x["event_action"].count(),
#         "duration_sum": x["duration"].sum(),
#     }
#     return pd.Series(res, index=res.keys())
#
# filtered_flatten_df2.to_csv('/Users/tanya_kuchko/Downloads/Articles111.csv')
#
# res_df = filtered_flatten_df2.groupby("event_action")[["event_action", "duration"]].apply(calculate)
# print(res_df.sort_values(by="duration_sum", ascending=False), "2" * 50)
# res_df.to_csv('/Users/tanya_kuchko/Downloads/Articles.csv')

# # _____________________________________________________________________________________________________
# matomo = pd.read_csv('/Users/tanya_kuchko/Downloads/MATOMO_PATIENTS.csv', low_memory=False, thousands=",")
# res_dfs = []
# for i in range(48):
#     event_action_field = f"ACTION {i} - Event Action"
#     duration_field = f"ACTION{i}time_duration(sec)"
#     # date = f"ACTION {i} - Date & Time"
#     userId = 'userId'
#     df = matomo[[userId, event_action_field, duration_field]].copy()
#     df.rename(columns={userId: "userId", event_action_field: "event_action", duration_field: "duration"}, inplace=True)
#     res_dfs.append(df)
#
# flatten_df = pd.concat(res_dfs)  # drop index?
# flatten_df = flatten_df.reset_index(drop=True)
# filtered_flatten_df = flatten_df.loc[flatten_df['duration'] > 10]
# # filtered_flatten_df = filtered_flatten_df.copy()
# # filtered_flatten_df['date'] = pd.to_datetime(filtered_flatten_df['date'], format='%d/%m/%Y %H:%M:%S')
# # filtered_flatten_df.loc[:, 'date'] = filtered_flatten_df['date'].dt.date
# print(filtered_flatten_df)
#
#
# def calculate(x):
#     res = {
#         "clicks_count": x["event_action"].count(),
#         "duration_sum": x["duration"].sum(),
#     }
#     return pd.Series(res, index=res.keys())
#
# filtered_flatten_df.to_csv('/Users/tanya_kuchko/Downloads/Articles111.csv')
#
# res_df = filtered_flatten_df.groupby("event_action")[["event_action", "duration"]].apply(calculate)
# print(res_df.sort_values(by="duration_sum", ascending=False), "2" * 50)
# res_df.to_csv('/Users/tanya_kuchko/Downloads/Articles.csv')
# ------------------------------------------------------------------------------------------------
matomo = pd.read_csv('/Users/tanya_kuchko/Downloads/Number_action.csv', low_memory=False, thousands=",")
res_dfs = []
for i in range(50):
    action_final_field = f"ACTION {i} - Event_final"
    # event_action_field = f"ACTION {i} - Event Action"
    duration_field = f"ACTION{i}time_duration(sec)"
    action = f"ACTION {i} - Type"
    # date = f"ACTION {i} - Date & Time"
    user = 'userId'
    # age = 'age'
    # basicCondition = 'basicCondition'
    df = matomo[[user, action, action_final_field, duration_field]].copy()
    df["i"] = i
    df.rename(columns={user: "user", action: "action", action_final_field: "event_action", duration_field: "duration"}, inplace=True)
    res_dfs.append(df)

flatten_df = pd.concat(res_dfs)  # drop index?
# flatten_df = flatten_df.reset_index(drop=True)
# filtered_flatten_df = flatten_df.loc[flatten_df['duration'] > 1]
filtered_flatten_df1 = flatten_df.loc[flatten_df['action'] == 'event'].copy()
# filtered_flatten_df2 = filtered_flatten_df1[filtered_flatten_df1['age'].notna()]
# filtered_flatten_df['date'] = pd.to_datetime(filtered_flatten_df['date'], format='%d/%m/%Y %H:%M:%S')
# filtered_flatten_df.loc[:, 'date'] = filtered_flatten_df['date'].dt.date
print(filtered_flatten_df1)


def calculate(x):
    res = {
        "clicks_count": x["event_action"].count(),
        "duration_sum": x["duration"].sum(),
    }
    return pd.Series(res, index=res.keys())

filtered_flatten_df1.to_csv('/Users/tanya_kuchko/Downloads/Articles111.csv')
