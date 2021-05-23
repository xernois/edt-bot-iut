const fetch = require('node-fetch');

module.exports = function edtFetch (annee, groupe, semaine){
    fetch(`http://109.220.5.61/api/edt/a${annee}?s=${semaine}&g=${groupe}`)
        .then(response => response.json())
        .then(response => console.log(response.G1A.Lundi.forEach(element => console.log)))
        .catch(console.error)
}
