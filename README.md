# PRISMA

Gráfica online desenvolvida em Django como projeto final da disciplina **WEB III** (FATEC).

🔗 **Site publicado:** https://danifeitozaalves.pythonanywhere.com

## Funcionalidades

**Área pública**
- **Home:** apresentação da empresa e do sistema.
- **Quem Somos:** integrantes da equipe, lidos de um banco remoto no **Supabase**.
- **Produtos:** serviços cadastrados no banco local, com botão **Comprar** (somente para usuários logados), e produtos de uma **API externa** (catálogo público da Printful).
- **Contato:** formulário para envio de mensagens, sem necessidade de login.
- **Entrar:** login, cadastro de novo usuário e recuperação de senha pelo mecanismo nativo do Django.

**Área restrita**
- Login de **administrador** redireciona para o painel `/admin` do Django.
- Login de **cliente** redireciona para a **Dashboard**, com:
  - **Editar Perfil** e **Alterar Senha**
  - **Contatos:** mensagens recebidas, com exclusão
  - **Serviços:** busca, filtros, estatísticas e CRUD completo
  - **Equipe:** CRUD dos integrantes no Supabase
  - **Meus Pedidos:** serviços comprados e total
  - **Relatórios:** indicadores e gráficos (Chart.js)

## Tecnologias

- Python 3.13 e Django 6.1
- Django REST Framework
- SQLite (banco local)
- Supabase (banco remoto)
- Requests (consumo de API externa)
- Chart.js (gráficos)
- PythonAnywhere (hospedagem)

## Estrutura

| App | Responsabilidade |
|---|---|
| `app` | Home, Quem Somos, Produtos, Serviços, Equipe, Meus Pedidos e Relatórios |
| `contato` | Formulário e gerenciamento de contatos |
| `login` | Autenticação, cadastro, perfil, Dashboard e recuperação de senha |
| `projeto` | Configurações e rotas principais |

## Como rodar localmente

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse http://127.0.0.1:8000.

Para criar um administrador: `python manage.py createsuperuser`.

> Os e-mails de recuperação de senha são exibidos no terminal (`EMAIL_BACKEND` de console).
