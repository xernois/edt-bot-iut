module.exports.run = async (client, message, args) => {
	console.log(args.length);
	if(args.length > 1){
		console.log("Valeur inattendu suivante");
	}
	message.channel.send("```Etat du bot :\n"
	+"Est en fonctionnement depuis : " + Math.floor(client.uptime/1000/60/60) + "h" + Math.floor(client.uptime/1000/60%60) + "m" + Math.floor(client.uptime/1000%60%60) + "s" + "\n"
	+"Latence : " + client.ws.ping + "ms\n"
	+"Mémoire : " + Math.round(process.memoryUsage().heapUsed/1024/1024*100)/100 + "mb```");
};

module.exports.conf = {
	name: "status",
	argsAllowed : 0
};