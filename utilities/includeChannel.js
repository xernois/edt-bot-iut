module.exports = 
function includeChannel(message, channel){
    let channelsId = [];
    message.guild.channels.cache.each((guildChannel) =>
      channelsId.push(guildChannel.name)
    );

    if (channelsId.includes(channel)) {
        return true;
    }
    else{
        return false;
    }
}
