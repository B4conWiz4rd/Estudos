<?php

require __DIR__ . '/src/model/EstadoConservacao.php';
require __DIR__ . '/src/model/MaterialDidatico.php';
require __DIR__ . '/src/model/Livro.php';
require __DIR__ . '/src/model/RevistaCientifica.php';
require __DIR__ . '/src/service/VerificadorDeEmprestimo.php';

// Instanciando os veiculos
$meuLivro = new Livro("LOR, Sociedade do Anel", 1954, EstadoConservacao::BOM, 576);
$meuArtigo = new RevistaCientifica("Comer cocô é super estimado", 2001, EstadoConservacao::GASTO, 3);

$calculadora = new VerificadorDeEmprestimos();

// Calculando o tempo de empréstimo

$calculadora->tempoEmprestimo($meuLivro);
$calculadora->tempoEmprestimo($meuArtigo);

echo "Total de dias de empréstimo: " . $calculadora->getTotal();
