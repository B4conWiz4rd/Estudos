<?php
    $registroAno = $argv[1];

    if ($registroAno %2 == 0) {
        echo "O ano de $registroAno é bissexto!";
    } else {
        echo "O ano de $registroAno não é bissexto!";
    };
