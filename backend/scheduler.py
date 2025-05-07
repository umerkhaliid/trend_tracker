# backend/scheduler.py
import schedule
import time
from save_data import save_posts

schedule.every(10).minutes.do(save_posts)

while True:
    schedule.run_pending()
    time.sleep(1)
