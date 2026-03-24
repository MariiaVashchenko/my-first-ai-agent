# Research Agent
Дослідницький агент, який шукає інформацію в інтернеті та генерує структуровані Markdown-звіти.
---
## Як запустити
1. Клонувати репозиторій:
   ```bash
   git clone <url-репозиторію>
   cd research-agent
2.Створити віртуальне середовище:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3.Встановити залежності:
bash
pip install -r requirements.txt
Створи файл .env і додай API-ключ (див. нижче)

4.Запустити агента:
bash
python main.py
------
Залежності
Всі залежності вказані у requirements.txt:

-langchain — фреймворк для створення агентів
-langchain-openai — інтеграція з OpenAI
-langgraph — управління станом і памʼяттю агента
-ddgs — пошук через DuckDuckGo
-trafilatura — витягування тексту з веб-сторінок
-python-dotenv — читання змінних середовища
-pydantic-settings — валідація конфігурації
-httpx — HTTP-запити
-API-ключ
Проєкт використовує OpenAI API.

Зареєструйся на platform.openai.com
Створи API-ключ: platform.openai.com
Створи файл .env у корені проєкту: OPENAI_API_KEY=sk-proj-твій-ключ-тут

Архітектура
research-agent/
├── main.py           # Точка входу — інтерактивний діалог
├── agent.py          # Створення та налаштування агента
├── tools.py          # Інструменти: web_search, read_url, write_report
├── config.py         # Конфігурація, налаштування, system prompt
├── requirements.txt  # Залежності проєкту
├── .env              # API-ключі (не в git!)
├── .gitignore        # Файли, які ігнорує git
├── output/           # Папка для згенерованих звітів
└── README.md         # Цей файл
Як працює агент:
main.py — запускає інтерактивний цикл, приймає запити користувача
agent.py — створює ReAct-агента з памʼяттю через LangGraph
tools.py — три інструменти:
web_search — шукає в DuckDuckGo
read_url — читає повний текст сторінки
write_report — зберігає звіт у файл
config.py — зберігає всі налаштування в одному місці

Цикл роботи агента:
Користувач задає питання
        ↓
Агент аналізує запит
        ↓
web_search → знаходить релевантні сторінки
        ↓
read_url → читає деталі з найкращих джерел
        ↓
Агент формує відповідь
        ↓
write_report → зберігає звіт у output/

Приклад використання:

 Ти: Порівняй три підходи до RAG: naive, sentence-window та parent-child
Агент думає...
Агент: [структурований звіт]
Звіт збережено: output/rag_comparison.md
Приклад згенерованого звіту — у папці example_output/.
