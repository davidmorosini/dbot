# dbot
Projeto com objetivo de explorar o ambiente de desenvolvimento e utilizar a integração com o [Telegram](https://web.telegram.org/).

## Projeto Não Comercial, apenas para uso pessoal e aprendizagem

## Como responder as primeiras mensagens com o bot?

* Para criar um Bot no [Telegram](https://web.telegram.org/#/login), realize o login e Acesse o canal [@BotFather](https://telegram.me/botfather).
	- Envie uma mensagem com ```/newbot``` e siga as instruções fornecidas até concluir. Após criar, o BotFather irá lhe fornecer o *Token* de acesso, salve em um arquivo ```telegram-token.json```, conforme abaixo:
	
	```python
		{
			"key":"TELEGRAM_TOKEN"
		}	
	```

* Com o Bot criado, vamos configurar o ambiente de desenvolvimento. Neste projeto fora utilizado python e a biblioteca [telebot](https://github.com/eternnoir/pyTelegramBotAPI) para conexão com o Telegram.
	
	- Instale o [Anaconda](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart).
	- Abra o terminal e crie um ambiente virtual para o projeto, o ativando em seguida:
		```
			$ conda create --name bot python=3
			$ conda activate bot
		```

	- Instale as bibliotecas bases necessárias via [pip](https://pypi.org/project/pip/):
		```
			(bot)$ pip install pyTelegramBotAPI
		
		```
	- No mesmo terminal aberto, rode o arquivo ```main.py```
		```
			(bot)$ python main.py
		```
	- Procure pelo nome do bot no buscador do telegram e cliquem em Começar
		- O nome do bot é o de posfixo ```_bot```

	- Teste com algumas mensagens e comandos, como por exemplo ```/help``` ou ```Ola bot```
	 


* Para maiores detalhes, utilize a documentação contida no [github](https://github.com/eternnoir/pyTelegramBotAPI)


## Referências

* API de conexão com Telegram [telebot](https://github.com/eternnoir/pyTelegramBotAPI)


	
