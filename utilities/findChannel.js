module.exports = 

function findChannel(message, channel){
let channelsName = [];
message.guild.channels.cache.each((guildChannel) =>
  channelsName.push(guildChannel.name)
);

if (channelsName.includes(channel)){
    return channel
}
}