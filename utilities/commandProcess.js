module.exports = (client, message, tagged) => {
  let command = message.content;
  if (!tagged) {
    command = command.substr(1, command.length - 1);
  }
  let args = command.split(" ");
  let firstCommand = args.shift();
  if (tagged) {
    firstCommand = args.shift();
  }
  if (
    client.commands.has(firstCommand) &&
    client.commands.get(firstCommand).conf.argsAllowed >= args.length
  ) {
    const cmd = client.commands.get(firstCommand);
    if (
      !cmd.conf.hasOwnProperty("permission") ||
      message.member.hasPermission(cmd.conf.permission)
    ) {
      cmd.run(client, message, args);
    } else {
      return message.channel.send(
        "Vous n'avez pas la permission requise pour effectuer cette modification"
      );
    }
  } else {
    return message.channel.send("Ceci n'est pas une commande valide");
  }
};