<?php
    $registroPeso = $altv[1];
    $registroAltura = $altv[2];
    $valorImc = ($registroAltura*$registroAltura);
    $valorImc = $registroPeso/$valorImc;
    echo ("O valor do IMC é de $valorImc kg/m²");