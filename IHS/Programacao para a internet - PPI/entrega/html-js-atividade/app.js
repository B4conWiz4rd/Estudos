//=====Interação com HTML=====

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
  let nomeCidade = prompt('Qual o nome da sua cidade?')
  alert(`Estivem em ${nomeCidade} e lembrei de você!`)
}

function ex005() {
  alert('Calculadora de somatório')
  let primeiroNum = parseInt(prompt('O primeiro número natural (ex: 1, 2, 30)'))
  let segundoNum = parseInt(prompt('O segundo número natural (ex: 1, 2, 30)'))
  let resultado = primeiroNum + segundoNum
  alert(`A soma de ${primeiroNum} mais ${segundoNum} resulta em ${primeiroNum + segundoNum}.`)
}

//=====Funcões=====

function ex006() {
  function digaOla() {
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
  let resultadoEx8 = document.querySelector('#outputEx08')
  resultadoEx8.innerHTML = dobro
}

function ex009() {
  let ex09NumA = parseInt(document.querySelector('#inputEx09-numA').value)
  let ex09NumB = parseInt(document.querySelector('#inputEx09-numB').value)
  let ex09NumC = parseInt(document.querySelector('#inputEx09-numC').value)

  let ex09media = (ex09NumA + ex09NumB + ex09NumC) / 3

  let resultadoEx9 = document.querySelector('#outputEx09')
  resultadoEx9.innerHTML = ex09media
}

function ex010() {
  let ex10NumA = parseInt(document.querySelector('#inputEx10-numA').value)
  let ex10NumB = parseInt(document.querySelector('#inputEx10-numB').value)
  let resultadoEx10 = document.querySelector('#outputEx10')

  if (ex10NumA > ex10NumB) {
    resultadoEx10.innerHTML = `O número ${ex10NumA} é MAIOR que ${ex10NumB}`
  } else if (ex10NumA == ex10NumB) {
    resultadoEx10.innerHTML = `Os números ${ex10NumA} e ${ex10NumB} são IGUAIS`

  } else {
    resultadoEx10.innerHTML = `O número ${ex10NumA} é MENOR que ${ex10NumB}`
  }
}

function ex011() {
  let ex11NumA = parseInt(document.querySelector('#inputEx11-numA').value)
  let resultadoEx11 = document.querySelector('#outputEx11')

  resultadoEx11.innerHTML = ex11NumA ** 2
}

function ex012() {
  let ex12NumA = parseFloat(document.querySelector('#inputEx12-numA').value)
  let ex12NumB = parseFloat(document.querySelector('#inputEx12-numB').value)

  let resultadoIMC = ex12NumA / (ex12NumB * ex12NumB)

  let resultadoEx12 = document.querySelector('#outputEx12')

  resultadoEx12.innerHTML = resultadoIMC

}

function ex013() {
  let ex13NumA = parseInt(document.querySelector('#inputEx13-numA').value)
  let resultadoEx13 = document.querySelector('#outputEx13')

  let resultado = 1

  for (let i = 1; i <= ex13NumA; i++) {
    resultado *= i;
  }

  resultadoEx13.innerHTML = resultado
}

function ex014() {
  let ex14Num = parseFloat(document.querySelector('#inputEx14-numA').value)
  let resultadoEx14 = document.querySelector('#outputEx14')

  resultadoEx14.innerHTML = ex13Num * 4.80
}

function ex015() {
  //largura
  let ex15NumA = parseFloat(document.querySelector('#inputEx15-numA').value)
  //altura
  let ex15NumB = parseFloat(document.querySelector('#inputEx15-numB').value)

  let resultadoEx15 = document.querySelector('#outputEx15')

  let area = ex15NumA * ex15NumB;
  let perimetro = 2 * (ex15NumA + ex15NumB);

  resultadoEx15.innerHTML = `Área ${area}, Perimetro ${perimetro}`
}

function ex016() {
  let pi = 3.14;
  //raio
  let ex16NumA = parseFloat(document.querySelector('#inputEx16-numA').value)
  let resultadoEx16 = document.querySelector('#outputEx16')
  area = pi * (ex16NumA ** 2);
  perimetro = 2 * pi * ex16NumA;
  resultadoEx16.innerHTML = `Área ${area} m², Perimetro ${perimetro}m.`
}

function ex017() {
  let ex17NumA = parseInt(document.querySelector('#inputEx17-numA').value)
  let resultadoEx17 = document.querySelector('#outputEx17')

  let ex17resultado = "<br>";

   for (let i = 1; i <= 10; i++) {
    let ex17calculo = ex17NumA * i;
    ex17resultado += ex17NumA + "x" + i + "=" + ex17calculo + "<br>"
  }
  resultadoEx17.innerHTML = ex17resultado
}

//=====Arrays e Funções=====