const Discord = require('discord.js');

module.exports.run = async (client, message, args) => {
	console.log(args.length);
	if(args.length > 1){
		console.log("Valeur inattendu suivante");
	}
    message.author.send("```Pour intéragir avec le bot, mentionnez-le puis faites la commande, ou utilisez le préfixe § \n" //On envoie un message contenant la liste des commandes à celui qui à fait la demande 
    + "Commandes : \n"
    + "help    :: Vous donne la page d'aide\n"
    + "edt     :: Donne le site des emplois du temps\n"
    + "next    :: /! WIP !\\ Vous donne votre prochain cours /! WIP !\\\n"
    + "current :: /! WIP !\\ Donne le lien de l'edt actuel   /! WIP !\\```");
}

module.exports.conf = {
    name : "help",
    argsAllowed : 0
}