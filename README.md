## Requirements.txt
Salvar as depêndencias (bibliotecas) instaladas no virtual env:
```bash
pip freeze > requirements.txt
```

# CRIAR O VIRTUAL ENV:
# OPÇÃO 2 (máquina windows):
python -m venv env

# Ativar o ambiente virtual:
env/Scripts/activate

# instalar dependências
pip install -r requirements.txt

# Desativar o ambiente virtual:
deactivate