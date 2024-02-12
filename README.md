# Sistema Cabeleleila Leila

Sistema desenvolvido para Avaliação Técnica DSIN, esse sistema cobre os requisitos propostos para um salão de beleza.
Com esse sistema é possível realizar novos cadastros, novos agendamentos, e até mesmo alterar agendamentos que já foram feitos anteriormente.

### 📋 Pré-requisitos

É necessário ter instalado em seu dispositivo o MySQL e o PyCharm (ou qualquer IDE que comporte o Python)
Além disso, é necessário instalar duas bibliotecas.

Para instalar o MySQL, você pode achar o download em: [MYSQL](https://dev.mysql.com/downloads/)
Para instalar o PyCharm, você pode achar o download em: [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/?section=windows)

### 🔧 Instalação

Também será necessária a instalação de 2 bibliotecas Python. 
Como fazer:

1- Instalar o mysql connector
Abra o terminal de sua IDE ou do CMD, e digite:
```
pip install mysql-connector-python
```

Após isso, o mysql connector será instalado

2- Instalar o pyinstaller
Ainda no seu terminal, digite:
```
pip install pyinstaller
```

Depois disso, a instalação estará completa e você poderá fechar seu terminal.


## ⚙️ Executando os testes

Foram feitos testes de todas as funcionalidades do sistema, e tudo correu sem apresentar nenhum tipo de erro.

### 🔩 Imagens dos testes

Seguem imagens das diversas funcionalidades do sistema:

![image](https://github.com/mariafernandarsantos/cabeleleila_leila/assets/106030117/b79c9bb7-376e-47b2-8891-b45c8a60b559)

![image](https://github.com/mariafernandarsantos/cabeleleila_leila/assets/106030117/3008ec07-d2e0-460f-9725-31d58931667e)

![image](https://github.com/mariafernandarsantos/cabeleleila_leila/assets/106030117/76079875-43f0-4558-8226-bec97bc3443c)

![image](https://github.com/mariafernandarsantos/cabeleleila_leila/assets/106030117/81da92a2-f195-4368-b9a0-67500bb72b93)

![image](https://github.com/mariafernandarsantos/cabeleleila_leila/assets/106030117/f482f466-63b7-4a23-83a7-e47298173d5c)



### ⌨️ Notas

* O banco de dados vem VAZIO, pois serão adicionados dados conforme ocorrem os cadastros pelo sistema.
* Além do código em Python que pode ser executado para o funcionamento do sistema, também há um arquivo executável 'sistema_leila.exe' na pasta 'dist'
* É recomendado executar o sistema por meio da IDE em caso de testar todas as funcionalidades, pois a cada encerramento o arquivo .exe é fechado e deve ser aberto novamente.
* Dentro do código em 'host', 'user', 'password' e 'database', deve ser inserido as informações do SEU sistema do banco de dados
![image](https://github.com/mariafernandarsantos/cabeleleila_leila/assets/106030117/f39b9ddb-2111-48e8-9cc0-71ec567fd9d0)

* Caso o arquivo 'sistema_leila.exe' não funcione, será necessário que você execute o seguinte comando em seu terminal:
  ```
    pyinstaller --onefile sistema_leila.py

  ```
  Isso resultará na criação de um outro arquivo .exe, mas com o seu banco de dados.


## 🛠️ Construído com

* [Python](https://www.python.org)
* [MySQL](https://www.mysql.com)


## ✒️ Autora

* **Maria Fernanda Rodrigues Santos** - *Todo o projeto* - [mariafernandarsantos](https://github.com/mariafernandarsantos)


## 🎁 Gratidão

* Agradeço a equipe da DSIN pela oportunidade;
* Agradeço a todos meus professores, pois me ensinaram grande parte do que sei;
* Agradeço meus pais, pois sem eles não estaria aqui;
* Obrigada pela atenção!
