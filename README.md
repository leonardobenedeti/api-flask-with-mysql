# FLASK API WITH POSTGRES ON HEROKU

Todos os arquivos necessários para rodar a api já estão prontos, porém foram criados no meu ambiente. 
Recomendo que siga os passos abaixo para sobrescreve-los de acordo com o seu ambiente e projeto.
Caso queira renomear alguma coisa por exemplo, vale revisitar os passos para não quebrar a API.

## Instalações necessárias para rodar localmente
Como estamos criando uma api python, nem preciso comentar que precisa ter o python instalado. O que vale ressaltar é que estou utilizando a versão 3.6.5 para criar este ambiente.

```
pip install flask gunicorn
```

### ~ a partir daqui é necessário estar dentro da pasta da api/repo ~

## Criação/Sobrescrita do arquivo requirements.txt
Este arquivo é responsável por nomear os pacotes que são necessários para sua api. Se a ideia é apenas rodar a api localmente, não é necessário, porém como este repositório está conectado com um app heroku, ele precisa existir. Recomendo o teste no heroku, é bem simples.

```
pip freeze > requirements.txt
```

## Criação/Sobrescrita do arquivo Procfile
Este arquivo, em poucas palavras, indexa sua api. Ex.: este repositorio tem a api com nome de api e fica na raiz. sendo assim api:app. Caso queira alterar para uma pasta mais elaborada ou qualquer outro nome é preciso alterar este arquivo também.

```
web: gunicorn api:app
```

## Iniciar a api localmente
Para executar a api localmente apenas com python basta rodar o comando

```
python app.py
```

Com isso você pode verificar sua api rodando normalmente no endereço, http://localhost:5000


## Add plugin do postgres
