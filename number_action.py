import pandas as pd


matomo = pd.read_csv('/Users/tanya_kuchko/Downloads/Number_action.csv', low_memory=False, thousands=",")

res_dfs = []
for i in range(50):
    action_final_field = f"ACTION {i} - Event_final"
    df = matomo[["userId", action_final_field]].copy()
    df.dropna(inplace=True)
    df["i"] = i
    df.rename(columns={"userId": "user_id", action_final_field: "action_final"}, inplace=True)
    res_dfs.append(df)
    # print(df, "1" * 50)

flatten_df = pd.concat(res_dfs)

res_df = flatten_df.groupby(["user_id", "action_final"]).first()

print(res_df, "1" * 50)

res_df.to_csv('/Users/tanya_kuchko/Downloads/Number_action111.csv')
