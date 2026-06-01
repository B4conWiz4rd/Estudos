<?php
    class Lanche extends ItemCardapio {
        public function __construct(
            string $nomeProduto,
            TamanhoPorcao $tamanho,
            public readonly int $qtdCarnes,
            )
        {
            return parent::__construct($nomeProduto, $tamanho);
        }



    }