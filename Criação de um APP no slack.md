# manager_slack -  Envio de mensagens via API do slack
 
# Criação de um APP para o slack

## acesse a url https://api.slack.com/apps e clique em "Create New App", e logo em seguida aparecerá uma janela flutuante clique em "From Scratch"
 
![capturar](https://user-images.githubusercontent.com/42252285/144473501-d474af02-fe94-45f3-8e88-704ba11da0ca.png)

## de um nome ao seu APP e selecione em qual workspace deseja adiciona-lo e clique em "Create APP"
![capturar](https://user-images.githubusercontent.com/42252285/144474002-e18db4ac-b599-48d7-9e54-e97b981e3ca9.png)

## nessa pagina temos as configurações de todos nossos apps do slack, mas nosso foco no momento e criar um webhook para enviar mensagens, por isso vamos clicar em "OAuth & Permissions" na coluna do lado esquerdo

![capturar](https://user-images.githubusercontent.com/42252285/144474391-5ae505c2-6695-4b47-aa55-a73e72bfce04.png)

## Nesta pagina vamos nos deparar com varios blocos para permissões do APP, role a pagina até "Scopes" e adicione a permissão "chat:write"
![capturar](https://user-images.githubusercontent.com/42252285/144475592-73466233-87d1-4397-9fb2-9168e045eada.png)

## Após fazer isto, role a pagina para cima e clique em "Install App" na coluna do lado esquerdo, e clique em "Install to Workspace", na pagina que aparecer irá solicitar que você permita o APP a acessar o seu workspace
![capturar](https://user-images.githubusercontent.com/42252285/144475892-393fc5f2-a5ac-4069-b12c-8ed0376c4783.png)

## Em seguida vamos ativar os webhooks para o APP, clicando em "Incoming Webhooks", e virando a chave para "On", ao fazer isto, será solicitado a reinstalação do APP, seguiremos com a reinstalação clicando no link da mensagem amarela na parte superior
![capturar](https://user-images.githubusercontent.com/42252285/144476214-96864d0d-5c0e-4290-acb7-4d1c3bd0f92f.png)

## Agora sim vamos selecionar onde nosso APP irá mandar mensagens, no meu caso vou selecionar no meu chat privado

![capturar](https://user-images.githubusercontent.com/42252285/144476668-eb3e66c6-e52e-43c7-81ed-235e56139f4e.png)

## Feito isso, agora temos a URL do webhook pronta para enviarmos mensagens para o chat selecionado, para adicionar novas urls direcionado para outro chat, basta apenas clicar em "Add New Webhook to Workspace" no final da pagina
![capturar](https://user-images.githubusercontent.com/42252285/144477214-645aa999-73d7-4c1e-9751-c356574f1d32.png)
