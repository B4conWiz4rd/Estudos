<?php

$numero = $argv[1];
$nomeDaFuncao = 'ex' . $numero;

echo "========================================\n";
echo "   Executando o Exercício $numero\n";
echo "========================================\n\n";

$nomeDaFuncao(); 

echo "\n========================================\n";


// ÁREA DOS EXERCÍCIOS: Funções com a lógica de cada questão
// ==============================================================================

function ex1() {
    echo "Olá, Mundo!\n";
}

function ex2() {
    $nome = readline("Qual é o seu nome? ");
    echo "Olá $nome, é um prazer te conhecer!\n";
}

