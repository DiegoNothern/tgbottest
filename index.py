from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait

stop = False
client = Client('session', '15179171', 'c8c90d2964a788d4827aac026acf6913')
client.start()
client.stop()

@client.on_message(filters.command('спам', prefixes=['.','!','/', '-']) & filters.me)
def message_handler(client, message):
    global stop
    args = message.text.split(' ')
    #if !args[1] or !is_number(args[1]) or !args[2]:
        #client.send_message(message.chat.id, 'Используйте: /spam <кол-во сообщений> <сообщение>')
    if args[1] == 'стоп':
        stop = True
        client.send_message(message.chat.id, 'Вы успешно отключили спам!')
    i = int(args[1])
    while i >= 0:
        try:
            if(stop == True):
                i = 0
                stop = False
            client.send_message(message.chat.id, args[2])
            sleep(1/7)
        except FloodWait as e:
            sleep(e.x)
        i -= 1

client.run()