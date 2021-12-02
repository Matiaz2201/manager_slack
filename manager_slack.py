import requests

class Slack():

    def __init__(self, url, mensagem=None):
        self.url = url
        self.mensagem = mensagem

    def send(self, mensagem=None, url=None, **kwargs):
        if mensagem:
            self.mensagem = mensagem
        if url:
            self.url = url

        payload = {
            "attachments": [
                    {
                        "color": "#0052CC",
                        "blocks": [
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": f"Hello World:\n*<{kwargs.get('dados')['urlWebHook']}|Informações sobre WebHooks>*"
                                }
                            },
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": self.mensagem
                                },
                                "accessory": {
                                    "type": "image",
                                    "image_url": f"{kwargs.get('dados')['imagemSlack']}",
                                    "alt_text": f"{kwargs.get('dados')['nome']}"
                                }
                            }
                        ]
                    }
                ]
            }
            	
        response = requests.post(url=self.url, json=payload)
        print(response)
    
    def send_error(self, mensagem=None, url=None, **kwargs):
        if mensagem:
            self.mensagem = mensagem
        if url:
            self.url = url
            
        payload = {
            "attachments": [
                    {
                        "color": "#ff0000",
                        "blocks": [
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": self.mensagem
                                }
                            }
                        ]
                    }
                ]
            }
            	
        response = requests.post(url=self.url, json=payload)
        print(response)
    
    def send_success(self, mensagem=None, url=None, **kwargs):
        if mensagem:
            self.mensagem = mensagem
        if url:
            self.url = url
            
        payload = {
            "attachments": [
                    {
                        "color": "#26D701",
                        "blocks": [
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": self.mensagem
                                }
                            }
                        ]
                    }
                ]
            }
            	
        response = requests.post(url=self.url, json=payload)
        print(response)
    
if __name__ == "__main__" :
    pass