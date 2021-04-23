// Un tag ou mention est le fait de mentionner quelqu'un dans un message grâce au préfixe @, qui est en réalité un raccourci pour <@!idDeLaPersonne>
// Un token est un numéro d'identification unique permettant la prise de contrôle d'un compte
// client désigne le bot discord


const Discord = require('discord.js');                                             //Appelle du module pour faire le bot discord
const fs = require('fs').promises;
const path = require('path');
const client = new Discord.Client();                                               //Création du bot
const token = "NjExOTEyNjMxNzk1NzEyMDAw.XVauDA.GBKqcqOPSN6RBcc9PYZOeDADorc";       //Token du bot                                 //Mention du bot <@!idDeLaPersonneMentionnée>
client.commands = new Discord.Collection();
client.event = new Discord.Collection(); 

client.login(token) ;  //On se connecte avec le bot grâce au token pouvant permettre le contrôle

async function eventLoader(dir= "./events"){
    const files = await fs.readdir(path.join(__dirname, dir));
    for(const file of files){
        const status = await fs.lstat(path.join(__dirname, dir, file));
        if(status.isDirectory()){
            await commandLoader(path.join(__dirname, dir));
        }
        else if (file.endsWith('.js')){
            const event = file.substring(0, file.indexOf('.js'));
            try{
                eventDir = require(path.join(__dirname, dir, file));
                client.on(event, eventDir.bind(null, client));
            }
            catch(err){
                throw new Error(`Error : ${err}`);
            }
        }
    }
}
eventLoader();

async function commandLoader(dir= "./commands"){
    const files = await fs.readdir(path.join(__dirname, dir));
    for(const file of files){
        const status = await fs.lstat(path.join(__dirname, dir, file));
        if(status.isDirectory()){
            await commandLoader(path.join(__dirname, dir));
        }
        else if (file.endsWith('.js')){
            try{
                const cmdMod = require(path.join(__dirname, dir, file));
                if(cmdMod.conf && cmdMod.conf.name){
                    console.log(`${cmdMod.conf.name} loaded successfully`);
                    client.commands.set(cmdMod.conf.name, cmdMod);
                }
            }
            catch(err){
                throw new Error(`Error : ${err}`);
            }
        }
    }
}
commandLoader();
