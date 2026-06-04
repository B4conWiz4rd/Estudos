<?php
    class Computador {
        public function __construct(
            public readonly Situacao $situacao,
            public readonly Marca $marca,
            public readonly string $descricao
        )
        {}
}