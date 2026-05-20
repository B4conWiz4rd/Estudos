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
  let dobro = definirNumero * 2
  let resultadoEx8 = document.querySelector('#resultado-dobro')
  resultadoEx8.innerHTML = dobro
}

function ex009() {
  // (a + b + c) / 3
  let exer09NumA = parseInt(document.querySelector('#exer09-numA').value)
  let exer09NumB = parseInt(document.querySelector('#exer09-numB').value)
  let exer09NumC = parseInt(document.querySelector('#exer09-numC').value)

  let calcularMedia = (exer09NumA + exer09NumB + exer09NumC)/3

  let resultadoEx9 = document.querySelector('#resultado-media')
  resultadoEx9.innerHTML = calcularMedia
}

function ex010(){
  let exer10NumA = parseInt(document.querySelector('#exer10-numA').value)
  let exer10NumB = parseInt(document.querySelector('#exer10-numB').value)

  alert(exer10NumA)

}