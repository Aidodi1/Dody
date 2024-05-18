import telebot
from asa import *
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Данный бот переводит неправильные глаголы в вторую форму , и на руский язык ')
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'be':
        bot.send_message(message.from_user.id, 'in the past : was, were  and translation : был')
    elif message.text == 'become':
        bot.send_message(message.from_user.id, 'in the past : became   and translation : становиться')
    elif message.text == 'begin':
        bot.send_message(message.from_user.id, 'in the past : began   and translation : начинать')
    elif message.text == 'bring':
        bot.send_message(message.from_user.id, 'in the past : brought   and translation : приносить')
    elif message.text == 'build':
        bot.send_message(message.from_user.id, 'in the past : built   and translation : строить')
    elif message.text == 'buy':
        bot.send_message(message.from_user.id, 'in the past : bought   and translation : покупать')
    elif message.text == 'can':
        bot.send_message(message.from_user.id, 'in the past : could   and translation : можешь')
    elif message.text == 'come':
        bot.send_message(message.from_user.id, 'in the past : came    and translation : приходить')
    elif message.text == 'cost':
        bot.send_message(message.from_user.id, 'in the past : cost   and translation : стоить')
    elif message.text == 'do':
        bot.send_message(message.from_user.id, 'in the past : did   and translation : делать')
    elif message.text == 'draw':
        bot.send_message(message.from_user.id, 'in the past : drew   and translation : рисовать')
    elif message.text == 'drink':
        bot.send_message(message.from_user.id, 'in the past : drank   and translation : пить')
    elif message.text == 'eat':
        bot.send_message(message.from_user.id, 'in the past : ate   and translation : есть')
    elif message.text == 'fall':
        bot.send_message(message.from_user.id, 'in the past : fel   and translation : падать')
    elif message.text == 'feel':
        bot.send_message(message.from_user.id, 'in the past : felt   and translation : чувствовать')
    elif message.text == 'fight':
        bot.send_message(message.from_user.id, 'in the past : fought   and translation : бороться')
    elif message.text == 'find':
        bot.send_message(message.from_user.id, 'in the past : found   and translation : находить')
    elif message.text == 'fly':
        bot.send_message(message.from_user.id, 'in the past : flew   and translation : летать')
    elif message.text == 'forget':
        bot.send_message(message.from_user.id, 'in the past : forgot   and translation : забывать')
    elif message.text == 'get':
        bot.send_message(message.from_user.id, 'in the past : got   and translation : получать')
    elif message.text == 'give':
        bot.send_message(message.from_user.id, 'in the past : gave   and translation : давать')
    elif message.text == 'go':
        bot.send_message(message.from_user.id, 'in the past : went   and translation : идти')
    elif message.text == 'grow':
        bot.send_message(message.from_user.id, 'in the past : grew   and translation : расти')
    elif message.text == 'hang':
        bot.send_message(message.from_user.id, 'in the past : hung   and translation : вешать')
    elif message.text == 'have':
        bot.send_message(message.from_user.id, 'in the past : had   and translation : иметь')
    elif message.text == 'hear':
        bot.send_message(message.from_user.id, 'in the past : heard   and translation : слышать')
    elif message.text == 'hold':
        bot.send_message(message.from_user.id, 'in the past : held   and translation : держать')
    elif message.text == 'know':
        bot.send_message(message.from_user.id, 'in the past : knew   and translation : знать')
    elif message.text == 'leave':
        bot.send_message(message.from_user.id, 'in the past : left   and translation : оставлять')
    elif message.text == 'let':
        bot.send_message(message.from_user.id, 'in the past : let   and translation : позволять')
    elif message.text == 'make':
        bot.send_message(message.from_user.id, 'in the past : made   and translation : делать')
    elif message.text == 'may':
        bot.send_message(message.from_user.id, 'in the past : might   and translation : может')
    elif message.text == 'meet':
        bot.send_message(message.from_user.id, 'in the past : met   and translation : встретиться')
    elif message.text == 'pay':
        bot.send_message(message.from_user.id, 'in the past : paid   and translation : платить')
    elif message.text == 'put':
        bot.send_message(message.from_user.id, 'in the past : put   and translation : поставить')
    elif message.text == 'read':
        bot.send_message(message.from_user.id, 'in the past : read   and translation : читать')
    elif message.text == 'retell':
        bot.send_message(message.from_user.id, 'in the past : retold   and translation : пересказывать')
    elif message.text == 'ring':
        bot.send_message(message.from_user.id, 'in the past : rang   and translation : звонить')
    elif message.text == 'rise':
        bot.send_message(message.from_user.id, 'in the past : rose   and translation : подниматься')
    elif message.text == 'run':
        bot.send_message(message.from_user.id, 'in the past : ran   and translation : бежать')
    elif message.text == 'say':
        bot.send_message(message.from_user.id, 'in the past : said   and translation : говорить')
    elif message.text == 'see':
        bot.send_message(message.from_user.id, 'in the past : saw   and translation : смотреть')
    elif message.text == 'sell':
        bot.send_message(message.from_user.id, 'in the past : sold   and translation : продавать')
    elif message.text == 'send':
        bot.send_message(message.from_user.id, 'in the past : sent   and translation : отправлять')
    elif message.text == 'show':
        bot.send_message(message.from_user.id, 'in the past : showed   and translation : показывать')
    elif message.text == 'shut':
        bot.send_message(message.from_user.id, 'in the past : shut   and translation : закрывать')
    elif message.text == 'sing':
        bot.send_message(message.from_user.id, 'in the past : sang   and translation : петь')
    elif message.text == 'sit':
        bot.send_message(message.from_user.id, 'in the past : sat   and translation : сидеть')
    elif message.text == 'sleep':
        bot.send_message(message.from_user.id, 'in the past : slept   and translation : спать')
    elif message.text == 'speak':
        bot.send_message(message.from_user.id, 'in the past : spok   and translation : говорить')
    elif message.text == 'spend':
        bot.send_message(message.from_user.id, 'in the past : spent   and translation : тратить')
    elif message.text == 'stand':
        bot.send_message(message.from_user.id, 'in the past : stood   and translation : стоять')
    elif message.text == 'swim':
        bot.send_message(message.from_user.id, 'in the past : swam   and translation : плавать')
    elif message.text == 'take':
        bot.send_message(message.from_user.id, 'in the past : took   and translation : брать')
    elif message.text == 'tell':
        bot.send_message(message.from_user.id, 'in the past : told   and translation : рассказывать')
    elif message.text == 'think':
        bot.send_message(message.from_user.id, 'in the past : thought   and translation : думать')
    elif message.text == 'understand':
        bot.send_message(message.from_user.id, 'in the past : understood   and translation : понимать')
    elif message.text == 'wake':
        bot.send_message(message.from_user.id, 'in the past : woke   and translation : просыпаться')
    elif message.text == 'win':
        bot.send_message(message.from_user.id, 'in the past : won   and translation :выигрывать')
    elif message.text == 'write':
        bot.send_message(message.from_user.id, 'in the past : wrote   and translation : писать')
    else:
        bot.send_message(message.from_user.id, 'I didn`t get it  ')

bot.infinity_polling()
