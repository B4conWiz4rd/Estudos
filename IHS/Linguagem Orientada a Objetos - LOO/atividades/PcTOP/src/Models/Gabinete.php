<?php
    class Gabinete extends DefineComponente {
        public function __construct(
            string $tipoModelo,
            NomeMarca $marca,
            public readonly int $qtdFans

        ) {
            return parent::__construct($tipoModelo, $marca);
        }
    }