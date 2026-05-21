<?php
    class Smartphone extends produto {
        public function __construct(
        string $nome,    
        float $precoBase,
        CatergoriaEletronico $catergoriaEletronico,
        public readonly int $qtdAcessorios,){
            parent::__construct($nome, $precoBase, $catergoriaEletronico);
        }

        #[Override]
        public function calcularTaxaEnvio():float {
            return $this -> qtdAcessorios * 15.00;
        }
    }