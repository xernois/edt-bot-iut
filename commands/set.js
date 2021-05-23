const { Role } = require("discord.js");
const includeChannel = require("../utilities/includeChannel");

fs = require("fs");
const file = "./utilities/conf.json";

module.exports.run = async (_client, message, args) => {
  const setter = args.shift();
  switch (setter) {
    case "prefix":
      prefix(message, args);
      break;
    case "channel":
      chan(message, args);
      break;
    case "role":
      role(message, args);
    default:
      break;
  }
};

function prefix(message, args) {
  let modify = JSON.parse(
    fs.readFileSync(`./utilities/flexConfig.json`).toString()
  );
  for (let firstArg in modify) {
    try {
      if (args[0] === firstArg) {
        modify[firstArg] = args[1];
        fs.writeFileSync(file, JSON.stringify(modify));
        delete require.cache[require.resolve("../utilities/flexConf.json")];
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
}

/*  A finir

function chan(message, args) {
  channel = args.shift();
  if(includeChannel(message, channel)){
    message.channel.send(`Le salon ${channel.id} existe`);
  }
  else{ 
    message.channel.send(`Le salon <#${channel}> n'existe pas`);
  }

  // set channel A1 permission ADMINISTRATOR
}*/

module.exports.conf = {
  name: "set",
  permission: ["ADMINISTRATOR"],
  argsAllowed: 5,
};
