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
    

    console.log(`Jour : ${days[Math.floor(dow)]}`);

    if(args.length){
        const groupe = args.shift();
        let semaine = derniereSemaine;

        if(args.length == 1){
          semaine = args.shift();
        }

        hour >= 19 ? days = days[Math.floor(dow)] + 1 : days = days[Math.floor(dow)];
;
        if(groupe.substr(1,1) == 1 || groupe.substr(1,1) == 2 || groupe.substr(1,1) == 3){
            annee(message, 1, groupe, semaine, days[Math.floor(dow)], hour);
        }
        else if (groupe.substr(1,1) == 4 || groupe.substr(1,1) == 5){
            annee(message, 2, groupe, semaine, days[Math.floor(dow)], hour);
        }
    }
    else{
        message.channel.send("Erreur : Il n'y a pas d'arguments");
    }
    
    
    
    //!next G1A
    
};

async function hourFinder(hour, minutes){
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

function dayofweek(d, m, y)
{
    let t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ];
    y -= (m < 3) ? 1 : 0;
    return ( y + y/4 - y/100 + y/400 + t[m-1] + d) % 7;
}

function groupCheck(groupe, groups) {
    const a = groupe.substr(1,1);
    for (const i of groups){
        if (a == i) return i;
    }
    return false;
}
  
async function annee(message, annee, groupe, semaine, jour, hour){
    edt = await edtFetch(annee, groupe, semaine)
        .then((response) => response.json())
        .then((response) => {return response});
    try{
        if(edt.hasOwnProperty('code')){
            message.channel.send(`Èrreur ${edt.code} : ${edt.message}`)
            console.log(`Èrreur ${edt.code} : ${edt.message}`);
            return;
        }
        let cours = [];
        edt[jour].Cours.forEach(element => cours.push(element));
        message.channel.send(cours[hourFinder]);
    }
    catch(err){
        console.error(err);
    }
}
