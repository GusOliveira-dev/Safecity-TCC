# safecity v0.1
<p align="center">
<img src="https://github.com/olivasss/safecity/assets/82964223/bd74ae19-5d0e-4fee-b578-01b7442881f1" width="80">
</p>
<p align="center" width="80"><strong>Safecity</strong></p>

## Objetivo
O grande volume de ocorrências criminais no estado de São Paulo acaba superpopulando sua base de dados, dificultando a avaliação dos problemas. Para tomar medidas de prevenção e segurança em uma localidade, são necessárias informações claras sobre a situação, para este fim está sendo desenvolvido esse projeto, com o intuito de ajudar a conscientizar a população e as autoridades com informações dispostas de maneira clara e interativa, auxiliando em estudos e tratativas.

## Linguagens / Ferramentas utilizadas:

|     Versoes     |                         Linguagens                          |
| :----------------: | :---------------------------------------------------: |
|     `python 3.9+`    | <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Python-Dark.svg" width="48">  |
|     `HTML 5`    | <img src="https://github.com/tandpfun/skill-icons/raw/main/icons/HTML.svg" width="48">  |
|     `CSS 3`    | <img src="https://github.com/tandpfun/skill-icons/raw/main/icons/CSS.svg" width="48">  |
|     `JavaScript ES13`    | <img src="https://github.com/tandpfun/skill-icons/raw/main/icons/JavaScript.svg" width="48">  |

## Configuração para compilar o site

**Clone o repositório e acesse a pasta do projeto:**

```bash
$ git clone https://github.com/olivasss/safecity.git
```

## Para localhost e com noticias funcionando:

**Para iniciar o projeto, execute:**
```bash
python -m http.server 8080
```

**Ir para a porta criada localmente:**
<br><br>
Heroku Deploy:
```
https://safecity-55bf961495b6.herokuapp.com/
```

## Configuração para rodar o bot de captaçao de dados

**É necessário instalar as bibliotecas externas python para funcionamento do script:**
```bash
pip install pandas
pip install selenium
pip install openpyxl
```
<br>

**Configurando o código**

1. Navegue até a pasta do projeto.

2. Abra o arquivo `bot.py` localizado dentro da pasta.

3. Adicione os caminhos necessários para rodar a aplicaçao dentro da sua máquina.

```bash
# Caminho para a pasta de downloads padrão do navegador
arquivo_baixado = "/SPDadosCriminais_2023.xlsx" # Aplicar o caminho onde está o arquivo baixado (padrao) na máquina (exemplo: "F:/Users/xxx/Downloads/SPDadosCriminais_2023.xlsx")
```

4. Rode o código.
