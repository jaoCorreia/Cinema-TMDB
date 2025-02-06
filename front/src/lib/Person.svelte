<script>
    import Page from "../routes/+page.svelte";
    import PersonItem from "./PersonItem.svelte";

    let results = $state(null);
    let inputContent = $state('');
    let filter = $state(1);
    let error = $state(null)

    const getPersons = (data)=>{
        let [inputContent, filter] = data; 
        let endpoint = 'http://localhost:8000';
        if(filter == 2){
            endpoint+=`/person/${inputContent}`
        }else if(filter == 1){
            endpoint+=`/byname/person/${inputContent}`
        }
        let response = fetch(endpoint, {headers:{"Content-type":"application/json"}})
        .then(res => res.json()).then(data =>{
            return data;
        })
        return response
    }
    const handleClick = async () =>{
        if(inputContent == '' || inputContent == null){
            error = "Preencha todos os campos"
        }else{
            error = null;
            let data = await getPersons([inputContent,filter]);
            if(data['results']){
                results = data['results'].length ? data['results'] : "Nenhum resultado encontrado";
            }else{
                console.log(data.length)
                results = data ? [data] : "Nenhum resultado encontrado";
            }

        }
    }
</script>


<h1>Celebridades</h1>
<div >
    <p>Pesquise uma celebridade</p>
    {#if error }
        <p id="error">{error}</p>
    {/if}
    <input type={filter == 1 ? 'text' : 'number'}  onchange={(event) => inputContent = event.target.value} > 
    <select onchange={(event) => filter = (event.target.value)}>
        <option value=1 >Name</option>
        <option value=2>ID</option>
    </select>
    <button onclick={handleClick}>Search</button>
</div>

<div class="result">
    {#if results}
    {#each results as person}
        <PersonItem {person} />
    {/each}
    {/if}
</div>

<style>

h1 {
    text-align: center;
    color: #ffb400;
    font-size: 2.5rem;
    margin-bottom: 1rem;
    font-family: Arial, sans-serif;
}


div {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
}


p {
    font-size: 1.1rem;
    color: #aeaeae;
    font-family: Arial, sans-serif;
}


input, select {
    padding: 10px;
    font-size: 1rem;
    margin: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    background-color: #fff;
    width: 250px;
    font-family: Arial, sans-serif;
}


button {
    background-color: #ff7e5f;
    color: #fff;
    padding: 10px 20px;
    font-size: 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s;
    margin-top: 10px;
}

button:hover {
    background-color: #e0664c;
    transform: scale(1.05);
}


#error {
    color: #ff0000;
    font-size: 1rem;
    margin-top: 10px;
}

.result {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
}


.result div {
    background-color: #fff;  
    color: #333; 
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 250px;
    text-align: center;
    font-family: Arial, sans-serif;
    transition: transform 0.2s ease, background-color 0.3s ease;
}

.result div:hover {
    background-color: #f4f4f9; 
    transform: scale(1.05);
}


.result img {
    width: 150px;
    height: 150px;  
    border-radius: 50%;  
    margin-top: 10px;
}

.result p {
    font-size: 1.1rem;
    margin: 10px 0;
    color: #555;  
    line-height: 1.5;
}

.result p:nth-child(2) {
    font-weight: bold;
    font-size: 1.2rem;
    color: #222;  
}

.result p:nth-child(3),
.result p:nth-child(4) {
    font-size: 1rem;
    color: #777;  
}

@media (max-width: 600px) {
    h1 {
        font-size: 2rem;
    }

    input, select {
        width: 80%;
    }

    .result div {
        width: 100%;
    }

    .result img {
        width: 120px;  /* Ajuste do tamanho da imagem para telas pequenas */
        height: 120px;
    }

    .result p {
        font-size: 1rem;}

    button {
        font-size: 0.9rem;
        padding: 8px 16px;
    }
}

  </style>
  