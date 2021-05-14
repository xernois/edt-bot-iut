const { Discord } = require("discord.js");
const message = require("../events/message");

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

function createRole(message, args) {
  let rolesName = [];

  message.guild.roles.cache.each((role) => rolesName.push(role.name));
  if (!rolesName.includes(args[0])) {
    message.guild.roles
      .create({
        data: { name: `${args[0]}`, color: `grey` },
        reason: "creation du rôle",
      })
      .then(console.log())
      .catch(console.error);
  }
}

function createChannel(message, args) {
  let channelsName = [];
  message.guild.channels.cache.each((channel) =>
    channelsName.push(channel.name)
  );

  if (!channelsName.includes(args[0])) {
    message.guild.channels.create(`${args[0]}`);
  }
}
