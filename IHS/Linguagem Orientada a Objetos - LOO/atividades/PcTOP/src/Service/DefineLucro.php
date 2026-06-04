<?php
    class DefineLucro {
        private float $lucroDefinido = 0.1;

        public function valorFinal(DefineComponente $componente ): void {
            $this->lucroDefinido += $componente->calcularValor();
        }

        public function getTotal(): float {
            return $this->lucroDefinido;
        }
    }