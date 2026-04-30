<?php

class serie extends Titulo
{
    private array $notas;

    public function __construct(
        string $nome,
        int $anoLancamento,
        Genero $genero,

        public readonly int $temporadas,
        public readonly int $qtdEpTemp,
        public readonly int $duracaoEp,
    ) {
        parent::__construct($nome, $anoLancamento, $genero);
    }

    public function duracaoEmMinutos(): int{
        return $this->temporadas * $this->qtdEpTemp * $this->duracaoEp;
    }
}
