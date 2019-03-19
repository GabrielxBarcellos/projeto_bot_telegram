import telepot
from watson_bot import mandar_msg_watson


bot = telepot.Bot('803914027:AAHGy_0QQNlqqEGhL_gYiW_a2VDQUbSr2IU')
def recebendoMsg(msg):

    retorno = mandar_msg_watson(msg['text'])
    retorno_msg = str(retorno['output']['text']).strip("['']")
    bot.sendMessage(chat_id=int(msg['chat']['id']),text=retorno_msg)

bot.message_loop(recebendoMsg)

while True:
    pass