from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from bot_configur import Alert 
import psutil
import uvicorn
import socket

app = FastAPI(title="metriks")
templates = Jinja2Templates(directory="templates")


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



@app.get("/")
def metrics(request: Request):
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent > 80 or mem_percent > 80:
        Alert.alert(f"High CPU or memory utilization! CPU={cpu_percent}%, memory={mem_percent}%")
        message = "High CPU or memory utilization!"
    return templates.TemplateResponse("index.html", {"request": request, "value1": cpu_percent, "value2": mem_percent, "ip": local_ip, "massage": message})


if __name__ == "__main__":
    uvicorn.run(app="web:app")


