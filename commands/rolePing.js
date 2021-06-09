
const createRole = require("../utilities/createRole");
const Discord = require("discord.js");

module.exports.run = (client, message, args) => {
    message.channel.messages.fetch()
        .then(singleMessage => (singleMessage.forEach(element => {if(element.author.id == '611912631795712000' && element.embeds[0].title == "Recevoir le ping des edt ?"){
            message.channel.send(`Vous pouvez chercher le rôle ping ici : <#{${element.id}>`)
        } else {
            let response = new Discord.MessageEmbed()
            .setColor('#ffffff')
            .setTitle("Recevoir le ping des edt ?")
            
            
            createRole(message, ['rolePing']);
            message.channel.send(response)
            .then(sentResponse => {sentResponse.react("👍"); sentResponse.react("👎")})}})))
        .catch(console.error);
}

module.exports.conf = {
    name: "rolePing",
    permission: ["Administrator"],
    argsAllowed :  0,
}