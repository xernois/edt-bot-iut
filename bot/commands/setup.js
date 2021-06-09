module.exports.run = (client, message, _args) => {
  let cmd = client.commands.get("create");
  cmd.run(client, message, ["role", "pingEdt"]);
  cmd.run(client, message, ["channel", "role"]);

  //   let newChannel;
  //   message.guild.channels.cache.each(Element => {if(Element.name == "role"){newChannel = Element.id}});
};

module.exports.conf = {
  name: "setup",
  argsAllowed: 0,
  permission: ["ADMINISTRATOR"],
};
