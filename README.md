# Django Blog

Este repositório contém um projeto desenvolvido durante o curso de Python
do [Otávio Miranda](https://www.otaviomiranda.com.br/). 
O projeto consiste em um blog construído com o framework Django,
explorando conceitos essenciais de desenvolvimento web com Python.

## 🚀 Funcionalidades
- Criar, editar e excluir posts.
- Gerenciamento de usuários.
- Sistema de autenticação e autorização.
- Interface amigável e responsiva.

## 🛠️ Tecnologias utilizadas
- **Python**  
- **Django**  
- **HTML/CSS**  
- **Bootstrap** (opcional para estilização)

## 📦 Como usar
1. Clonar o Repositório
Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/Merctxt/Django-blog.git
   cd Django-blog

<br>

2. Construir e Iniciar os Containers com Docker
Certifique-se de que o Docker está instalado e funcionando. Depois, execute:
   ```bash
   docker-compose up --build

Este comando irá construir as imagens necessárias e iniciar os serviços definidos no arquivo docker-compose.yml e no DockerFile.

<br>

3. Acessar a Aplicação
Após iniciar os containers, acesse a aplicação no navegador:
   ```bash
   http://127.0.0.1:8000/

<br>

4. Executar Migrações (se necessário)
Caso precise aplicar migrações no banco de dados, utilize:
   ```bash
   docker-compose exec web python manage.py migrate

<br>

5. Criar um Superusuário (para acessar o admin)
Para criar um usuário administrador, execute:
   ```bash
   docker-compose exec web python manage.py createsuperuser

<br>

6. Parar os Containers
Para parar os serviços, use:
   ```bash
   docker-compose down

📝 Licença

Este projeto é licenciado sob a Licença MIT.
