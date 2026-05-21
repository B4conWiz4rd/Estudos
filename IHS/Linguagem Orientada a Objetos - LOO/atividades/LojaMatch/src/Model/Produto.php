<?php
    abstract class produto {
        public function __construct(
            public readonly string $nome,
            public readonly float $precoBase,
            public readonly CatergoriaEletronico $categoriaEletronico,
        ){}

        abstract function calcularTaxaEnvio();
    }