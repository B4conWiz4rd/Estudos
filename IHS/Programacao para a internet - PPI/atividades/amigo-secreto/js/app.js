let amigos = []
btSort = document.querySelector(".button secundary")

function adicionar() {
    //var
    let amigo = document.getElementById('nome-amigo');
    let lista = document.getElementById('lista-amigos');

    if ((amigo.value == '') || (amigos.includes(amigo.value))){
        alert('Nome inválido ou repetido')
    } else {
        if (lista.textContent == '') {

        lista.textContent = amigo.value;

        } else {

        lista.textContent = lista.textContent + ', ' + amigo.value;

        }
    };
    
    amigos.push(amigo.value);
    amigo = ''

};

function sortear() {
    function embaralha(lista) {

        let indice = lista.length

        while (indice) {
            // atenção para o pós-incremento indice-- 
            const indiceAleatorio = Math.floor(Math.random() * indice--);
            [lista[indice], lista[indiceAleatorio]] =
                [lista[indiceAleatorio], lista[indice]];
        }
    }

    embaralha(amigos);

    for (let i = 0; i < amigos.length; i++) {

        if (i == (amigos.length - 1)) {
            resultado.innerHTML = resultado.innerHTML + amigos[i] + '==>' + amigos[0] + '<br>'
        } else {
            resultado.innerHTML = resultado.innerHTML + amigos[i] + '==>' + amigos[i + 1] + '<br>'
        }
        
    }
};

function reiniciar() {
    amigos = ''

    let lista = document.getElementById('lista-amigos');
    let resultado = document.getElementById('lista-sorteio');

    
    lista.textContent = ''
    resultado.textContent = ''
};