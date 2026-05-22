<?php
class RevistaCientifica extends MaterialDidatico
{
    public function __construct(
        string $titulo,
        int $anoPublicacao,
        EstadoConservacao $estadoConcervacao,
        public readonly int $qtdArtigos
    ) {
        parent::__construct($titulo, $anoPublicacao, $estadoConcervacao);
    }

    public function calcularDiasEmprestimo(): float
    {
        return $this->qtdArtigos * 2;
    }
}
