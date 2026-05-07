


//    <div class="produto">
//                 <img src="https://images.tcdn.com.br/img/img_prod/1106817/pirulito_coresmel_twister_lollipop_600g_com_25_unidades_20845_1_57fb8db3209215351a86b8f32243dfcd.jpg" alt="">
//                 <h2>PIRULITO TWISTER</h2>
//                 <p>R$ 20,00</p>
//                 <button type="button">COMPRAR</button>
//             </div>
function aula() {
    // variavel<- vetor de [1..3] de caractere
    var filmes = [
        "interestelar",
        "Meninas Malvadas",
        "Diabo veste prada 2"
    ];
    console.log(filmes);
    console.log(filmes[1])
    console.log("Um filme que está estourando é", filmes[0])
    //push adiciona no ultimo
    filmes.push("As branquelas");
    console.log(filmes)
    //shift adiciona no primeiro
    filmes.unshift("Homem aranha")
    console.log(filmes)
    //pop deleta o ultimo
    filmes.pop();
    console.log(filmes)
    //shift deleta o primeiro
    filmes.shift();
    console.log(filmes)
    //splice(indice. quantos quer sobrescrever, dados)
    filmes.splice(1, 1);
    console.log(filmes)

    filmes.splice(1, 0, "kill bill vol 1 e 2")
    console.log(filmes)
    var filmesCopia = filmes.slice();
    console.log(filmesCopia)

    for (var i = 0; i < filmes.length; i++) {
        console.log(filmes[i]);
    }
    filmes.map(cadaFilme => {
        console.log(cadaFilme);
    });

}
aula();
var doces = [
    ['PIRULITO', 'https://images.tcdn.com.br/img/img_prod/1106817/pirulito_coresmel_twister_lollipop_600g_com_25_unidades_20845_1_57fb8db3209215351a86b8f32243dfcd.jpg', 20],

    ['Sonho de valsa', 'https://cdn.awsli.com.br/600x450/298/298064/produto/13538380/0925688202.jpg', 5.99],

    ['LOLLO', 'https://http2.mlstatic.com/D_NQ_NP_726554-MLB42006493276_052020-O.webp', 3],


];
doces.map(cadaDoce=> {
    document.getElementById("produtos").innerHTML += `

<div class="produto">
                 <img src="${cadaDoce[1]}" alt="PIRULITO">
                <h2>${cadaDoce[0]}</h2>
               <p>R$${cadaDoce[2]}</p>
               <button type="button">COMPRAR</button>
            </div>
            `
});


