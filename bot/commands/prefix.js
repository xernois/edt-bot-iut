const prefix = require("../utilities/flexConf.json").prefix;

module.exports.run = async (_client, message, _args) => {
  message.channel.send(`Le préfixe est : ${prefix}`);
};

module.exports.conf = {
  name: "prefix",
  argsAllowed: 0,
};
