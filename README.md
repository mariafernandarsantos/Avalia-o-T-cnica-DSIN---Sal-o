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

![image](https://github.com/mariafernandarsantos/Cabeleleila_Leila/assets/106030117/774d221c-8beb-4b60-9f66-49f08a2987ac)

![image](https://github.com/mariafernandarsantos/Cabeleleila_Leila/assets/106030117/bace6d14-9b22-4922-b983-e19a50c75edc)

![image](https://github.com/mariafernandarsantos/Cabeleleila_Leila/assets/106030117/01025e28-006e-436c-9448-b915c71da229)

![image](https://github.com/mariafernandarsantos/Cabeleleila_Leila/assets/106030117/08d60937-e98d-44a1-b9a0-cc8dba14fb3d)

![image](https://github.com/mariafernandarsantos/Cabeleleila_Leila/assets/106030117/c94616cc-ddcb-4316-b087-83f6c42478d1)

![image](https://github.com/mariafernandarsantos/Cabeleleila_Leila/assets/106030117/1ee0709d-78e1-4e24-b0f6-0e9ae2aaa32e)

![image](https://github.com/mariafernandarsantos/Cabeleleila_Leila/assets/106030117/6ffee3e3-5a50-4123-9211-41a7c265d906)


### ⌨️ Notas - Como executar

* Para usar o sistema como LEILA, é necessário inserir o número de cadastro 0.
* O banco de dados vem VAZIO, pois serão adicionados dados conforme ocorrem os cadastros pelo sistema.
* Além do código em Python que pode ser executado para o funcionamento do sistema, também há um arquivo executável 'sistema_leila.exe' na pasta 'dist'
* É recomendado executar o sistema por meio da IDE em caso de testar todas as funcionalidades, pois a cada encerramento o arquivo .exe é fechado e deve ser aberto novamente.
* Dentro do código em 'host', 'user', 'password' e 'database', DEVE ser inserido as informações do SEU sistema do banco de dados, caso contrário o programa não íra funcionar
  
![image](https://github.com/mariafernandarsantos/Cabeleleila_Leila/assets/106030117/2f10d17e-9388-4094-95ea-036a51d37d0d)

* Caso o arquivo 'sistema_leila.exe' não funcione, será necessário que você execute o seguinte comando em seu terminal:
  ```
    pyinstaller --onefile sistema_leila.py

  ```
  Isso resultará na criação de um outro arquivo .exe, mas com o seu banco de dados.


## 🛠️ Construído com

* [Python](https://www.python.org) - Linguagem de programação utilizada
* [MySQL](https://www.mysql.com) - Banco de dados utilizado


## ✒️ Autora

* **Maria Fernanda Rodrigues Santos** - *Todo o projeto* - [mariafernandarsantos](https://github.com/mariafernandarsantos)


## 🎁 Gratidão

* Agradeço a equipe da DSIN pela oportunidade;
* Agradeço a todos meus professores, pois me ensinaram grande parte do que sei;
* Agradeço meus pais, pois sem eles não estaria aqui;
* Obrigada pela atenção!
