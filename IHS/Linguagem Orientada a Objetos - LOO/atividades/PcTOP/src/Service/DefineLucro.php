<?php
    class DefineLucro {
        private float $lucroDefinido = 0.1;

        public function incluirNoCalculo( ): void {
            $this->lucroDefinido += $veiculo->calcularTaxa();
        }

        public function getTotal(): float {
            return $this->totalImpostos;
        }
    }