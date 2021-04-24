const Discord = require("discord.js");

module.exports = (client, message, tagged) => {
  let command = message.content; //On attribue le contenu du message à la variable command
  if (!tagged) {
    //Si le bot n'est pas tag alors
    command = command.substr(1, command.length - 1); //on enlève le premier caractère car il s'agit du symbole d'appel
  }
  let args = command.split(" "); //On coupe la commande en plusieurs parties ce qui nous permettra de faire des commandes composées
  let firstCommand = args.shift(); //Alors on l'attribue à la seconde                                     //On attribue a une variable la commande principale
  if (tagged) {
    firstCommand = args.shift();
  }
  if (
    client.commands.has(firstCommand) &&
    client.commands.get(firstCommand).conf.argsAllowed === args.length
  ) {
    let cmd;
    cmd = client.commands.get(firstCommand);
    console.log(cmd.conf["permission"]);
    if (
      !cmd.conf.hasOwnProperty("permission") ||
      message.member.hasPermission(cmd.conf["permission"])
    ) {
      cmd.run(client, message, args);
    } else {
      message.channel.send(
        "Vous n'avez pas la permission requise pour effectuer cette modification"
      );
    }
  } else {
    //Sinon c'est une commande inconnue et on retourne l'erreur
    message.channel.send("Ceci n'est pas une commande valide");
  }
};
