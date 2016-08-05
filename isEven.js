function isEven(value){
    if (value < 0){ value *= -1; }
    if(value == 0){
        return true;
    }else if(value == 1){
        return false;
    }else{
        value -= 2;
        return isEven(value);
    }
}
console.log(isEven(50));
console.log(isEven(75));
console.log(isEven(-1));