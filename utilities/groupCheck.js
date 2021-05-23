
module.exports = function groupCheck(groupe, groups) {
    const a = groupe.substr(1);
    console.log(a);
    for (const i of groups){
        if (a == i) return i;
    }
    return false;
}