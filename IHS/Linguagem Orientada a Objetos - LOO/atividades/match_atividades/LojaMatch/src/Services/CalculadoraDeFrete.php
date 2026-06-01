<?php
    class CalculadoraDeFrete {
        private float $frete=0;
    
        public function calcularFrete(Produto $produto): void {
            $this->frete += $produto->calcularTaxaEnvio();
        }
        
        public function getTotal(): float {
            return $this->frete;
        }
    }