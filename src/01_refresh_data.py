import pandas as pd

from twitter_data import tweets_get
from helpers import print_break, get_project_global_variables

print_break("Refreshing Twitter Data")

start_date = get_project_global_variables()["start_date"]
users = get_project_global_variables()["twitter_handles"]
df_path_raw = get_project_global_variables()["df_path_raw"]

df = pd.DataFrame()
for user in users:
    df_temp = tweets_get(
        user_name=user, num=200, start_date=start_date
    )
    df_temp['handle'] = user
    df = pd.concat([df, df_temp], sort=False)

print("\nSummary of tweets:")
print(f" - total number of tweets: {df.shape[0]}")
print(f" - start date: {min(df['date'])}")
print(f" - end date: {max(df['date'])}")
print("\n Tweet count by user:")
print(df['handle'].value_counts())

df.to_csv(df_path_raw, index=False)
