<?php
class Cpu extends DefineComponente
{
    public function __construct(
        string $tipoModelo,
        NomeMarca $marca,
        public readonly float $qtdClock,
        public readonly float $precoBase = 300
    ) {
        return parent::__construct($tipoModelo, $marca);
    }


    public function calcularValor(): float {
        return $this -> qtdClock + precoBase;
        }
}