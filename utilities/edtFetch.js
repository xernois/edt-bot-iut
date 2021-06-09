const fetch = require('node-fetch');

module.exports = function edtFetch (annee, groupe, semaine){
    return fetch(`http://109.220.5.61/api/edt/a${annee}?s=${semaine}&g=${groupe}`)
}
