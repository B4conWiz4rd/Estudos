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
  let dobro = definirNumero*2
  let resultadoEx8 = document.querySelector('#outputEx08')
  resultadoEx8.innerHTML = dobro
}

function ex009() {
  let ex09NumA = parseInt(document.querySelector('#inputEx09-numA').value)
  let ex09NumB = parseInt(document.querySelector('#inputEx09-numB').value)
  let ex09NumC = parseInt(document.querySelector('#inputEx09-numC').value)
  
  let ex09media = (ex09NumA+ex09NumB+ex09NumC)/3
  
  let resultadoEx9 = document.querySelector('#outputEx09')
  resultadoEx9.innerHTML = ex09media
}

function ex010() {
  let ex10NumA = parseInt(document.querySelector('#inputEx10-numA').value)
  let ex10NumB = parseInt(document.querySelector('#inputEx10-numB').value)
  let resultadoEx10 = document.querySelector('#outputEx10')

  if (ex10NumA > ex10NumB) {
    resultadoEx10.innerHTML = `O número ${ex10NumA} é MAIOR que ${ex10NumB}`
  }else if (ex10NumA == ex10NumB) {
    resultadoEx10.innerHTML = `Os números ${ex10NumA} e ${ex10NumB} são IGUAIS`

  }else {
    resultadoEx10.innerHTML = `O número ${ex10NumA} é MENOR que ${ex10NumB}`
  }
}

function ex011() {
  let ex11NumA = parseInt(document.querySelector('#inputEx11-numA').value)
  let resultadoEx11 = document.querySelector('#outputEx11')

  resultadoEx11.innerHTML = ex11NumA**2
}

function ex012() {
  let ex12NumA = parseInt(document.querySelector('#inputEx12-numA').value)
  
  for (let i = ex12NumA; i < 1; i--) {
    alert(i)
  }
}

function ex013() {
  
}