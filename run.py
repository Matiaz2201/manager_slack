#coding:utf-8


from manager_slack import Slack

def main():
    url = 'SUA URL AQUI'
    mensagem = 'Mensagem teste'
    dados={
        'urlWebHook':'https://api.slack.com/messaging/webhooks', 
        'imagemSlack' : 'https://logosmarcas.net/wp-content/uploads/2020/12/GitHub-Logo.png',
        'nome' : 'Github'
    }
    slack = Slack(url=url)

    slack.send(dados=dados, mensagem=mensagem)

if __name__ == '__main__':
        main()