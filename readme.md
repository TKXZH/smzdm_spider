###什么值得买三小时排行榜爬虫，每三小时运行并将获取到的商品信息用语音播报出来。

step1: 在main.py中修改你自己的配置 

`APP_ID = '此处改成你自己的APP_ID'
API_KEY = '此处改成你自己的API_KEY'
SECRET_KEY = '此处改成你自己的SECRET_KEY'
MP3_PATH = '此处改成你希望mp3文件存储的本地目录'`

step2: 修改这行代码，已你希望的时间间隔运行程序
`schedule.every(3).hours.do(run)`