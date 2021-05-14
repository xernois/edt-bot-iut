const clientMention = "<@!611912631795712000>";
const isAsked = require("../utilities/isAsked.js");
const commandProcess = require("../utilities/commandProcess.js");

module.exports = (client, message) => {
  if (message.author == client.user || !message.channel.name) {
    return;
  }

  const prefix = require("../utilities/flexConf.json").prefix;
  const tagged = isAsked(clientMention, message);

  if (
    (message.content.startsWith(`${prefix}`) || tagged) &&
    message.content.length > 2
  ) {
    commandProcess(client, message, tagged);
  }
};
