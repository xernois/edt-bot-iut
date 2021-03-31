// Un tag ou mention est le fait de mentionner quelqu'un dans un message grâce au préfixe @, qui est en réalité un raccourci pour <@!idDeLaPersonne>
// Un token est un numéro d'identification unique permettant la prise de contrôle d'un compte
// client désigne le bot discord


const Discord = require('discord.js');                                             //Appelle du module pour faire le bot discord
const client = new Discord.Client();                                               //Création du bot
const token = "NjExOTEyNjMxNzk1NzEyMDAw.XVauDA.GBKqcqOPSN6RBcc9PYZOeDADorc";       //Token du bot
const clientMention = "<@!611912631795712000>";                                    //Mention du bot <@!idDeLaPersonneMentionnée>

client.on('ready', () => {                                //Quand le bot est connecté à discord
    console.log("Connecté en tant que : " + client.user.tag)        //On affiche dans la console qu'il est connecté en tant que + son nom
});


client.on('message', (messageListened)=>{                                       //Quand le bot voit qu'il y a un message, appelle une fonction avec pour paramètre le message
if(messageListened.author == client.user){                                      //Si le bot est le propre auteur du message
        return;                                                                 //il l'ignore
    }

    tagged = isAsked(clientMention, messageListened);                           //On met dans une variable, un booléen qui est le retour d'une fonction qui permet de voir si le bot est mentionné
    if (messageListened.content.startsWith("§") || tagged){                     //Si il est mentionné ou que la première lettre du message est § alors
        commandProcess(messageListened, tagged);                                //On rentre de la fonction commandProcess
    }
});

function commandProcess(messageListened, tagged){                               //Fonction : commandProcess; Entrée : un message, et si le bot a été tag
    let command = messageListened.content;                                      //On attribue le contenu du message à la variable command
    if(!tagged){                                                                //Si le bot n'est pas tag alors 
        command = command.substr(1);                                            //on enlève le premier caractère car il s'agit du symbole d'appel
    }
    let splittedCommand = command.split(" ");                                   //On coupe la commande en plusieurs parties ce qui nous permettra de faire des commandes composées
    let firstCommand = splittedCommand[0];                                      //On attribue a une variable la commande principale
    if(tagged){                                                                 //Mais si l'utilisateur a été tag
        firstCommand = splittedCommand[1];                                      //Alors on l'attribue à la seconde
    }

    if(firstCommand === "help"){                                                //Si la première commande est help
        messageListened.author.send("```Pour intéragir avec le bot, mentionnez-le puis faites la commande, ou utilisez le préfixe § \n" //On envoie un message contenant la liste des commandes à celui qui à fait la demande 
        + "Commandes : \n"
        + "help    :: Vous donne la page d'aide\n"
        + "edt     :: Donne le site des emplois du temps\n"
        + "next    :: /! WIP !\\ Vous donne votre prochain cours /! WIP !\\\n"
        + "current :: /! WIP !\\ Donne le lien de l'edt actuel   /! WIP !\\```");
    }
    else if(firstCommand === "edt"){                                             //Sinon si la première commande est edt, alors on envoie dans le salon, le site des emplois du temps
        messageListened.channel.send("Le site des edt : http://edt-iut-info.unilim.fr/edt/A1/");
    }
    else if(firstCommand === "status"){                                          //Sinon si la première commande est status, alors on affiche l'état du bot pour savoir son état et si on a besoin de le redémarrer
        messageListened.channel.send("```Etat du bot :\n"
        +"Est en fonctionnement depuis : " + Math.floor(client.uptime/1000/60/60) + "h" + Math.floor(client.uptime/1000/60%60) + "m" + Math.floor(client.uptime/1000%60%60) + "s" + "\n"
        +"Latence : " + client.ws.ping + "ms\n"
        +"Mémoire : " + Math.round(process.memoryUsage().heapUsed/1024/1024*100)/100 + "mb```");
    }
    else{                                                                       //Sinon c'est une commande inconnue et on retourne l'erreur
        messageListened.channel.send("Ceci n'est pas une commande valide");
    }
}

function isAsked(Person, messageListened){                      //Si les premiers caractères du message sont absolument identiques aux caractères correspondant au fait de tag un bot, retourne vrai
    for(i=0; i < Person.length;i++){
        if(messageListened.content[i] != Person[i]){
            return false;                                       //Sinon retourne faux
        }
    }
    return true;                                                                 
}

client.login(token) ;                                           //On se connecte avec le bot grâce au token pouvant permettre le contrôle