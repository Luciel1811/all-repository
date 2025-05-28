
const hacerAlgo = () => {
    const numero_1 = document.getElementById('numero_1')
    const numero_2 = document.getElementById('numero_2')
    try {
        const resultado = parseFloat(numero_1.value) + parseFloat(numero_2.value)
        
        document.getElementById('id_resultado').value = Number(resultado)
    } catch (error) {
        alert(`el error es: ${error}`)
    }

    //asfdhjasfdhjasfd
}


const ul = document.getElementById("myList");
let coders = ['Juanito', 'Isabella', 'Luis', 'Carlos', 'Antonio']
for(let i=0; i<5; i++){
    let li = document.createElement("li");
    li.appendChild(document.createTextNode(coders[i]));
    ul.appendChild(li);
}