<?php
class CalculadoraDeMaratonas
{

    private int $duracaoDaMaratona;

    public function incluir(Titulo $titulo): void {
        $this->duracaoDaMaratona += $titulo->duracaoEmMinutos();
    }

    public function getDuracao(){
        return $this->duracaoDaMaratona;
    }
}
