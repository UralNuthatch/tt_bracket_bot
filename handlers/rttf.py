from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# добавление опций
def get_options():
    options = webdriver.ChromeOptions()
    # частичная загрузка, не дожидаясь полной
    options.page_load_strategy = "eager"
    # Set cache size to 1 byte
    options.add_argument("--disk-cache-size=1")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    # не показывать работу браузера
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    )
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("useAutomationExtension", False)
    return options


def get_rttf_player(driver: webdriver.Chrome, name: str, old_rating: str):
    driver.get(f"https://rttf.ru/players/?cities[]=r59&name={name}")
    wait = WebDriverWait(driver, 10, 1)
    RTTF_LOCATOR = ("xpath", "//table//dfn")
    RTTF = wait.until(EC.visibility_of_all_elements_located(RTTF_LOCATOR))
    if len(RTTF) == 1:
        return None
    new_rating = old_rating
    min_diff = float("inf")
    for rating in RTTF:
        if rating.text == "":
            continue
        if abs(int(rating.text) - int(old_rating)) < min_diff:
            min_diff = abs(int(rating.text) - int(old_rating))
            new_rating = rating.text
    return new_rating


def refresh_rttf_ratings(players):
    options = get_options()
    driver = webdriver.Chrome(options=options)
    for player in players:
        name, rttf = player[1], player[2]
        if rttf == "-":
            continue
        new_rating = get_rttf_player(driver, name, rttf)
        if new_rating is None:
                player.append("⁉")
                return
        if new_rating != rttf:
            if int(new_rating) > int(player[2]):
                player.append("⬆")
            else:
                player.append("⬇")
            player[2] = new_rating
