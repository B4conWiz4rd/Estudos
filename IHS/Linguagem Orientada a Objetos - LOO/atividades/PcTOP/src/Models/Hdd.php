<?php
class Hdd extends DefineComponente
{
    #[Override]
    public function __construct(
        string $tipoModelo,
        NomeMarca $marca,
        public readonly int $qtdArmazenamento
    ) {
        return parent::__construct($tipoModelo, $marca);
    }
}