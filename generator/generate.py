import csv
import random
import os

mountains = [
    ["Everest", "Nepal", 8848, "hard"],
    ["K2", "Pakistan", 8611, "hard"],
    ["Kangchenjunga", "Nepal", 8586, "hard"],
    ["Lhotse", "Nepal", 8516, "hard"],
    ["Makalu", "Nepal", 8485, "hard"],
    ["Mont Blanc", "France", 4809, "medium"],
    ["Elbrus", "Russia", 5642, "medium"],
    ["Denali", "USA", 6190, "hard"],
    ["Aconcagua", "Argentina", 6961, "medium"],
    ["Kilimanjaro", "Tanzania", 5895, "easy"]
]

os.makedirs("/data", exist_ok=True)

with open("/data/data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "country", "height_m", "difficulty"])

    for i in range(50):
        mountain = random.choice(mountains)
        writer.writerow(mountain)

print("data.csv created")