alert ("Boas vindas ao jogo do número secreto!");

//Var em JS

let tentativas
let dificuldade = Number(prompt (`
    Escolha a dificuldade desejada!\n
    1 - Sissy (5 tentativas)\n
    2 - Normal (3 tentativas)\n
    3 - Adivinha (1 tentativa)\n
    `));

switch (dificuldade) {
    case 1 : 
        tentativas = 5;
        break;

    case 2 : 
        tentativas = 3;
        break;

    case 3 :
        tentativas = 1;
        break;

    default :
        alert (`ERRO! A opção selecionada é inválida.`);

};

let numeroSecreto = 9 ;
let palpite;
let gameover = false;

while (tentativas >= 0) {

    let palpite = prompt(`Escolha um número de 1 a 10 você tem ${tentativas} tentativas.`)

    if (palpite == numeroSecreto){
        break
    }

    else if (tentativas == 0) {
        gameover = true
        break
    }

    else {              // É possivel colocar a função if/else dentro de if/else
        alert ("O seu palpite está errado :/")
        if (palpite > numeroSecreto) {
            tentativas --
            alert (`O seu palpite ${palpite} é maior que o número secreto!`);
            alert (`Tentativas restantes ${tentativas}`);
        }
        else {
            tentativas --
            alert (`O seu palpite ${palpite} é menor que o número secreto!`);
            alert (`Tentativas restantes ${tentativas}`);
        };
    };
};

if (gameover == true) {
// Operador Ternário
let palavraTentativas = tentativas == 1 ? `tentativa`: `tentativas`;
alert(`Você descobriu o número secreto (${numeroSecreto}), com ${tentativas} ${palavraTentativas}`)
}

else {
    alert(`Game Over!`)
}
//alert (`O seu palpite está correto! (${numeroSecreto})`); //Encrementar string!