<?php

    require __DIR__ . '/src/Model/CatergoriaEletronico.php';
    require __DIR__ . '/src/Model/Produto.php';
    require __DIR__ . '/src/Model/Geladeira.php';
    require __DIR__ . '/src/Model/Smartphone.php';
    require __DIR__ . '/src/Services/CalculadoraDeFrete.php';

    // Instanciando os veiculos
    $meuSmartphone = new Smartphone ("Poco x1", 700, catergoriaEletronico::TELEFONIA, 5);
    $meuEletrodomestico = new Geladeira("Eletrolux", 3000, CatergoriaEletronico::ELETRODOMESTICO, 12);

    $calculadora = new CalculadoraDeFrete();

    // Calculando o imposto

    $calculadora->calcularFrete($meuSmartphone);
    $calculadora->calcularFrete($meuEletrodomestico);

    echo "Total de impostos a pagar da frota: R$ " . $calculadora->getTotal();