module.exports = 
function createRole(message, args) {
  let rolesName = [];

  message.guild.roles.cache.each((role) => rolesName.push(role.name));

  let name = args.shift();
  if (!rolesName.includes(name)) {
    message.guild.roles
      .create({
        data: { name: `${name}`, color: `grey` },
        reason: "creation du rôle",
      })
      .then(console.log())
  }
}