import pandas as pd

# Read leaderboard
df = pd.read_csv("leaderboard.csv")

# Convert to markdown table
table = df.to_markdown(index=False)

# Read README
with open("README.md", "r") as f:
    content = f.read()

# Replace section
start = content.find("## 🏆 Leaderboard")

new_content = content[:start] + "## 🏆 Leaderboard\n\n" + table

# Write back
with open("README.md", "w") as f:
    f.write(new_content)

print("README updated!")
