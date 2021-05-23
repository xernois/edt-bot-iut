const Discord = require("discord.js");
const derniereSemaine = require("../utilities/flexConf.json").derniereSemaine;
const edtFetch = require("../utilities/edtFetch.js");

module.exports.run = async (_client, message, args) => {
  const clientConf = require("../utilities/flexConf.json");
    if(args.length == 1){
        groupe = args.shift();
        groups = ['1', '2', '3','4','5'];
        if (`G${groupCheck(groupe, groups)}`){
            console.log(groupe.substr(1,1));
            if(groupe.substr(1,1) == 1 || groupe.substr(1,1) == 2 || groupe.substr(1,1) == 3){
                edtFetch(1, groupe, derniereSemaine);
            }
            else if (groupe.substr(1,1) == 4 || groupe.substr(1,1) == 5){
                edtFetch(2, groupe, derniereSemaine);
            }
        }
        else {
            message.channel.send("Groupe inexistant");
        }
    }
};

module.exports.conf = {
  name: "edt",
  argsAllowed: 1,
};

function groupCheck(groupe, groups) {
    const a = groupe.substr(1,1);
    for (const i of groups){
        if (a == i) return i;
    }
    return false;
}