<?php
    class VerificadorDeEmprestimos {
        private int $totalDias = 0;

        public function tempoEmprestimo(MaterialDidatico $material): void {
            $this -> totalDias += $material->calcularDiasEmprestimo();
        }
        
        public function getTotal(): float {
            return $this->totalDias;
        }
    }