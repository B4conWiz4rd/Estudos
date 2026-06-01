<?php
    //Idealizamos que há de ter um veículo (para calcular o IPVA), definimos uma classe abstrata com outras variáveis que define a classe.
    abstract class Veiculo {
        public function __construct(
            //restrigimos as informações como estado publico, mas somente leitura. Para que informação seja disponível POREM não modificável.
            public readonly string $marca,
            public readonly string $modelo,
            public readonly int $anoFabricacao,
            public readonly TipoCombustivel $combustivel,
        ) {}
        //Já que a 
        abstract public function calcularTaxa(): float;
    }