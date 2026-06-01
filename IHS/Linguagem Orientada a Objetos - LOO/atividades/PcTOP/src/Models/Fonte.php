<?php
class Fonte extends DefineComponente
{
    public function __construct(
        string $tipoModelo,
        NomeMarca $marca,
        public readonly int $totalCapacidade
    ) {
        return parent::__construct($tipoModelo, $marca);
    }
}
