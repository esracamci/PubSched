import schedule
import time

def job():

    import pubmed7

#### for testing purposes - ctrl-c will interrupt the loop
    # Run job every 3 second/minute/hour/day/week,
    #   schedule.every(5).seconds.do(job)

# Run job on Monday at 9:15 AM 
schedule.every().monday.at("09:15").do(job)

while True:
    # run_pending
    schedule.run_pending()
    time.sleep(1)
