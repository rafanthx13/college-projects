# Text Minig: Avaliador de Comentário

Trabalho de IA: Utilizaçâo de Rede Neural LSTM para aprender a classificar comentários sobre produtos com interface web usando Angular JS.

DataSet: https://www.kaggle.com/olistbr/brazilian-ecommerce/home

### Instalar no Linux

1. (Dados) Descompate o zip na pasta `/dados` para poder usar o `.csv`

2. (Web) na pasta `lib` execute no terminal `npm i` para instalar as dependências web para a página.

3. Para usar é recomendável instlar um `virtualenv` para rodar o flask. Basta seguir os seguintes passos (usando pytohn 3):


4. Execute os seguintes comandos no terminal: Instalar o virtual env, executalo, instlar as dependencias do python para o projeto, configurar `FLASK_APP` e rodar o server localmente.

```
$ sudo apt install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install flask
(venv) $ pip install flask_cors
(venv) $ pip install torch
(venv) $ pip install pandas
(venv) $ export FLASK_APP=server_txt.py
(venv) $ flask run
```

+ Tem que aparecer: `* Running on http://127.0.0.1:5000/`  indicando que está funcionando.
+ Para sair do flask, de CTRL+C e 
+ para sair desse ambiente, `deactivate`

5. Em seguida abra o `index.hmtl` pelo navegador e execute.

**Links úteis para instalação do virtualenv**

+ http://flask.pocoo.org/docs/1.0/installation/#install-create-env
+ https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais
+ https://www.tutorialspoint.com/flask/flask_environment.htm
+ https://linuxize.com/post/how-to-install-flask-on-ubuntu-18-04/
