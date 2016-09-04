Parte do Curso WttD / henrique Batos

```
Clone o repositório.
Crie um virtualenv com Python 3.5.2
Ative o virtualenv.
Instale as dependências.
Configure a instância com o .env
Execute os testes.

git clone git@github.com:FabianoAlmeidaMelo/wttd.git
cd wttd
mkvirtualenv .wttd
workon .wttd
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test

Como fazer o deploy:

Crie um instância no heroku.
Envie as configurações para o heroku.
Define uma SECRET_KEY segura para instância.
Defina DEBUG=False
Configure o serviço de email.
Envie o código para o heroku
heroku create minhainstancia

heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```
