const Discord = require("discord.js");

module.exports.run = async (_client, message, _args) => {
  const clientConf = require("../utilities/flexConf.json");

  message.channel.send(
    "Le site des edt : http://edt-iut-info.unilim.fr/edt/A1/"
  );
};

module.exports.conf = {
  name: "site",
  argsAllowed: 0,
};