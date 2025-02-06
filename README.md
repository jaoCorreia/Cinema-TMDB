# 🎬 Cinema-TMDB

Um aplicativo web para encontrar filmes populares e buscar artistas pelo nome, além de permitir salvar favoritos no MongoDB. O front-end foi desenvolvido em **Svelte**, e o back-end utiliza **FastAPI** com **MongoDB**.

## 🚀 Tecnologias Utilizadas

- **Front-end:** Svelte
- **Back-end:** FastAPI (Python)
- **Banco de Dados:** MongoDB
- **API de Filmes:** [TMDB API](https://www.themoviedb.org/)
- **Gerenciamento de Dependências:** npm (frontend) e pip (backend)

## 📌 Funcionalidades

- Buscar filmes populares
- Pesquisar artistas pelo nome
- Salvar filmes/artistas favoritos no banco de dados MongoDB
- Interface responsiva e intuitiva

---

## 📦 Como Rodar o Projeto

### 1️⃣ Configurar o Backend (FastAPI)

1. Clone o repositório:
   ```bash
   git clone https://github.com/jaoCorreia/Cinema-TMDB.git
   cd movie-finder
   ```
2. Entre na pasta do backend:
   ```bash
   cd backend
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure as variáveis de ambiente:
   Crie um arquivo **.env** dentro da pasta `backend/` e adicione:
   ```env
   MONGO_URI=mongodb://localhost:27017/movie_finder
   TMDB_API_KEY=SUA_CHAVE_TMDB
   ```
6. Execute o backend:
   ```bash
   uvicorn main:app --reload
   ```
   O servidor estará rodando em: **http://127.0.0.1:8000**

---

### 2️⃣ Configurar o Frontend (Svelte)

1. Volte para a raiz do projeto e entre na pasta do frontend:
   ```bash
   cd ../frontend
   ```
2. Instale as dependências:
   ```bash
   npm install
   ```
3. Configure a URL da API no arquivo `.env` dentro de `frontend/`:
   ```env
   VITE_API_URL=http://127.0.0.1:8000
   ```
4. Rode o projeto:
   ```bash
   npm run dev
   ```
   O frontend estará acessível em **http://localhost:5173**

## 📝 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para contribuir! 🎥🍿
