<?php
    
    $notas =[];
    $quantidadeDeNotas = ($argc - 1) == 0 ? 1 : ($argc - 1); 
    
    for ($i = 1; $i < $argc; $i++){
        
        $notas[] = (float) $argv[$i];
    
        }
    
    echo $notas;