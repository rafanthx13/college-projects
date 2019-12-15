## pipenv

+ instale pip env com `pip install pipenv` é um micro ambiente que junta dependencias e ambiente de execução

+ `pipenv --three`: Dentro da pasta, voce cria o pipenv do tipo python 3. Esse é o primerio passo
+ `pipenv install Flask` : Instala localmente no pipenv
+ `pipenv run pip freeze` : Ver as dependencias doseu pip env
+ `pipenv shell`: To activate this project's virtualenv, run the following:
 - No gitBash nao mostra o simbolo do novo ambiente. Se quiser saber dele, da outra `shell` que vai acusar que ja esta em um
 - `exit` para sair do ambiente
+ pipenv run <comando> : executa um arquivo pytohn considerando esse ambiente

+ `pipenv lock` cria pip.lock caso nao esxistir
+ ` pipenv run pip freeze > requirements.txt` : salvar tudo num arquivo, pra ter certeza

## flask

+ export FLASK_APP=server.py
+ $ export FLASK_DEBUG=1
+ flask run : Vai retornar o host da app



**Executar**

`pipenv shell -- export FLASK_APP=server.py &&  export FLASK_DEBUG=1 && flask run`