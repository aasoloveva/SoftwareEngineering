from time import sleep
from datetime import datetime

for i in range(5):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    sleep(1)
