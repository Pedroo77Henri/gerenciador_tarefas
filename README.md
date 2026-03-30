# Gerenciador de Tarefas

Projeto desenvolvido com o objetivo de estudar e demonstrar a evolução de uma aplicação Python,
partindo de um script simples até uma API completa com interface web.

---

## Evolução do projeto

### Nível 1 — Script com JSON (`legacy/`)
Aplicação de linha de comando utilizando funções, laços de repetição e armazenamento
em arquivo `.json`. Ponto de partida do projeto, focado na lógica básica.

### Nível 2 — API REST com FastAPI (`app/`)
Migração para uma API REST utilizando FastAPI e SQLAlchemy com banco de dados SQLite.
Implementação dos endpoints de criar, listar, atualizar e deletar tarefas,
com validação de dados via Pydantic.

### Nível 3 — Interface Web (`frontend/`)
Desenvolvimento de uma interface web em HTML, CSS e JavaScript puro consumindo a API
via `fetch()`. Visual minimalista e clean, com suporte a adicionar, concluir e remover tarefas
em tempo real.

---

## Tecnologias

- Python 3.11+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- HTML, CSS e JavaScript

---

## Como rodar localmente

### Pré-requisitos
- Python 3.11+
- pip

### 1. Clone o repositório

\`\`\`bash
git clone https://github.com/seu-usuario/gerenciador-tarefas.git
cd gerenciador-tarefas
\`\`\`

### 2. Crie e ative o ambiente virtual

\`\`\`bash
python -m venv .venv
\`\`\`

Windows:
\`\`\`bash
.venv\Scripts\activate
\`\`\`

Mac/Linux:
\`\`\`bash
source .venv/bin/activate
\`\`\`

### 3. Instale as dependências

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Suba o servidor

\`\`\`bash
uvicorn app.main:app --reload
\`\`\`

### 5. Abra o frontend

Abra o arquivo `frontend/index.html` no navegador com o Live Server do VS Code,
ou acesse diretamente pelo sistema de arquivos.

A documentação interativa da API estará disponível em:
\`\`\`
http://localhost:8000/docs
\`\`\`

---

## Estrutura do projeto

\`\`\`
gerenciador-tarefas/
├── app/
│   ├── schemas/
│   │   └── tarefa.py
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   └── models.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── legacy/
│   ├── main.py
│   └── tarefas.json
├── .gitignore
├── requirements.txt
└── tarefas.db
\`\`\`

---

## Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/tarefas/` | Lista todas as tarefas |
| POST | `/tarefas/` | Cria uma nova tarefa |
| PATCH | `/tarefas/{id}` | Atualiza título ou status |
| DELETE | `/tarefas/{id}` | Remove uma tarefa |

---

## Autor

Feito com dedicação como projeto de estudo e evolução em Python e desenvolvimento web.