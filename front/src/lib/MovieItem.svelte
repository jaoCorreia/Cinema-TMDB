<script>
    import { onMount } from "svelte";
    let {movie, onRemove} = $props();
    let savedMovie = $state(null);
    
    async function remove() {
        const endpoint = `http://localhost:8000/remove/movie/${movie.id}`;
        const settings = {
            method: 'DELETE',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            }};
        const res = await fetch(endpoint, settings);
        if(res.ok) {
            alert("REMOVIDO");
            onRemove(movie.id);
        } else {
            const data = res.json();
            alert("Erro ao remover: " + JSON.stringify(data));
        }
    }
    async function save() {
        const endpoint = `http://localhost:8000/save/movie`;
        const settings = {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(movie)
        };
        const res = await fetch(endpoint, settings);
        const data = res.json();
        if (res.ok) {
            savedMovie = data;
            return data;
        }else if(res.status == 409){
            alert("Filme já está favoritado");
        }
        else {throw new Error(data); }
      }
    </script>
    
    <main class="movie-card" >
        {#if movie?.poster_path }
            <p><img src="https://image.tmdb.org/t/p/w185/{movie.poster_path}" alt="{movie.title}"></p>
        {/if}
        <div>
            {#if !movie?.is_fav }
                <button onclick={save}>Salvar</button>
            {/if}
            {#if movie.is_fav }
                <button onclick={remove}>Remover</button>
            {/if}
            {#if savedMovie }
                <span>Movie saved</span>
            {/if}
            <h2 class="movie-title">{ movie?.title }</h2>
            <p class="movie-release">Lançamento: {new Date(movie.release_date).toLocaleDateString('pt-br')}</p>
            <p class="movie-id">{ movie._id}</p>
        </div>
    </main>
     
<style>
   .movie-card {
    background: #1a1a1a; /* Fundo preto elegante */
    color: #fff; /* Texto branco */
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(255, 102, 0, 0.3); /* Sombra laranja */
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    max-width: 300px;
    max-width: 50%;
    transition: transform 0.3s ease-in-out;
}

.movie-card:hover {
    transform: scale(1.05);
}

.movie-card img {
    border-radius: 8px;
    width: 100%;
    max-width: 185px;
    height: auto;
    margin-bottom: 15px;
    transition: opacity 0.3s;
}

.movie-card img:hover {
    opacity: 0.8;
}

.movie-title {
    font-size: 1.4em;
    font-weight: bold;
    color: #ff6600; /* Laranja vibrante */
    margin-bottom: 10px;
}

.movie-release {
    font-size: 0.9em;
    color: #ccc; /* Texto secundário */
    margin-bottom: 8px;
}

.movie-id {
    font-size: 0.8em;
    color: #777;
    margin-top: 5px;
}

button {
    background: #ff6600; /* Laranja vibrante */
    color: #fff;
    border: none;
    padding: 10px 15px;
    margin: 5px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1em;
    font-weight: bold;
    transition: background 0.3s, transform 0.2s;
}

button:hover {
    background: #cc5200; /* Laranja escuro */
    transform: scale(1.05);
}

button:active {
    transform: scale(0.95);
}

span {
    color: #0f0;
    font-weight: bold;
    margin-top: 10px;
}

</style>
    