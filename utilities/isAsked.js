module.exports = (mention, message) => {
    for(i=0; i < mention.length;i++){
        if(message.content[i] != mention[i]){
            return false;
        }
    }
    return true;
}