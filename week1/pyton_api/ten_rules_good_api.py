# Autor uczący się: Jarosław Krefft
# Data utworzenia: 08.05.2026
# Nazwa i wersja programu: ren_rules_good_api.py
# 1 - sza wersja kodu - programu który listuje 10 zasad dobrego API

import json
import os
from pathlib import Path
from rich.console import Console

BASE_DIR = Path(__file__).resolve().parent
json_path = BASE_DIR / "api_rules.json"

with open(json_path, "r" , encoding="utf-8") as plik:
    rules = json.load(plik)

console = Console() # wyczyszczenie konsoli
console.clear()

print("Jak tworzyć REST API 10 najważniejszych zasad. \n")

for rule in rules:
    print(rule["id"], " - ", rule["rule"])

print("\n")  
   


