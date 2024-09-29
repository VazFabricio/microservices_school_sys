# Usar uma imagem base do Python
FROM python:3.10.12

# Atualizar pacotes e instalar o cliente MySQL
RUN apt-get update && apt-get install -y default-mysql-client

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos e instalar as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta que o FastAPI usará
EXPOSE 9050

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9050", "--reload"]
