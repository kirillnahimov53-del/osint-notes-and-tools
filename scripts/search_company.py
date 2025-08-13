# Заглушка: сюда добавишь парсинг нужных источников
import sys
if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "test company"
    print(f"searching for: {q}")
