from instabot import *
import config

bot = Bot()

bot.login(username = config.user,
          password = config.passwd)

bot.upload_photo("./posts/post3.jpg",
                 caption = "Teste de Post 3")
