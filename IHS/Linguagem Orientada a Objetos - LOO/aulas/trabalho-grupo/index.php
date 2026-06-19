<?php
    $computadoFunc = [
        [
            'nome' => "Daten 01",
            'descricao' => "Computador Daten funcionando.",
            'foto' => "/assets/img/daten/funcionando/daten01-func.jpeg",
        ],
        [
            'nome' => "Daten 02",
            'descricao' => "Computador Daten funcionando.",
            'foto' => "/assets/img/daten/funcionando/daten02-func.jpeg",
        ],
        [
            'nome' => "Daten 03",
            'descricao' => "Computador Daten funcionando.",
            'foto' => "/assets/img/daten/funcionando/daten03-func.jpeg",
        ],
        [
            'nome' => "Daten 04",
            'descricao' => "Computador Daten funcionando.",
            'foto' => "/assets/img/daten/funcionando/daten04-func.jpeg",
        ],
        [
            'nome' => "Positivo 01",
            'descricao' => "Computador Positivo funcionando.",
            'foto' => "/assets/img/positivo/funcionando/posi01-func.jpeg",
        ],
    ];
    $computadoNaoFunc = [
        
        [
            'nome' => "Daten 01",
            'descricao' => "Computador Daten não está funcionando.",
            'foto' => "/assets/img/daten/nao-funcionando/daten01-nfunc.jpeg",
        ],
        [
            'nome' => "Daten 02",
            'descricao' => "Computador Daten não está funcionando.",
            'foto' => "/assets/img/daten/nao-funcionando/daten02-nfunc.jpeg",
        ],
        [
            'nome' => "Daten 03",
            'descricao' => "Computador Daten não está funcionando.",
            'foto' => "/assets/img/daten/nao-funcionando/daten03-nfunc.jpeg",
        ],
        [
            'nome' => "Daten 04",
            'descricao' => "Computador Daten não está funcionando.",
            'foto' => "/assets/img/daten/nao-funcionando/daten04-nfunc.jpeg",
        ],
        [
            'nome' => "Postivo 01",
            'descricao' => "Computador Positivo não está funcionando.",
            'foto' => "/assets/img/positivo/nao-funcionando/posi01-nfunc.jpeg",
        ],
        [
            'nome' => "Postivo 02",
            'descricao' => "Computador Positivo não está funcionando.",
            'foto' => "/assets/img/positivo/nao-funcionando/posi02-nfunc.jpeg",
        ],
        [
            'nome' => "Postivo 03",
            'descricao' => "Computador Positivo não está funcionando.",
            'foto' => "/assets/img/positivo/nao-funcionando/posi03-nfunc.jpeg",
        ],
        [
            'nome' => "Postivo 04",
            'descricao' => "Computador Positivo não está funcionando.",
            'foto' => "/assets/img/positivo/nao-funcionando/posi04-nfunc.jpeg",
        ],
        [
            'nome' => "Postivo 05",
            'descricao' => "Computador Positivo não está funcionando.",
            'foto' => "/assets/img/positivo/nao-funcionando/posi05-nfunc.jpeg",
        ],
    ]
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!--Estilização-->
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/main.css">
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
    <!--Lib-->
    <script type="module" src="assets/JS/lib.js"></script>
</head>

<body>

    <header data-bs-theme="dark">
        <div class="collapse text-bg-dark" id="navbarHeader">
            <div class="container">
                <div class="row">
                    <div class="col-sm-4 offset-md-1 py-4">
                        <h4>Acessos</h4>
                        <ul class="list-unstyled">
                            <li><a href="admin.html" class="text-white">Admin</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <img src="assets/img/pc.jpg" alt="icone de um computador" width="60">
                    <strong>Pc bolado REVENDAS</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>

    </header>

    <main>
        <section class="py-5 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <h1 class="fw-bold">Pc bolado REVENDAS</h1>
                    <p class="">
                        Consiga peças para o seu computador com os preços a baixo do mercado! Todas as peças foram
                        recondicionadas com o nosso selo de garantia! Aqui você tambêm pode encontrar peças não
                        funcionando para retirada de peças para reparo! Não vendemos lixo, nós fazemos reposição.
                    </p>
                    <p>
                        <a href="#pcFunciona" class="btn btn-primary my-2">Produtos Funcionando</a>
                        <a href="#pcNFunciona" class="btn btn-secondary my-2">Produtos não Funcionando</a>
                    </p>
                </div>
            </div>
        </section>
        <section>
            <div>

                <hr>
                <div class="album py-5" id="pcFunciona">
                    <h2>Computadores Funcionando</h2>
                    <div class="container">
                        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
                            <?php foreach ($computadoFunc as $pcFun): ?>
                                <amostra-prod
                                    img='<?php echo $pcFun['foto'] ?>'>
                                    <b><?php echo $pcFun['nome'] ?></b><br>
                                    <?php echo $pcFun['descricao'] ?>
                                </amostra-prod>
                            <?php endforeach; ?>
                        </div>
                    </div>
                </div>
                <hr>
                <div class="album py-5" id="pcNFunciona">
                    <h2>Computadores não Funcionando</h2>
                    <div class="container">
                        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
                            <?php foreach ($computadoNaoFunc as $pcNF): ?>
                                <amostra-prod
                                    img='<?php echo $pcNF['foto'] ?>'>
                                    <b><?php echo $pcNF['nome'] ?></b><br>
                                    <?php echo $pcNF['descricao'] ?>
                                </amostra-prod>
                            <?php endforeach; ?>
                        </div>
                    </div>
                </div>
                <hr>
            </div>
        </section>
    </main>


</body>

</html>