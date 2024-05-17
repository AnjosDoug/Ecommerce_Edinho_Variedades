# Ecommerce_Edinho_Variedades

Projeto de loja virtual (E-commerce) desenvolvido a pedido do professor Naldo Santos para a disciplina de programação web.

## Descrição

Este projeto tem como objetivo criar uma loja virtual completa chamada Edinho Variedades. Utilizando tecnologias modernas e práticas de desenvolvimento web, o sistema oferece uma plataforma de comércio eletrônico robusta e fácil de usar.

## Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

## Requisitos

- Python 3.x
- Django 3.x
- MySQL Server

## Instalação e Configuração

1. Clone o repositório:

   ```
   git clone https://github.com/ArthurRibeir0/Ecommerce_Edinho_Variedades.git
   ```

2. Navegue até o diretório do projeto:

   ```
   cd Ecommerce_Edinho_Variedades
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
    - **No Windows:**
        ```
        python -m venv nome_do_ambiente
        ```
        ```
        nome_do_ambiente\Scripts\activate
        ```
    - **No macOS e Linux:**
        ```
        python3 -m venv nome_do_ambiente
        ```
        ```
        source nome_do_ambiente/bin/activate
        ```

4. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

5. Configure as informações do banco de dados MySQL no arquivo `settings.py`.

6. Abra o arquivo `settings.py` no diretório `Ecommerce_Edinho_Variedades`.

7. Localize a seção de configuração do banco de dados. Normalmente, está sob o comentário `# Database`.

8. Dentro dessa seção, você encontrará parâmetros como `DATABASES`. Configure-os da seguinte maneira para usar o MySQL:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nome_do_banco_de_dados',
            'USER': 'nome_de_usuario',
            'PASSWORD': 'senha_do_usuario',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

    Substitua `nome_do_banco_de_dados`, `nome_de_usuario` e `senha_do_usuario` pelos detalhes do seu banco de dados MySQL.

9. Salve o arquivo `settings.py`.

10. Execute as migrações do banco de dados:

   ```
   python manage.py migrate
   ```

11. Inicie o servidor:

   ```
   python manage.py runserver
   ```

## Uso

Após iniciar o servidor, você pode acessar a loja virtual através do navegador web usando o endereço `http://localhost:8000`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Contato

Para mais informações, entre em contato:

<a href="https://www.linkedin.com/in/arthur-ribeiro-peixoto-3b0096232/" target="_blank">![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)</a>
<a href="mailto:dev.arthur15@gmail.com">![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>
<a href="https://www.instagram.com/arthurr2415" target="_blank">![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)</a>
