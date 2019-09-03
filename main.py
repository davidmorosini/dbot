import os
import sys
import json
import telebot

from utils.decode import Decode

def start_server():
    try:

        arq_configs = open('configs.json').read()
        configs = json.loads(arq_configs)

        #Carregando token do telegram (esse arquivo e excluido do projeto pelo .gitignore)
        arq_token_ = open('telegram-token.json').read()
        json_token = json.loads(arq_token_)

        bot = telebot.TeleBot(json_token['key'])
        
        d = Decode()

        #Listener para receber mensagens, exemplo: "Ok, ignore esta mensagem."
        @bot.message_handler(func = lambda m: not((len(m.text.split('/')) > 1)))
        def decodifica_msg(message):
            d.decode_msg(message, bot)

        #Listener para tratar as requests de mensagens como comando, exemplo: "/help" ou "/teste"
        @bot.message_handler(func = lambda m: ((len(m.text.split('/')) > 1)))
        def decodifica_handler(message):
            d.decode_handler(message, bot)

        #ou tambem definindo os comandos diretamente
        @bot.message_handler(commands=['help', 'start'])
        def reply_handler(message):
            bot.reply_to(message, 'Seja bem vindo!')

        
        #Iniciando o polling do servico
        print('Start polling.')
        bot.polling()
    except:
        print('# ERRO: Unexpected error on bot server: ' + sys.exc_info())
        

# "funcao" main do python
if __name__ == "__main__":
    start_server()