<?php
    abstract class ItemCardapio {
        public function __construct(
            public readonly string $nomeProduto,
            TamanhoPorcao $tamanho
        )
        {
            abstract public function calcularPrecoFinal(): float;
        }
    }