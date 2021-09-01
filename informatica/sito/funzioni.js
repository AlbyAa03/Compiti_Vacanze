function stampa404(nome) {
  document.getElementById("tabella").innerHTML = "";
  scritta = document.getElementById("404");
  scritta.innerHTML = "errore 404:\n" + "<br>" + nome + " inesistente";
}
function cancella404() {
  document.getElementById("404").innerHTML = "";
}

async function stampaJSON() {
  nome = document.getElementById("txtCitta").value;
  await fetch(
    new Request(
      "https://api.waqi.info/feed/" +
        nome +
        "/?token=a6856752cca047e8e149a704b4b4884d5ff5a181"
    )
  )
    .then((response) => response.json())
    .then((data) => {
      //console.log(data);
      if(data["status"] === 'error'){
        stampa404(nome)
        return;
      }
      cancella404()
      stampaCampi(data)

      
    });
}
var cntTr = -1;
var numTabella = -1;
function stampaCampi(data){
  document.getElementById("tabella").innerHTML = "";
  cntTr = -1
  numTabella = -1;

  let coordinate = document.getElementById("coordinates").checked,
  valoriOdierni = document.getElementById("valoriOggi").checked,
  settimanali = document.getElementById("valoriSettimana").checked,
  medi = document.getElementById("valoriMediSettimana").checked;

  nuovaTabella("tblNomeCitta","tbdyNomeCitta")
  aggiungiTrInTabella(nuovoTr("trCitta")) ;
  aggiungiTdInTabella(nuovoTdLato("tdCitta", data["data"]["city"]["name"],campoStyle = "column-span: all;color:red",clspan = 4),cntTr);
  
  if (coordinate) {
    nuovaTabella("tblCoordinate","tbdyCoordinate")
    aggiungiTrInTabella(nuovoTr       ("x"));
    aggiungiTdInTabella(nuovoTdLato   ("scrittaX","X",clspan = 2),cntTr)
    aggiungiTdInTabella(nuovoTdNormale("cit", data["data"]["city"]["geo"][0]),cntTr);

    aggiungiTrInTabella(nuovoTr       ("y")) ;
    aggiungiTdInTabella(nuovoTdLato   ("scrittaY","Y",clspan=2),cntTr)
    aggiungiTdInTabella(nuovoTdNormale("cit", data["data"]["city"]["geo"][1]),cntTr);
  }
  if (valoriOdierni) {
    nuovaTabella("tblValoriOdierni","tbdyValoriOdierni")
    aggiungiTrInTabella(nuovoTr       ("particelleValoriOdierni"));
    aggiungiTrInTabella(nuovoTr       ("valoriValoriOdierni"));
  
    for (chiave in data["data"]["iaqi"]){
      aggiungiTdInTabella(nuovoTdLato   ("particellaOdierna"+chiave,chiave),cntTr-1)
      aggiungiTdInTabella(nuovoTdNormale("valoreOdierna"+chiave, data["data"]["iaqi"][chiave]["v"]),cntTr);
    }
  }

  if (settimanali) {
    nuovaTabella("tblValoriSettimanali","tbdyVaoriSettimanali")
    aggiungiTrInTabella(nuovoTr       ("rigaGiorni"));
    aggiungiTdInTabella(nuovoTdInvisibile("vuotoGiorno","",),cntTr)

    for (chiave in data["data"]["forecast"]["daily"]["uvi"]){
      let temp = data["data"]["forecast"]["daily"]["uvi"][chiave]["day"]
      aggiungiTdInTabella(nuovoTdNormale("giorno"+temp,temp),cntTr)
    }

    for (chiave in data["data"]["forecast"]["daily"]){
      aggiungiTrInTabella(nuovoTr       ("rigaParticellaSettimanale"+chiave));
      aggiungiTdInTabella(nuovoTdLato   ("particellaSettimanale"+chiave,chiave),cntTr);
      for(giornaliero in data["data"]["forecast"]["daily"][chiave]){
        aggiungiTdInTabella(nuovoTdNormale(chiave+"valoreOdierna"+giornaliero, data["data"]["forecast"]["daily"][chiave][giornaliero]["min"] + ", " + data["data"]["forecast"]["daily"][chiave][giornaliero]["max"]),cntTr);
        console.log(giornaliero)
        console.log(data["data"]["forecast"]["daily"][chiave][giornaliero]["max"])
      }
    }
  }
  if(medi){
    nuovaTabella("tblValoriMediSettimanali","tbdyVaoriMediSettimanali")
    aggiungiTrInTabella(nuovoTr       ("rigaGiorniMedi"));
    aggiungiTrInTabella(nuovoTr       ("rigaValoriMediMassimi"));
    aggiungiTrInTabella(nuovoTr       ("rigaValoriMediMinimi"));
    aggiungiTdInTabella(nuovoTdLato("legendaParticellaMedia","PARTICELLA",),cntTr-2)
    aggiungiTdInTabella(nuovoTdLato("legendaValoreMedioMassimo","MASSIMI",),cntTr-1)
    aggiungiTdInTabella(nuovoTdLato("legendaValoreMedioMinimo","MINIMO",),cntTr)
    for (chiave in data["data"]["forecast"]["daily"]){
      let mediaMassima = 0,mediaMinima = 0,cnt = 0;
      for(giornaliero in data["data"]["forecast"]["daily"][chiave]){
          mediaMassima+=data["data"]["forecast"]["daily"][chiave][giornaliero]["max"]
          mediaMinima +=data["data"]["forecast"]["daily"][chiave][giornaliero]["min"]
          cnt+=1
      }
      
      aggiungiTdInTabella(nuovoTdNormale("Particella"+chiave+"Media",chiave),cntTr-2)
      aggiungiTdInTabella(nuovoTdNormale("valore"+chiave+"MediaMassima",(mediaMassima/cnt).toFixed(2)),cntTr-1)
      aggiungiTdInTabella(nuovoTdNormale("valore"+chiave+"MediaMinima",(mediaMinima/cnt).toFixed(2)),cntTr)
      
    }
  }
  document.getElementsByTagName("body")[0].style = "background-color: wheat; height: " +(Math.max(
    document.body.scrollHeight, document.documentElement.scrollHeight,
    document.body.offsetHeight, document.documentElement.offsetHeight,
    document.body.clientHeight, document.documentElement.clientHeight)+ 40) + "px";
 
  return;
}

