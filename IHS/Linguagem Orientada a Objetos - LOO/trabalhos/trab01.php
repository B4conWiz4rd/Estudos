<?php
    $usrNome = 'Prentys Assis';
    $valorSaldo = 1000;

    echo ("====== Banco Master Sistems ======\n");
    echo ("Olá $usrNome\n");
    echo ("Saldo: $valorSaldo\n");
    echo ("==================================\n");
    echo ("1 - Exbir Saldo Atual\n");
    echo ("2 - Sacar Saldo\n");
    echo ("3 - Depositar\n");
    echo ("4 - Sair\n");
    echo ("==================================\n");

    $opcao = (float)fgets(STDIN);

    switch ($opcao) {
        case 1:
            echo ("Saldo atual: $valorSaldo\n");

        case 2:
            $valorSaque;
            echo ("Digite o valor do saque\n");
            $valorSaque = (float)fgets(STDIN);
            if ($valorSaque>$valorSaldo){
                echo ("ERRO! Valor de saque a cima do Saldo.\n");
            }
            else {
                $valorSaque -= $valorSaldo;
                echo ("Saque efetuado com sucesso!\n");
                echo ("Valor atual: $valorSaldo\n");
            }

        case 3:
            $valorDeposito;
            echo ("Digite o valor de Depósito.\n");
            $valorDeposito = (float)fgets(STDIN);
            if ($valorDeposito < 0) {
                echo ("Erro! Valor digitado é negativo.\n");
            }
            else {
                $valorSaldo += $valorDeposito;
                echo ("O Valor foi depositado com sucesso!\n");
                echo ("Valor atual: $valorSaldo\n");
            }

        case 4:
            echo ("Adeus!\n");

        default:
            echo ("Opção inválida\n");
}