Array.prototype.last = function() {
    
    const arrLen = this.length

    if (arrLen) {
        return this[arrLen - 1]
    } 
    
    return -1
};