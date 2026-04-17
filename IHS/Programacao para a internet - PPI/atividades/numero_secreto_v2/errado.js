// é possivel fazer com que o JS modifique o HTML, com o ".innerHTML"
//let titulo = document.querySelector('h1');
//titulo.innerHTML = 'Jogo do número secreto';

//let paragrafo = document.querySelector('p');
//paragrafo.innerHTML = 'Escolha um número de 1 a 10';

//====================================================//

//essa linha serve para otimizar o código a cima, definimos função nomeada como "exibir mensagem inicial" utilizando o .quarySelector, perceba também as variáveis definidas, o tag que a gente vai definir e o texto que a gente quer.
function exibirMensagemInicial(tag, texto) {
    let campo = document.querySelector(tag)
    campo.innerHTML = texto;
};
//aqui nós puxamos a definição definida, e as informações, a primeira sendo a tag e em seguida o texto desejado.
exibirMensagemInicial('h1', 'Jogo do Número Secreto');
exibirMensagemInicial('p', 'Escolha um número de 1 a 10');

//****************************************************//
let tentativa = 1;
numeroSecreto = gerarNumeroSecreto;

function gerarNumeroSecreto(){
    //o return VOLTA oque você definiu, neste caso vai mudar para a variável "numeroSecreto"
    return parseInt (Math.random() * 10 + 1);
};

// atribui funcão a algo, neste caso, o botão presente na linha 17 do html. Perceba que foi definida uma variável chamado chute (linha 29) que pegar o valor posto no site, com ele será possivel verificar e válidar se o número é correto.
function verificarChute() {
    let chute = document.querySelector('input').value;

    if (chute == numeroSecreto) {
        
        exibirMensagemInicial('h1', 'Parabéns, acertou o número secreto!');
        
        let palavraTentativas = tentativa == 1 ? `tentativa`: `tentativas`;  
        let msgTentativa = `Você acertou o número secreto (${numeroSecreto}), com ${tentativa} ${palavraTentativas}!`;
        
        exibirMensagemInicial('p', msgTentativa);
    }

    else {
        tentativa++;

        if (chute > numeroSecreto) {
            exibirMensagemInicial('h1', 'Que pena, você errou!');
            exibirMensagemInicial('p', 'O número inserido é maior que o número secreto');
        } else {
            exibirMensagemInicial('h1', 'Que pena, você errou!');
            exibirMensagemInicial('p', 'O número inserido é menor que o número secreto');
        }
    };
};

function limparInput(){
    chute = document.querySelector('input');
    chute.innerHTML = '';
}
