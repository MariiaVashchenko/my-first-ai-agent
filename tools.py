import os
from langchain_core.tools import tool
from ddgs import DDGS
import trafilatura

@tool
def web_search(query: str):
    """
    Пошук в інтернеті через DuckDuckGo. Повертає список із 5 результатів.
    """
    # Ручне визначення схеми для Function Calling
    web_search.name = "web_search"
    web_search.description = "Пошук в інтернеті через DuckDuckGo для отримання актуальної інформації."
    web_search.args_schema = {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Пошуковий запит (наприклад, 'порівняння RAG підходів')"
            }
        },
        "required": ["query"]
    }

    try:
        with DDGS() as ddgs:
            results = [
                {"title": r.get("title"), "href": r.get("href"), "body": r.get("body")}
                for r in ddgs.text(query, max_results=5)
            ]
            return results
    except Exception as e:
        return f"Помилка пошуку: {e}"


# --- 2. Інструмент Читання URL ---

@tool
def read_url(url: str):
    """
    Отримує повний текст сторінки за посиланням.
    """
    # Ручне визначення схеми
    read_url.name = "read_url"
    read_url.description = "Читає повний вміст веб-сторінки. Використовуй, коли треба детально вивчити джерело."
    read_url.args_schema = {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "Повна адреса сайту (URL)"
            }
        },
        "required": ["url"]
    }

    try:
        downloaded = trafilatura.fetch_url(url)
        text = trafilatura.extract(downloaded)
        return text[:8000] if text else "Не вдалося витягти текст."
    except Exception as e:
        return f"Помилка читання: {e}"


# --- 3. Інструмент Запису Звіту ---

@tool
def write_report(filename: str, content: str):
    """
    Зберігає фінальний Markdown-звіт у файл.
    """
    # Ручне визначення схеми
    write_report.name = "write_report"
    write_report.description = "Зберігає фінальний результат дослідження у файл .md."
    write_report.args_schema = {
        "type": "object",
        "properties": {
            "filename": {
                "type": "string",
                "description": "Назва файлу (наприклад, 'report.md')"
            },
            "content": {
                "type": "string",
                "description": "Весь текст звіту у форматі Markdown"
            }
        },
        "required": ["filename", "content"]
    }

    try:
        if not os.path.exists("output"):
            os.makedirs("output")

        path = os.path.join("output", filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Звіт збережено у: {path}"
    except Exception as e:
        return f"Помилка запису: {e}"


# Список усіх інструментів для підключення до агента
all_tools = [web_search, read_url, write_report]