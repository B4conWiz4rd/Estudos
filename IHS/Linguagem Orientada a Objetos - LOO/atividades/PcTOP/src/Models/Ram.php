<?php
    class Ram extends DefineComponente {
        public function __construct(
            string $tipoModelo,
            NomeMarca $marca,
            public readonly float $qtdTamanho
            ) {
            return parent::__construct($tipoModelo, $marca);
        }
    }