const Discord = require("discord.js");
fs = require("fs");
const file = "./utilities/conf.json";

module.exports.run = async (client, message, args) => {
  let modify = JSON.parse(fs.readFileSync(file).toString());
  for (let firstArg in modify) {
    try {
      if (args[0] === firstArg) {
        console.log(`/!\\ ${firstArg} will get replaced by ${args[1]}`);
        console.log(modify);
        modify[firstArg] = args[1];
        fs.writeFileSync(file, JSON.stringify(modify));
        delete require.cache[require.resolve("../utilities/conf.json")];
        message.channel.send(
          `La caractéristique ${firstArg}, à été remplacé par ${args[1]}`
        );
        return;
      }
    } catch (err) {
      console.log(`Error : ${err}`);
    }
  }
  message.channel.send(
    `Nous n'avons pas pu trouver votre argument dans la configuration actuelle`
  );
};

module.exports.conf = {
  name: "set",
  argsAllowed: 2,
};
