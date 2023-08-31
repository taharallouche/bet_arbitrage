from selenium import webdriver
from selenium.webdriver.common.by import By
import json


url = "https://www.coteur.com/comparateur-de-cotes"
with webdriver.Chrome() as driver:
    driver.get(url)
    driver.implicitly_wait(5)

    table = driver.find_element(By.TAG_NAME, "table")

    rows = table.find_elements(By.TAG_NAME, "tr")

    matches_odds = {}

    for row in rows:
        match_name = row.find_element(By.CSS_SELECTOR, "[class*=Rencontre]")
        match_name = match_name.text
        odds_divs = row.find_elements(By.CLASS_NAME, "odds")

        matches_odds[match_name] = {
            "odds": [div.text for div in odds_divs],
            "arbitrage": row.text.split("\n")[-1],
        }

    with open("odds.json", "w") as f:
        json.dump(matches_odds, f)
