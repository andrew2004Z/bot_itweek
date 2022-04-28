import telebot

bot = telebot.TeleBot('5332736256:AAE5XW7GXi0Fyzqe6qdFAVgxCS3QH-omBo8')
sp = []
for i in range(1, 12):
    photo = bot.send_photo('604900292', open(f'2/{i}.jpg', 'rb'))
    file_id = photo.photo[0].file_id
    sp.append(file_id)
print(sp)
