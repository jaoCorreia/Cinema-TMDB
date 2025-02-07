<script>
let {person, onRemove} = $props()
let savedPerson = $state(null);
    
    async function remove() {
        const endpoint = `http://localhost:8000/remove/person/${person.id}`;
        const settings = {
            method: 'DELETE',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            }};
        const res = await fetch(endpoint, settings);
        if(res.ok) {
            alert("REMOVIDO");
            onRemove(person.id);
        }else {
            const data = res.json();
            alert("Erro ao remover: " + JSON.stringify(data));
        }
    }
    async function save() {
        const endpoint = `http://localhost:8000/save/person`;
        const settings = {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(person)
        };
        const res = await fetch(endpoint, settings);
        const data = res.json();
        if (res.ok) {
            savedPerson = data;
            return data;
        }else if(res.status == 409){
            alert("Artista já está favoritado");
        } else {throw new Error(data); }
      }
    </script>


<div class="result">
    <div>
        <p>ID: {person ._id || person.id}</p>
        <p>Nome: {person.name}</p>  
        <p>Popularidade: {person.popularity}</p>  
        <p>Departamento: {person.known_for_department}</p>  
        <img style="width: 150px;" alt="profile" src="https://image.tmdb.org/t/p/w500/{person.profile_path}">
        {#if !person?.is_fav }
            <button onclick={save}>Salvar</button>
        {/if}
        {#if person.is_fav }
            <button onclick={remove}>Remover</button>
        {/if}
        {#if savedPerson }
            <span>Artista salvo</span>
        {/if}
    </div>
</div>

<style>

.result {
    background: #1a1a1a; 
    color: #fff; 
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(255, 102, 0, 0.3); 
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    max-width: 280px;
    transition: transform 0.3s ease-in-out;
}

.result:hover {
    transform: scale(1.05);
}

.result img {
    border-radius: 50%;
    width: 120px;
    height: 120px;
    object-fit: cover;
    margin-bottom: 15px;
    border: 3px solid #ff6600; 
    transition: opacity 0.3s, transform 0.3s;
}

.result img:hover {
    opacity: 0.9;
    transform: scale(1.08);
}

.result p {
    font-size: 1em;
    color: #ccc; 
    margin: 5px 0;
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