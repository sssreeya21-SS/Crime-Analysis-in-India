import pandas as pd

df = pd.read_csv("leaderboard.csv")

# sort highest accuracy first
df = df.sort_values(by="Accuracy", ascending=False)

df.to_csv("leaderboard.csv", index=False)

print("Leaderboard sorted!")
