<?php

class Filme
{
    //Atributos nome: string, anoLancamento: int, genero: string
    //notas: array (ela não é criada pela função construtora)

    //Atributos
    private array $notas;

    public function __construct(
        public readonly string $nome,
        public readonly int $anoLancamento,
        public readonly Genero $genero,
        public readonly int $duracaoEmMinutos
    ) {
        $this->notas = [];
    }
    //alt + shift + f (aninha o codigo sozinho)
    //Métodos
    public function avaliar(float $nota): void //Metodo Setter
    {
        $this->notas[] = $nota;
    }

    public function media(): float
    {
        $somaNotas = array_sum($this->notas);
        $quantidadeNotas = count($this->notas);

        return $somaNotas / $quantidadeNotas;
    }
}
