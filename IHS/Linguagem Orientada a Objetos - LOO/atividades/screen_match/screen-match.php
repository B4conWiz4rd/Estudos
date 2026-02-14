<?php

    $nomeFilme = 'Top Gun - Maverick';  //String
    //$nomeFilme = 'Thor: Ragnarok';
    //$nomeFilme = 'Se beber não case'
    $anoLancamento = $argv[2] ?? 2022;  //Int
    $somaNotas = (9+6+8+7.5+5)  /5;     //Soma de Valores em Variáveis
    $notaFilme = $somaNotas;            //Float
    $planoPrime = true;                 //Bool
    //No php a variável é definida automaticamente

    $genero = match ($nomeFilme) {
        'Top Gun - Maverick'    => 'Ação',
        'Thor: Ragnarok'        => 'Super-Heroi',
        'Se beber não case'     => 'Comédia',
        default                 => 'Não consta',
    };

    $incluidoNoPlano = $planoPrime || $anoLancamento < 2000;

    echo "\nBem Vindo ao Screen Match\n";

    echo "\nNome do Filme: $nomeFilme\n";
    echo 'Ano do Filme: ' .$anoLancamento ."\n";    //Concatenando
    echo "Nota do Filme: $notaFilme\n";
    echo "Incluido no plano: $incluidoNoPlano\n";
    echo "Gênero do filme: $genero\n";   


    //Estrutura de decisão

    if ($anoLancamento > 2022) {
        echo "Lançamento!\n";
    } elseif ($anoLancamento > 2020 && $anoLancamento <= 2022) {
        echo "Ainda é novo!";
    } else {
        echo "Não é lançamento.\n";
    }

    //Switch Case

    //switch ($variavel) {
    //case 1:
        //código...
        //break;
    //default:
        //código
        //break;
    //}