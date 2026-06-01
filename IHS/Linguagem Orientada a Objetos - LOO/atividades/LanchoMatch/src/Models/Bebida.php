<?php
    class Lanche extends ItemCardapio {
        public function __construct(
            string $nomeProduto,
            TamanhoPorcao $tamanho,
            public readonly int $mlVolume,
            )
        {
            return parent::__construct($nomeProduto, $tamanho);
        }

        public function calcularTaxa(): float {
            return $this -> mlVolume * 700;
        }

    }