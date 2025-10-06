# 7 Days of Code: Python e Django (Alura)

![Status](https://img.shields.io/badge/Status-Concluído-green)
![Linguagem](https://img.shields.io/badge/Linguagem-Python-blue)
![Framework](https://img.shields.io/badge/Framework-Django-darkgreen)

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como resultado do desafio [**#7DaysOfCode** da Alura](https://7daysofcode.io/matricula/python-web), com foco na linguagem Python e no framework web Django. O objetivo foi construir uma aplicação web que consome uma [API do universo de "Avatar"](https://last-airbender-api.fly.dev/), trata os dados obtidos e os exibe em uma interface amigável e com paginação.

## ✨ Tecnologias Utilizadas

* **Python 3**
* **Django**
* **Requests** (para consumo da API)
* **Googletrans** (para tradução de dados)
* **Bootstrap** (para estilização do front-end)
* **Virtualenv** (para gerenciamento de ambiente)

## 📚 Desafios Diários

Este projeto foi construído em 7 dias, com um novo desafio a cada dia para adicionar funcionalidades à aplicação.

* **🔹 Dia 1:** Consumo da API de Avatar com o pacote `requests`.
    * *Resolução na branch: [desafio1](https://github.com/Leturnos/alura-django-7daysofcode/tree/desafio1)*
* **🔹 Dia 2:** Tratamento de dados e tradução com a biblioteca `googletrans`.
    * *Resolução na branch: [desafio2](https://github.com/Leturnos/alura-django-7daysofcode/tree/desafio2)*
* **🔹 Dia 3:** Primeiro contato com o framework Django e estrutura do projeto.
    * *Resolução na branch: [desafio3](https://github.com/Leturnos/alura-django-7daysofcode/tree/desafio3)*
* **🔹 Dia 4:** Criação de rotas e views, seguindo a arquitetura MVT.
    * *Resolução na branch: [desafio4](https://github.com/Leturnos/alura-django-7daysofcode/tree/desafio4)*
* **🔹 Dia 5:** Desenvolvimento de uma tabela visual com Bootstrap integrado ao Django.
    * *Resolução na branch: [desafio5](https://github.com/Leturnos/7daysofcode/tree/desafio5)*
* **🔹 Dia 6:** Geração de ID automático para os personagens no banco de dados do Django.
    * *Resolução na branch: [desafio6](https://github.com/Leturnos/alura-django-7daysofcode/tree/desafio6)*
* **🔹 Dia 7:** Implementação de paginação para exibir múltiplos personagens.
    * *Resolução na branch: [desafio7](https://github.com/Leturnos/alura-django-7daysofcode/tree/desafio7)*

*Observação: A branch `main` ou `master` contém o resultado final com todos os desafios concluídos.*

## 🚀 Rodando o Projeto

Siga os passos abaixo para executar a aplicação localmente.

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* [Python 3](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Leturnos/alura-django-7daysofcode.git
    ```

2.  **Acesse a pasta do projeto:**
    ```bash
    cd alura-django-7daysofcode
    ```

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar a venv
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no Linux/macOS
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute as migrações do banco de dados:**
    *(Este passo cria a estrutura do banco de dados que o Django precisa para funcionar)*
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse a aplicação:**
    Abra seu navegador e acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
