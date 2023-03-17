function doGenerate() {
    document.getElementById('progress').style.display = "block";
    const prompt= document.getElementById('prompt').value;
    document.getElementById('status').innerText ='';
    const model = document.getElementById('model').value;
    fetch(`/api/generate/${model}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            prompt
        })
    }).then(response => response.json())
        .then(result => {
            document.getElementById('prompt').value = result.generatedtext
            document.getElementById('progress').style.display = "none";
            document.getElementById('status').innerText = `Generated in ${result.generationtime} seconds by ${result.model} model`
        })
}
