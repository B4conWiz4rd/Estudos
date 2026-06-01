<?php
class Livro extends MaterialDidatico
{
    public function __construct(
        string $titulo,
        int $anoPublicacao,
        EstadoConservacao $estadoConcervacao,
        public readonly int $qtdPaginas
    ) {
        parent::__construct($titulo, $anoPublicacao, $estadoConcervacao);
    }

    public function calcularDiasEmprestimo(): float
    {
        return $this->qtdPaginas / 50;
    }
}
