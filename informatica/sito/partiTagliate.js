/*
var arrivato = false;

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function richiestaAPI(nome) {
  let response,data
  await fetch("https://api.waqi.info/feed/" +
  nome +
  "/?token=a6856752cca047e8e149a704b4b4884d5ff5a181").then(response => response.json()).then(data => {console.log("arrivato")});
  return data
  let response = await fetch(
    "https://api.waqi.info/feed/" +
      nome +
      "/?token=a6856752cca047e8e149a704b4b4884d5ff5a181"
  ); //https://api.waqi.info/feed/Cuneo/?token=a6856752cca047e8e149a704b4b4884d5ff5a181
  let data = response.json();
  return data;
  //console.log(Object.keys(data))
  //console.log(data["data"]["forecast"])
}

async function faiRichiesta() {
  let data = richiestaAPI(document.getElementById("txtCitta").value);
  
  return data;
}
*/

/*
DA METTERE A POSTO
*/
/*
function creaTabella(nRighe, nColonne) {
  let body = document.getElementById("tabella");
  body.style =
    "margin-top:500px;padding-top: 200px;position: absolute;top:0%;left: 50%;-webkit-transform: translate(-50%, -50%);transform: translate(-50%, 0%);";
  let tbl = document.createElement("table");
  tbl.style =
    "width: 800px;border-collapse: collapse;overflow: hidden;box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);";

  let tbdy = document.createElement("tbody");
  tbdy.id = "tbdy";
  for (let i = 0; i < nRighe; i++) {
    let tr = document.createElement("tr");
    for (let j = 0; j < nColonne + 1; j++) {
      let td = document.createElement("td");
      if (j == 0) {
        td.innerHTML = 4;
        td.style =
          "width: 200px;text-align:center ;padding: 15px;background-color: rgba(255, 255, 255, 0.2);color: #fff;text-shadow: 1px 1px 1px #000;";
      } else {
        td.innerHTML = "";
        td.id = i + "_" + j;
        td.style = "border: 1px solid rgba(255, 255, 255, 0.2);background-color: #c56731";
        td.onclick = eventoBottone;
      }
      tr.appendChild(td);
    }
    tbdy.appendChild(tr);
  }

  tbl.appendChild(tbdy);
  body.appendChild(tbl);
}

function aggiungiRighe(nRighe, nColonne, ids) {
  tbdy = document.getElementById("tbdy");
  for (let i = 0; i < nRighe; i++) {
    let tr = document.createElement("tr");
    for (let j = 0; j < nColonne + 1; j++) {
      let td = document.createElement("td");
      if (j == 0) {
        td.innerHTML = 4;
        td.style =
          "width: 200px;text-align:center ;padding: 15px;background-color: rgba(255, 255, 255, 0.2);color: #fff;text-shadow: 1px 1px 1px #000;";
      } else {
        td.innerHTML = "";
        td.id = i + ids + j;
        td.style = "border: 1px solid orange;background-color: #e6dc55;";
        td.onclick = eventoBottone;
      }
      tr.appendChild(td);
    }
    tbdy.appendChild(tr);
  }

  tb = document.getElementById("tabella").style;
}
*/