<?php

class Filme extends Titulo
{
    private array $notas;

    public function __construct(
        string $nome,
        int $anoLancamento,
        Genero $genero,
        public readonly int $duracaoEmMinutos
    ) {
        parent::__construct($nome, $anoLancamento, $genero);
    }
    public function duracaoEmMinutos(): Int{
        return $this -> duracaoEmMinutos;
    }
}
