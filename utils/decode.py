



#Classe responsável por decodificar as mensagens

class Decode:

    def __init__(self):
        print('start decode module')

    def decode_msg(self, msg, bot):
        bot.send_message(msg.chat.id, "No momento estou apenas respondendo a comandos, qualquer duvida, me pede um /help")

    def decode_handler(self, handler, bot):
        bot.reply_to(handler, 'Seja bem vindo!')           
