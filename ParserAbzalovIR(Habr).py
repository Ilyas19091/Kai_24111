import csv
import time
import random
import requests
from bs4 import BeautifulSoup
import urllib3

# Отключаем предупреждения о проверке SSL-сертификатов
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://habr.com/ru/news/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
OUTPUT_FILE = "habr_news.csv"  # Изменили имя итогового файла
PAGES_TO_PARSE = 3  # Количество страниц для сбора данных


def parse_habr_news():
    all_news = []

    print(f"Начинаем парсинг первых {PAGES_TO_PARSE} страниц новостей Хабра...")

    for page in range(1, PAGES_TO_PARSE + 1):
        # Формируем ссылку правильно: https://habr.com
        url = f"{BASE_URL}page{page}/"
        print(f"Обрабатывается страница {page}: {url}")

        try:
            response = requests.get(url, headers=HEADERS, timeout=10, verify=False)

            if response.status_code != 200:
                print(f"Ошибка доступа к странице {page}: Статус {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            articles = soup.find_all("article", class_="tm-articles-list__item")

            for article in articles:
                try:
                    title_element = article.find("a", class_="tm-title__link")
                    if not title_element:
                        continue

                    title = title_element.text.strip()
                    link = "https://habr.com" + title_element["href"]

                    author_element = article.find("a", class_="tm-user-info__username")
                    author = author_element.text.strip() if author_element else "Не указан"

                    date_element = article.find("span", class_="tm-article-reading-time__label") or article.find("time")
                    date_text = date_element.get("title", date_element.text).strip() if date_element else "Не указана"

                    rating_element = article.find("span", class_="tm-votes-meter__value")
                    rating = rating_element.text.strip() if rating_element else "0"

                    all_news.append({
                        "Title": title,
                        "Author": author,
                        "Date": date_text,
                        "Rating": rating,
                        "Link": link
                    })

                except AttributeError:
                    continue

        except requests.exceptions.RequestException as e:
            print(f"Ошибка сети при запросе страницы {page}: {e}")

        time.sleep(random.uniform(1.0, 3.0))

    if all_news:
        save_to_csv(all_news, OUTPUT_FILE)
        print(f"\nПарсинг успешно завершен! Сохранено новостей: {len(all_news)}")
    else:
        print("\nНе удалось собрать данные. Проверьте подключение к интернету.")


def save_to_csv(data, filename):
    with open(filename, mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Date", "Rating", "Link"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Данные успешно записаны в файл {filename}")


if __name__ == "__main__":
    parse_habr_news()
