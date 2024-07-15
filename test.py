import schedule
import time

def job():
    print("Sending email...")

# Schedule the task
schedule.every().day.at("09:00").do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)