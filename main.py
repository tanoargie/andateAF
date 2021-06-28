import os
import arrow
import tweepy
import time
import schedule
from dotenv import load_dotenv

load_dotenv()

def job():
    finalMandato = arrow.Arrow(2023, 12, 10)
    comienzoMandato = arrow.Arrow(2019, 12, 10)
    diasQueFaltanDeMandato = ( finalMandato - arrow.now() ).days
    diasTotalesDeMandato = (finalMandato - comienzoMandato).days
    diasQuePasaronDeMandato = (arrow.now() - comienzoMandato).days
    percentageDone = round( ( diasQuePasaronDeMandato / diasTotalesDeMandato ) * 100, 2 )    
    auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET'))
    auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN_KEY'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
    
    api = tweepy.API(auth)
    api.update_status("Faltan " + str( diasQueFaltanDeMandato ) + " días para que termine el gobierno de Alberto Fernández. Ya pasó el " + str( percentageDone ) + "% de su mandato.")
    # print(str( percentageDone ))
    # print(str( diasQueFaltanDeMandato ))
    return

schedule.every().day.at("23:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)

# if __name__ == '__main__':
    # job()