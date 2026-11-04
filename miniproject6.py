import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("login_attempts.csv")
df["percent"] = ((df["failed"]/df["attempts"])*100).round(2)   
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

print(df[df["status"] != "OK"])

grouped = df.groupby("status")
print(grouped["status"].value_counts())

df.to_csv("login_report.csv", index=False)

df["status"].value_counts().plot(kind="bar")
plt.title('status')
plt.savefig('status_counts.png')


print(df)

