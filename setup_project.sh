#!/bin/bash

# Cria e ativa o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instala as dependências necessárias
pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy databases asyncpg

# Gera o arquivo requirements.txt
pip freeze > requirements.txt