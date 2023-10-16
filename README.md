# dio.etl-colab
O projeto consome a API restful da SDW e utiliza a API do Bing GPT-4 para criar uma mensagem personalizada para cada usuario, se passando pelo Tio Patinhas.
## Detalhes
- A api pode dar erro quando utilizada em plataformas de nuvens como o Google Colab, pois há um processo de captcha para IP's que estão em uma lista "não-segura" (VPN, servidores etc).
- Rodando em máquina local funciona perfeitamente.
- O bing é meio burro então as vezes precisa rodar o código duas vezes para completar a operação, pois ele da a resposta errada.
