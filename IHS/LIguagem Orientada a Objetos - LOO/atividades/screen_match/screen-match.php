<?php

    $nomeFilme = 'Top Gun - Maverick';  //String
    $anoLancamento = 2022;              //Int
    $somaNotas = (9+6+8+7.5+5)  /5;     //Soma de Valores em Variáveis
    $notaFilme = $somaNotas;            //Float
    $incluidoNoPlano = true;            //Bool
    
    //No php a variável é definida automaticamente

    echo "\nBem Vindo ao Screen Match\n";

    echo "\nNome do Filme: $nomeFilme\n";
    echo 'Ano do Filme: ' .$anoLancamento ."\n";    //Concatenando
    echo "Nota do Filme: $notaFilme\n";
    echo "Incluido no plano: $incluidoNoPlano\n";