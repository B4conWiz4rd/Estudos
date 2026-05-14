function calcularFatorial() {
  
  let resultado = 1;
  let numero = 5;
  
  for (let i = numero; i >= 1; i--) {
    resultado *= i;
  }
  
  alert (resultado);
}

function ex001() {
  let titulo = document.querySelector('h1');
  titulo.innerHTML = 'Hora do Desafio';
}

function ex002() {
  console.log('O botão foi pressionado')
}

function ex003() {
  alert('Eu <3 JavaScript')
}

function ex004() {
  let nomeCidade = prompt ('Qual o nome da sua cidade?')
  alert (`Estivem em ${nomeCidade} e lembrei de você!`)
}

function ex005() {
  alert ('Calculadora de somatório')
  let primeiroNum = parseInt(prompt ('O primeiro número natural (ex: 1, 2, 30)'))
  let segundoNum = parseInt(prompt ('O segundo número natural (ex: 1, 2, 30)'))
  let resultado = primeiroNum + segundoNum
  alert(`A soma de ${primeiroNum} mais ${segundoNum} resulta em ${primeiroNum + segundoNum}.`)
}

function ex006() {
  function digaOla(){
    return console.log('Olá Mundo')
  }

  let saudacao = digaOla()
}

function ex007() {
  let definirNome = document.querySelector('#inputEx07').value;
  function retornaNome() {
    return console.log(`Olá, ${definirNome}`)
  }

  let saudacao = retornaNome()
}

function ex008() {
  let definirNumero = parseInt(document.querySelector('#inputEx08').value);
  function multiplica() {
    let dobro = definirNumero * 2
  }
  let mostraResultado = document.querySelector('#resultado-dobro--ex02');
  mostraResultado.innerHTML = multiplica()
}

function ex009() {
  
}