<script>
import { onMount } from 'svelte';
import PersonItem from './PersonItem.svelte';
let results = $state(null);
let debug = $state(false);

async function getArtists() {
    const endpoint = `http://localhost:8000/save/person`;
    const response = await fetch(endpoint);
    const data = response.json();
    if (response.ok) {
        return data;
    } else {throw new Error(data); }
  }

onMount(() => {
    getArtists().then((data)=>{
        results = data["persons"]; 
    });
});


function removePerson(removedId) {
  results = results.filter(person  => person.id !== removedId);
}
</script>

<main>

    <h1>Celebridades favoritas</h1>
    
    {#if results}
        <div class="results">
            {#each results as person }
                <PersonItem {person} onRemove={removePerson}/>
            {/each}
        </div>
    {/if}
    
</main>

<style>
main{
    padding: 10px;
}
.results{
    display: flex;
    gap: 10px;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: flex-start;
}
</style>