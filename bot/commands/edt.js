const Discord = require("discord.js");
const edtFetch = require("../utilities/edtFetch.js");
const derniereSemaine = require("../utilities/flexConf.json").derniereSemaine;

module.exports.run = async (_client, message, args) => {

    if(args.length){
        const groupe = args.shift();
        let semaine = derniereSemaine;

        if(args.length == 1){
          semaine = args.shift();
        }

        if(groupe.substr(1,1) == 1 || groupe.substr(1,1) == 2 || groupe.substr(1,1) == 3){
            annee(message, 1, groupe, semaine);
        }
        else if (groupe.substr(1,1) == 4 || groupe.substr(1,1) == 5){
            annee(message, 2, groupe, semaine);
        }
    }
    else{
        message.channel.send("Erreur : Il n'y a pas d'arguments");
    }
};

module.exports.conf = {
  name: "edt",
  argsAllowed: 2,
};

function groupCheck(groupe, groups) {
    const a = groupe.substr(1,1);
    for (const i of groups){
        if (a == i) return i;
    }
    return false;
}
  
async function annee(message, annee, groupe, semaine){
    edt = await edtFetch(annee, groupe, semaine)
        .then((response) => response.json())
        .then((response) => {return response});
    console.log(edt);
    try{
        if(edt.hasOwnProperty('code')){
            message.channel.send(`Èrreur ${edt.code} : ${edt.message}`)
            console.log(`Èrreur ${edt.code} : ${edt.message}`);
            return;
        }
        let cours = "";
        edt.Lundi.Cours.forEach(element => {cours += ' ' + element});
        message.channel.send(cours); //+ edt.Mardi.Cours + edt.Mercredi.Cours + edt.Jeudi.Cours + edt.Vendrerdi.Cours + edt.Samedi.Cours);
    }
    catch(err){
        console.error(err);
    }
}