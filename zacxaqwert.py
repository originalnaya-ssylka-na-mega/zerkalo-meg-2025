import requests
import time

# Настройки
LM_STUDIO_API_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "your-model-name"  # например, "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"

HEADERS = {"Content-Type": "application/json"}

# Системный промпт (настрой под себя)
SYSTEM_PROMPT = """
Ты — профессиональный SEO-копирайтер. Напиши подробную, информативную и уникальную статью на заданную тему.
Статья должна быть структурирована: введение, основная часть с подзаголовками, заключение.
Объём — не менее 1500 слов. Используй ключевые слова естественно.
"""

# Чтение тем из файла
with open("topics.txt", "r", encoding="utf-8") as f:
    topics = [line.strip() for line in f if line.strip()]

# Генерация статей
for i, topic in enumerate(topics, 1):
    print(f"Генерация статьи {i}/{len(topics)}: {topic}")

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Напиши статью на тему: {topic}"}
        ],
        "temperature": 0.7,
    
        filename = f"article_{i:03d}_{topic[:30].replace(' ', '_').replace('/', '_')}.txt"
        with open(filename, "w", encoding="utf-8") as f_out:
            f_out.write(f"Тема: {topic}\n\n")
            f_out.write(article)

        print(f"✅ Сохранено: {filename}")
        time.sleep(1)  # пауза между запросами, чтобы не перегружать модель

    except Exception as e:
        print(f"❌ Ошибка при генерации статьи для темы '{topic}': {e}")

print("✅ Все статьи сгенерированы!")
