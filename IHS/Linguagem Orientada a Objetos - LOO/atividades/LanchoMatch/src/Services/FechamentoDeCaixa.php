<?php
    class FechamentoDeCaixa {
        private float $totalDaBandeja = 0;

        public function regitarItem(Item $itemCardapio):void {
            $this->totalDaBandeja += ItemCardapio -> calcularPrecoFinal();
        }

        public function getTotal():float{

        }
    }