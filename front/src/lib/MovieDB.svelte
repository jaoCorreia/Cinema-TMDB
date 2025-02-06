<script>
    import { onMount } from "svelte";
    import MovieItem from "./MovieItem.svelte";
    let results = $state(null);
    async function getMovies() {
        let endpoint = `http://localhost:8000/save/movie`;
        const res = await fetch(endpoint);
        const data = await res.json();
        if (res.ok) {
            return data;
        }else {throw new Error(data); }
    }

    onMount(() => {
      getMovies().then((data)=>{
          results = data["movies"]; 
      });
    });
    
    function removeMovie(removedId) {
        results = results.filter(movie => movie.id !== removedId);
    }

</script>

<h1>Filmes Favorito</h1>
<div  class="results">
    {#if results}
        {#each results as movie}
            <MovieItem {movie} onRemove={removeMovie}/>
        {/each}
    {/if}
</div>
   
<style>

/* Centralizar e estilizar o título */
h1 {
	text-align: center;
	color: #ffb400;
	font-size: 2.5rem;
	margin-bottom: 1rem;
	font-family: Arial, sans-serif;
}

/* Botão estilizado */
button {
	background-color: #ff7e5f;
	color: #fff;
	padding: 10px 20px;
	font-size: 1rem;
	border: none;
	border-radius: 5px;
	cursor: pointer;
	transition: background-color 0.3s ease, transform 0.2s;
	margin: 10px auto;
	display: block;
	box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	font-family: Arial, sans-serif;
}

button:hover {
	background-color: #e0664c;
	transform: scale(1.05);
}

/* Container dos resultados */
.results {
	max-width: 800px;
	margin: 20px auto;
	padding: 20px;
	background-color: #2b2b2b;
	border-radius: 10px;
	box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
	color: #f4f4f9;
}

/* Estilizar os itens dos filmes */
.results p {
	font-size: 1.2rem;
	color: #fff;
	background-color: #1c1c1c;
	margin: 10px 0;
	padding: 15px;
	border-radius: 5px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
	transition: transform 0.2s ease, background-color 0.3s ease;
}

.results p:hover {
	background-color: #333;
	transform: scale(1.02);
}

/* Responsividade */
@media (max-width: 600px) {
	h1 {
		font-size: 2rem;
	}

	button {
		font-size: 0.9rem;
		padding: 8px 16px;
	}

	.results p {
		font-size: 1rem;
		padding: 10px;
	}
}


</style>