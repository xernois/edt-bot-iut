const edtFetch = require("../utilities/edtFetch");
const derniereSemaine = require("../utilities/flexConf.json").derniereSemaine;

module.exports.run = async(_client, message, args) => {
    let days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"];
    let date = new Date();

    let day = date.getDate();
    let month = date.getMonth() + 1;
    let year = date.getFullYear();

    let dow = dayofweek(day, month, year) - 1;
    
    let hour = date.getHours();
    let minutes = date.getMinutes();
    
    if(args.length){
        const groupe = args.shift();
        let semaine = derniereSemaine;

        if(args.length == 1){
          semaine = args.shift();
        }

        hour >= 19 ? days = days[Math.floor(dow) + 1] : days = days[Math.floor(dow)];
;
        if(groupe.substr(1,1) == 1 || groupe.substr(1,1) == 2 || groupe.substr(1,1) == 3){
            annee(message, 1, groupe, semaine, days, hour, minutes);
        }
        else if (groupe.substr(1,1) == 4 || groupe.substr(1,1) == 5){
            annee(message, 2, groupe, semaine, days, hour, minutes);
        }
    }
    else{
        message.channel.send("Erreur : Il n'y a pas d'arguments");
    }
        
};

function hourFinder(hour, minutes){
    let next_hour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    num = (hour - 8)*2;
    if(minutes >= 30){
        num += 1;
    }
    if(hour < 8 || hour >= 19){
        num = 0;
    }
    return(next_hour[num])
}

module.exports.conf = {
    name: "next",
    argsAllowed: 1,
};


/////////////////////* Méthode de Sakamoto  : https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Implementation-dependent_methods_of_Sakamoto.2C_Lachman.2C_Keith_and_Craver*/////////////////
function dayofweek(d, m, y)
{
    let t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ];
    y -= (m < 3) ? 1 : 0;
    return ( y + d + y/4 - y/100 + y/400  + t[m-1]) % 7 ;
}
/////////////////////////////////////////////////////////////////////////////

function groupCheck(groupe, groups) {
    const a = groupe.substr(1,1);
    for (const i of groups){
        if (a == i) return i;
    }
    return false;
}

async function annee(message, annee, groupe, semaine, jour, hour, minutes){
    let prochaineHeure = ["8h00", "8h30", "9h00", "9h30", "10h00", "10h30", "11h00", "11h30", "12h00", "12h30", "13h00", "13h30", "14h00", "14h30", "15h00", "15h30", "16h00", "16h30", "17h00", "17h30", "18h00", "18h30", "19sh00"]
    edt = await edtFetch(annee, groupe, semaine)
        .then((response) => response.json())
        .then((response) => {return response});
    try{
        if(edt.hasOwnProperty('code')){
            message.channel.send(`Èrreur ${edt.code} : ${edt.message}`)
            console.log(`Erreur ${edt.code} : ${edt.message}`);
            return;
        }
        let cours = [];

        edt[jour].Cours.forEach(element => cours.push(element));

        message.channel.send(`Prochain cours : ${cours[hourFinder(hour, minutes)]} à ${prochaineHeure[hourFinder(hour, minutes)]}`);

    }
    catch(err){
        console.error(err);
    }
}
