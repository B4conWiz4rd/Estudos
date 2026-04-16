function validar(){

    let nome = document.getElementById('idnome').value;
    let idade = document.getElementById('ididade').value;
    let saldDisp = document.getElementById('idsaldodisp').value;
    
    let resultado = document.getElementById('resultado');

    let mensagemDeErro = ('Erro! Preencha todos os campos.')

    if (nome == '') {
        alert (mensagemDeErro)
    } else if (idade == '') {
        alert (mensagemDeErro)
    } else if (saldDisp == '') {
        alert (mensagemDeErro)
    } else {
    resultado.innerHTML = `<p id="resultado">
    <br>Nome: ${nome}
    <br>Idade: ${idade}
    <br>Saldo: ${saldDisp} tupinicoins
    </p>`
    };
}