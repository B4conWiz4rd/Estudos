<?php

    require __DIR__ . '/src/model/TipoCombustivel.php';
    require __DIR__ . '/src/model/Veiculo.php';
    require __DIR__ . '/src/model/Onibus.php';
    require __DIR__ . '/src/model/Carro.php';
    require __DIR__ . '/src/service/CalculadoraDeIPVA.php';

    // Instanciando os veiculos
    $meuCarro = new Carro ("Fiat", "Uno", 2020, TipoCombustivel::GASOLINA, 5);
    $meuOnibus = new Onibus("Mercedes-Benz", "0500", 2018, TipoCombustivel::DISEL, 40);

    $calculadora = new CalculadoraDeIPVA();

    // Calculando o imposto

    $calculadora->incluirNoCalculo($meuCarro);
    $calculadora->incluirNoCalculo($meuOnibus);

    echo "Total de impostos a pagar da frota: R$ " . $calculadora->getTotal();