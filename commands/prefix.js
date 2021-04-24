const Discord = require("discord.js");
const prefix = require("../utilities/conf.json").prefix;

module.exports.run = async (client, message, args) => {
  message.channel.send(`Le préfixe est : ${prefix}`);
};

module.exports.conf = {
  name: "prefix",
  argsAllowed: 0,
};
