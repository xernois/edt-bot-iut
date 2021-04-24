const Discord = require("discord.js");
const clientMention = "<@!611912631795712000>";
const isAsked = require("../utilities/isAsked.js");
const commandProcess = require("../utilities/commandProcess.js");
const fs = require("fs");

module.exports = (client, message) => {
  if (message.author == client.user || !message.channel.name) {
    return; //il l'ignore
  }

  let prefix = require("../utilities/conf.json").prefix;

  console.log(`Prefix : ${prefix}`);

  tagged = isAsked(clientMention, message); //On met dans une variable, un booléen qui est le retour d'une fonction qui permet de voir si le bot est mentionné
  if (message.content.startsWith(`${prefix}`) || tagged) {
    //Si il est mentionné ou que la première lettre du message est § alors
    commandProcess(client, message, tagged); //On rentre de la fonction commandProcess
  }
};
