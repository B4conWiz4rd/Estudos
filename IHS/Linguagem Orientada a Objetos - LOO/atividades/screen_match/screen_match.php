<?php

require __DIR__ . "/src/funcoes.php";

echo "\nBem-vindo ao Screen Match!\n";

$nomeFilme = "Thor Ragnarok";
$anoLancamento = 2022;

$genero = match ($nomeFilme) {
    "Top Gun - Maverick" => "Ação",
    "Thor Ragnarok" => "Super Herói",
    "Se Beber não Case" => "Comédia",
    default => "Desconhecido",    
};

$quantidadeDeNotas = ($argc - 1) == 0 ? 1 : ($argc - 1); // Evita divisão por zero com o operado ternário

$notas =[];
for ($i = 1; $i < $argc; $i++){
    $notas[] = (float) $argv[$i];
}

$notaFilme = array_sum($notas) / $quantidadeDeNotas;

$planoPrime = true;

$incluidoNoPlano = incluidoNoPlano($planoPrime, $anoLancamento);

echo "Nome do Filme: " . $nomeFilme . "\n"; 
echo "Nota do Filme: $notaFilme\n";
echo "Ano de Lançamento: $anoLancamento\n";
echo "Incluido no Plano: $incluidoNoPlano\n";

exibeMensagemLancamento($anoLancamento);

echo "Genero do Filme: $genero\n";

$filme = criaFilme(

    nome : 'Thor: Ragnarok',
    ano : 2021,
    nota : 7.5,
    genero : 'Super-Herói'

);

echo $filme;

//var_dump($notas);
//sort($notas);
//var_dump($notas);
//$menorNota = min($notas);
//echo $menorNota;

//var_dump($filme['nome']);
//$posicaoDoisPontos = strpos($filme['nome'],':'); //os dois pontos estão na posicao 4
//var_dump($posicaoDoisPontos);
//var_dump(substr($filme['nome'], 0, $posicaoDoisPontos));

//Criando uma variável em que converte a variável $filme para um string em Json.
$filmeComoStringJson = json_encode($filme);

//Tem a função de mover o arquivo json na pasta raiz, nomeado como "fime.json"
file_put_contents(__DIR__ . '/filme.json', $filmeComoStringJson);
