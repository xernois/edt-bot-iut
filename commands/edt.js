const Discord = require('discord.js');
const clientConfig = require('../utilities/config.json')


module.exports.run = async (client, message, args) => {
    console.log(message.channel.name);
    for (let chan in clientConfig){
        console.log(message.channel.name);
        let a = message.channel.name;
        try{
        if(clientConfig[chan] == a.toUpperCase()){
            console.log("Let's go!")
            message.channel.send(`C'est le channel ${message.channel.name}, il existe dans ${chan}`);
            return;
        }
        }
        catch(err){
            console.log(err);
        }
    }
    message.channel.send("Le site des edt : http://edt-iut-info.unilim.fr/edt/A1/");
}

module.exports.conf = {
    name : "edt",
    argsAllowed : 0
}