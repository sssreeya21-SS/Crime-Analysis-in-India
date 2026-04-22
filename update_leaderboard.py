import pandas as pd
import os
from sklearn.metrics import accuracy_score, f1_score

# Load ground truth
gt = pd.read_csv("data/ground_truth.csv")

results = []

# Read all submissions
for file in os.listdir("submissions"):
    if file.endswith(".csv"):
        team_name = file.replace(".csv", "")
        pred = pd.read_csv(f"submissions/{file}")

        # Merge
        df = pd.merge(gt, pred, on="id", suffixes=("_true", "_pred"))

        # Metrics
        acc = accuracy_score(df["label_true"], df["label_pred"])
        f1 = f1_score(df["label_true"], df["label_pred"], average="weighted")

        results.append({
            "Team": team_name,
            "Accuracy": round(acc * 100, 2),
            "F1": round(f1, 4)
        })

# Sort
results = sorted(results, key=lambda x: x["Accuracy"], reverse=True)

# Markdown table
table = "## 🏆 Leaderboard\n\n"
table += "| Rank | Team | Accuracy | F1 Score |\n"
table += "|------|------|----------|----------|\n"

for i, r in enumerate(results):
    medal = ["🥇", "🥈", "🥉"]
    rank_icon = medal[i] if i < 3 else str(i+1)
    table += f"| {rank_icon} | {r['Team']} | {r['Accuracy']}% | {r['F1']} |\n"

# Update README
with open("README.md", "r") as f:
    content = f.read()

start = content.find("## 🏆 Leaderboard")
if start == -1:
    new_content = content + "\n\n" + table
else:
    end = content.find("##", start + 1)
    if end == -1:
        end = len(content)
    new_content = content[:start] + table + content[end:]

with open("README.md", "w") as f:
    f.write(new_content)

print("Leaderboard updated!")
