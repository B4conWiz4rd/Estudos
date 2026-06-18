<?php

$dbCaminho = '../serenatto.sqlite';

$pfo = new PDO("sqlite:$dbCaminho");
echo "Banco de dados criado e conectado com sucesso! \n";