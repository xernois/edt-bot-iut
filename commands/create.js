const { Discord } = require("discord.js");
const createChannel = require("../utilities/createChannel");
const createRole = require("../utilities/createRole");

module.exports.run = async (_client, message, args) => {
  // Si un utilisateur ajoute sa réaction sur la réaction du bot alors lui rajouter lez rôle : info-edt
  //   if(message.guild.roles.has('');
  type = args.shift();
  type === "role"
    ? createRole(message, args)
    : type === "channel"
    ? createChannel(message, args)
    : message.channel.send("Demande de création inconnue");
};

module.exports.conf = {
  name: "create",
  argsAllowed: 2,
  permission: ["ADMINISTRATOR"],
};
