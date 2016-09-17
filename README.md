# Eventex

Sistema de Eventos encomendado pela morena.

Parte do Curso WttD / Henrique Bastos

[![Build Status](https://travis-ci.org/FabianoAlmeidaMelo/wttd.svg?branch=master)](https://travis-ci.org/FabianoAlmeidaMelo/wttd)


## Como desenvolver?

```
Clone o repositório.
Crie um virtualenv com Python 3.5.2
Ative o virtualenv.
Instale as dependências.
Configure a instância com o .env
Execute os testes.
```

```console
git clone git@github.com:FabianoAlmeidaMelo/wttd.git wttd
cd wttd
mkvirtualenv .wttd
workon .wttd
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy:

```
Crie um instância no heroku.
Envie as configurações para o heroku.
Define uma SECRET_KEY segura para instância.
Defina DEBUG=False
Configure o serviço de email.
Envie o código para o heroku
```

```console
heroku create minhainstancia
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```
