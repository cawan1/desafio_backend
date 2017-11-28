# desafio_backend
Desafio_backend - API

#https://bitbucket.org/idexoteam/desafio-backend

Desenvolver API Produtos, carrinho de compras, e checkout. 

O desafio não completo.  :(


Infos:
 - Utilizado Python -> Django -> Djangorestframework
 - Gestão de pacotes via pipenv
 - Dados persistidos em banco de dados local sqlite3
 - Repositoro para Pull Request https://github.com/cawan1/desafio_backend

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Funionalidades desenvolvidas:
 - Adicionar/Remover Produtos (contendo atributos: Nome, Descrição, Imagem, Valor e Fator. Existem três fatores A, B e C.) - Gerenciado por Users
 - Adicionar/Remover produtos do carrinho - Gerenciado por Users
 - Browsable

Falta:
 - Aplicar regras de desconto no carrinho
 - Realizer Ckout com pagar.me


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Passos para instalação:
 1 - pip install pipenv 
 2 - git clone https://github.com/cawan1/desafio_backend
 3 - pipenv install
 4 - pipenv shell
 5 - python manage.py makemigrations
 6 - python manage.py migrate
 7 - python manage.py createsuperuser
 8 - python manage.py runserver 0.0.0.0:5000

Passos para execução:

Listar Produtos
 curl -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/produtos/
Adicionar Produto 
 curl -u username:password -H "Content-Type: application/json" -X POST -d '{"nome" : "Produto1", "descricao" : "Produto muito bom.", "valor" : "200", "fator": "A"}' http://127.0.0.1:5000/produtos/
Remover Produto
 curl -u username:password -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/produtos/1/
Editar Produto
 curl -u username:password -H "Content-Type: application/json" -X PUT -d '{"nome" : "Produto2", "descricao" : "Produto muito ruim.", "valor" : "100", "fator": "A"}' http://127.0.0.1:5000/produtos/1/


Listar Carrinho
 curl -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/carrinho/
Adicionar ItemCarrinho
 curl -u username:password -H "Content-Type: application/json" -X POST -d '{"item": [ "http://127.0.0.1:5000/produtos/2/" ], "quantidade": 1}' http://127.0.0.1:5000/itemscarrinho/
 curl -u username:password -H "Content-Type: application/json" -X POST -d '{"items": ["http://127.0.0.1:5000/itemscarrinho/1/"]}' http://127.0.0.1:5000/carrinhos/
Remover ItemCarrinho
 curl -u username:password -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/itemscarrinho/1
Remover Carrinho
 curl -u username:password -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/carrinhos/1




-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#SCHEMA
```json
{
    "_meta": {
        "title": "Pastebin API",
        "url": "http://127.0.0.1:5000/schema/"
    },
    "_type": "document",
    "carrinhos": {
        "list": {
            "_type": "link",
            "action": "get",
            "description": "ViewSet para o Carrinho",
            "url": "/carrinhos/"
        },
        "read": {
            "_type": "link",
            "action": "get",
            "description": "ViewSet para o Carrinho",
            "fields": [
                {
                    "location": "path",
                    "name": "id",
                    "required": true,
                    "schema": {
                        "_type": "integer",
                        "description": "A unique integer value identifying this carrinho.",
                        "title": "ID"
                    }
                }
            ],
            "url": "/carrinhos/{id}/"
        }
    },
    "itemscarrinho": {
        "list": {
            "_type": "link",
            "action": "get",
            "description": "ViewSet para ItemCarrinho",
            "url": "/itemscarrinho/"
        },
        "read": {
            "_type": "link",
            "action": "get",
            "description": "ViewSet para ItemCarrinho",
            "fields": [
                {
                    "location": "path",
                    "name": "id",
                    "required": true,
                    "schema": {
                        "_type": "integer",
                        "description": "A unique integer value identifying this item carrinho.",
                        "title": "ID"
                    }
                }
            ],
            "url": "/itemscarrinho/{id}/"
        }
    },
    "produtos": {
        "list": {
            "_type": "link",
            "action": "get",
            "description": "ViewSet para o Produto, acoes - list, create, retrieve, update, and detroy.",
            "url": "/produtos/"
        },
        "read": {
            "_type": "link",
            "action": "get",
            "description": "ViewSet para o Produto, acoes - list, create, retrieve, update, and detroy.",
            "fields": [
                {
                    "location": "path",
                    "name": "id",
                    "required": true,
                    "schema": {
                        "_type": "integer",
                        "description": "A unique integer value identifying this produto.",
                        "title": "ID"
                    }
                }
            ],
            "url": "/produtos/{id}/"
        }
    },
    "users": {
        "list": {
            "_type": "link",
            "action": "get",
            "description": "This viewset automatically provides list and detail actions.",
            "url": "/users/"
        },
        "read": {
            "_type": "link",
            "action": "get",
            "description": "This viewset automatically provides list and detail actions.",
            "fields": [
                {
                    "location": "path",
                    "name": "id",
                    "required": true,
                    "schema": {
                        "_type": "integer",
                        "description": "A unique integer value identifying this user.",
                        "title": "ID"
                    }
                }
            ],
            "url": "/users/{id}/"
        }
    }
}
```
