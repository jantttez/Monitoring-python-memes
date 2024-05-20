from bot_configur import Alert 
import threading
import psutil
from time import sleep
import socket


def get_local_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip_address = s.getsockname()[0]
        s.close()
        return local_ip_address
    except Exception as e:
        return str(e)

local_ip = get_local_ip_address()


def metrikas():
        while True:
            sleep(5)
            cpu_percent = psutil.cpu_percent()
            mem_percent = psutil.virtual_memory().percent
            if cpu_percent > 80 or mem_percent > 80:
                Alert.alert(f"High CPU or memory utilization! CPU={cpu_percent}%, memory={mem_percent}% on server {local_ip}")
            


if __name__ == "__main__":
    print("start monitoring witch notification...")
    print("monitoring.")
    thread = threading.Thread(target=metrikas)
    thread.daemon = True 
    thread.start()

    while True:
        pass