function nuovoTdLato(id, testo,campoStyle = "",clspan = 1) {
  let td = document.createElement("td");
  td.colspan = clspan
  td.style =
    "width: 200px;text-align:center ;padding: 15px;background-color: rgba(255, 255, 255, 0.2);color: #fff;text-shadow: 1px 1px 1px #000;"+  campoStyle;
  td.id = id;
  td.innerHTML = testo;
  return td;
}
function nuovoTdNormale(id, testo, campoStyle ="",clspan = 1) {
  let td = document.createElement("td");
  td.id = id;
  td.colspan = clspan;
  td.innerHTML = testo;
  td.style = "border: 1px solid orange;background-color: #e6dc55;text-align:center;" + campoStyle;
  return td;
}
function nuovoTdInvisibile(id, testo = "", campoStyle ="",clspan = 1) {
  let td = document.createElement("td");
  td.id = id;
  td.colspan = clspan;
  td.innerHTML = testo;
  td.style = "border-collapse: collapse;overflow: hidden;box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);";
  return td;
}
function nuovoTr(id,incremento = 1) {
  let tr = document.createElement("tr");
  tr.id = id;
  cntTr +=incremento
  return tr;
}
function aggiungiTrInTabella(tr){
  document.getElementsByTagName("tbody")[numTabella].appendChild(tr);
}
function aggiungiTdInTabella(td,num){
  document.getElementsByTagName("tr")[num].appendChild(td);
}
function rigaVuota(incremento = 1){
  cntTr+=incremento;
  let tr = document.createElement("tr");
  tr.style = "background-color: #e6dc55;text-align:center;height: 48px"
  tr.innerHTML = " "
  document.getElementsByTagName("tbody")[numTabella].appendChild(tr);
}

function nuovaTabella(idTbl,idTbdy){
  let body   = document.getElementById("tabella");
  let tbl    = document.createElement("table");
  let tbdy   = document.createElement("tbody");
  body.innerHTML+="<br>"
  body.style =
    "margin-top:500px;padding-top: 200px;position: absolute;top:0%;left: 50%;-webkit-transform: translate(-50%, -50%);transform: translate(-50%, 0%);";
  tbl.style  =
    "width: 800px;border-collapse: collapse;overflow: hidden;box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);";
  tbdy.id    = idTbdy;
  tbl.id     = idTbl;
  tbl.appendChild(tbdy);
  body.appendChild(tbl);
  numTabella+=1;
  return;
}