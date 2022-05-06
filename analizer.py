import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions"), sep="\n")

link = input("Please enter your product code: ")

opinions = pd.read_json(f"opinions/{link}.json")
print(opinions)