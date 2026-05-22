<?php
abstract class MaterialDidatico
{
    public function __construct(
        public readonly string $titulo,
        public readonly int $anoPublicacao,
        public readonly EstadoConservacao $estadoConcervacao,
    ) {}

    abstract function calcularDiasEmprestimo(): float;
}
