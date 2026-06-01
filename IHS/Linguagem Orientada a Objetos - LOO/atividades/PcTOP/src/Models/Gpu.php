<?php
    class Gpu extends DefineComponente {
        public function __construct(
            string $tipoModelo,
            NomeMarca $marca,
            public readonly float $qtdClock
            ) {
            return parent::__construct($tipoModelo, $marca);
        }
    }