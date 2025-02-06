# Credenciais
Credenciais devem ser armazenadas em um arquivo de configuração,
que não está rastreado pelo controle de versão ou seja compartilhado.

## Instalar biblioteca dotenv
Permite a leitura do arquivo .env de configuração
```
pip freeze > requirements.txt
p
```
```bash
pip install python-dotenv
```
```
pip install -r requirements.txt
```

## Importar token do ambiente 

```python
import os
import dotenv
dotenv.load_dotenv(".env")
token = os.environ["API_TOKEN"]
```

## Formato de URLs

### Query parameter
https://api.themoviedb.org/3/search/person?id=2000

### Url parameter 
https://api.themoviedb.org/3/search/person/2000

----

# API TMDB
- Cadastro no site para gerar a chave da API:
- https://www.themoviedb.org/settings/api

## Documentação
- https://developer.themoviedb.org/reference/intro/getting-started

### verifica qual o python esta sendo usado no terminal
```
which python
```

## Instalar biblioteca requests
```bash
pip install requests
```


# Criação de ambiente virtual 
## cria a pasta env (roda somente  uma vez)
```
python 3 -m venv env
```
## Ativar o ambiente
Ativa o ambiente para usar no projeto.

```bash
source env/bin/activate

# windows
.\env\scripts\activate
```
# instalar biblioteca requests 

```
pip install requests
```

# Servidor Web (FastAPI) 

```
pip install "fastapi[standard]" uvicorn
```

## Inicia o servidor 
# de forma rapida 
```
fastapi dev main.py
fastapi run main.py
uvicorn main:app
uvicorn main:app --reload
uvicorn main:app --reload --port=5000
 
```
# verificar todos os endpoints 
/docs

# motor 
pip install motor
# drive mongo
python -m pip install "pymongo[srv]"