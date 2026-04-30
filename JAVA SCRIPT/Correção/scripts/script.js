
function ex1(){
  var nPessoas = document. getElementById("nPessoas").value;
  var valor = document.querySelector("#valor").value;
  var valorDivido = valor / nPessoas;
  alert (` O valor total é R$ ${valorDivido}`)
 }
 document.querySelector("#btnEx2").addEventListener("click", ex2)

 function ex2(){
  alert(`O numero ${numero}, antexessor ${numero-1},sucessor ${numero+ 1}`);
 }

//função anonima
// document.addEventlistener("click",() =>)
    //{);
