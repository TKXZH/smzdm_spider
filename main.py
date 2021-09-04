import schedule
import scrape.smzdm_cralwer as cralwer
import speaker.baidu_aip as aip
import speaker.player as player

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
MP3_PATH = ''


def run():
    text = cralwer.run()
    map3_path = aip.get_map3(text, APP_ID, API_KEY, SECRET_KEY, MP3_PATH)
    player.play(map3_path)


if __name__ == '__main__':
    schedule.every(3).hours.do(run())
