<?php
require __DIR__ . "/src/model/genero.php";
require __DIR__ . "/src/model/Filme.php";

$fime1 = new filme(
    "Thor: Ragnarock",
    2020,
    Genero::SuperHeroi,
);

$filme2 = new filme(
    "Top Gun Maverick",
    2020,
    Genero::Acao,
);

echo 'Sup fella!';

$filme1->avalia(6);
$filme2->avalia(8);
$filme1->avalia(4);
$filme2->avalia(10);
$filme1->avalia(7);
$filme2->avalia(7);

echo $filme1->media();