var nome = "NEYMAR";
var vida = 5;
var money = 0;
var dano = 1;

function mostrarPersonagem() {
    document.getElementById("ficha").innerHTML = `
        <img src="images/giphy.gif" id="icone" alt="icone">
        <h1>🌟 ${nome}</h1>
        <p>❤️ ${vida}</p>
        <p>💵 ${money}</p>
        <p>🔫 ${dano}</p>
    `;
}

// VIDA
document.getElementById("vida").addEventListener("click", function () {
    if (vida >= 20) {
        alert("⚠️ LIMITE DE VIDA MÁXIMA: 20");
        return;
    }
    vida++;
    mostrarPersonagem();
});

// MONEY
document.getElementById("money").addEventListener("click", function () {
    var personalizado = confirm("Deseja adicionar valor personalizado?");
    
    if (personalizado) {
        var valor = parseInt(prompt("Digite a quantidade de moedas:"));
        if (!isNaN(valor)) {
            money += valor;
        }
    } else {
        money++;
    }

    mostrarPersonagem();
});

// DANO
document.getElementById("dano").addEventListener("click", function () {
    var arma = prompt(`Qual arma o ${nome} está segurando?`).toUpperCase();

    switch (arma) {
        case "ESPADA":
            alert("Você selecionou a espada! ⚔️ (2 de dano)");
            dano = 2;
            break;

        case "ARCO":
            alert("Você selecionou o arco! 🏹 (3 de dano)");
            dano = 3;
            break;

        case "PISTOLA":
            alert("Você selecionou a pistola! 🔫 (4 de dano)");
            dano = 4;
            break;

        default:
            alert("❌ Arma não encontrada! Tente novamente.");
            return;
    }

    mostrarPersonagem();
});

// Inicial
mostrarPersonagem();