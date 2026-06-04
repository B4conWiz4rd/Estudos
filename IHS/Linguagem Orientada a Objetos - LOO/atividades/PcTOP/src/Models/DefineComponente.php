<?php
abstract class DefineComponente {
    public function __construct(
        public readonly string $tipoModelo,
        public readonly NomeMarca $marca
    ) {}
    abstract function calcularValor();
}