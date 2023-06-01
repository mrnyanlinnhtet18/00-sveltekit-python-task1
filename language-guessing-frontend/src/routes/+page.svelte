<script>
   let inputText = '';
   let language = '';

  
   export const submitInput = async ()=>{
        let url = 'http://127.0.0.1:5000/api/post'
      const response = await fetch(url, {
        method: 'POST',
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({inputText})
      });

      if (response.ok) {
      const data = await response.json();
      language = data.language;
    } else {
      console.error('Error:', response.status);
    }      
    }

  </script>
  
  <main>
    <h1>Guess the Language</h1>
    <p>Type some text below:</p>
    <form on:submit|preventDefault={submitInput}>
      <input type="text" bind:value={inputText} />
      <button type="submit">Submit</button>
    </form>
    {#if language}
      <p>That seems to be {language}!</p>
    {/if}
  </main>
  