const findChannel = require("../utilities/includeChannel");
module.exports =
function createChannel(message, args) {
    channel = args;
    console.log(channel);
  
    if (!findChannel(message, channel)) {
      message.guild.channels.create(`${channel}`);
    }
}