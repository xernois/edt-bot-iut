const Discord = require("discord.js");

module.exports.run = async (client, message, args) => {
  const clientConf = require("../utilities/conf.json");

  for (let chan in clientConf) {
    let a = message.channel.name;
    try {
      if (clientConf[chan].toLowerCase() == a.toLowerCase()) {
        message.channel.send(
          `C'est le channel ${message.channel.name}, il existe dans ${chan}`
        );
        return;
      }
    } catch (err) {
      console.log(err);
    }
  }
  message.channel.send(
    "Le site des edt : http://edt-iut-info.unilim.fr/edt/A1/"
  );
};

module.exports.conf = {
  name: "edt",
  argsAllowed: 0,
};
