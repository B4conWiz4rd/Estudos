<?php
class Geladeira extends Produto{
    public function __construct(
        string $nome,
        float $precoBase,
        CatergoriaEletronico $catergoriaEletronico,
        public readonly int $qtdMesesGarantia
    ) {
        parent::__construct($nome, $precoBase, $catergoriaEletronico,);
    }

    public function calcularTaxaEnvio(): float
    {
        return $this->qtdMesesGarantia * 50.00;
    }
}
