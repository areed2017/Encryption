
const min = 500
const max = 2000

class RSA{

    constructor(modulus=0, exponent=0){
        this.modulus = modulus
        this.exponent = exponent
    }

    generate_pq(){

        let value
        while( this.p == null || this.q == null ){
            value = Math.floor(min + Math.random() * (max - min))

            if ( isPrime(value) ){
                if(this.p == null)
                    this.p = value
                else if(this.q == null)
                    this.q = value
            }
        }

        return {p:this.p, q:this.q}
    }

    setModulus(modulus=null){
        this.modulus = modulus
        if(modulus == null)
            this.modulus = this.p * this.q

        return this.modulus
    }

    generatePublicExponent(){

        let phi = totient(this.p, this.q)

        let value = Math.floor(Math.random() * phi) + 1
        while( true ){
            if(value === 1)
                value = Math.floor(Math.random() * phi) + 2

            if( gcd(phi, value) === 1 ){
                this.public_exponent = value
                return this.public_exponent
            }
        }
    }

    generatePrivateExponent(public_exponent){
        if(public_exponent == null)
            return null

        let phi = totient(this.p, this.q)

        let d = 1.1
        let k = 1
        while( d !== Math.floor(d) ){
            k += Math.floor(Math.random() * 10) + 1
            d = (1 + k * phi) / public_exponent
        }

        this.private_exponent = d
        return this.private_exponent
    }

    setPublicExponent(public_exponent=null){
        if( public_exponent != null) {
            this.public_exponent = public_exponent
            return public_exponent
        }

        this.generatePublicExponent()
        return this.public_exponent
    }

    setPrivateExponent(private_exponent=null) {
        if (private_exponent != null) {
            this.private_exponent = private_exponent
            return private_exponent
        }

        this.generatePrivateExponent(this.public_exponent)
        return this.private_exponent
    }

    getPhi() {
        if( this.phi == null )
            this.phi = totient(this.p, this.q)

        return this.phi
    }

    encrypt(value) {
        let encrypted = ""
        if( isAlpha(value) || typeof value === typeof ""){
            let temp

            while(value.length % 3 !== 0)
                value += "{"

            for( let i = 0; i < value.length; i+=3){
                let temp2 = ""
                temp =  charCode(value.charAt(i)) + "" +
                        charCode(value.charAt(i + 1))+ "" +
                        charCode(value.charAt(i + 2))

                while(temp.length < 2)
                    temp = "0" + temp

                temp2 += temp
                encrypted += this.exec(temp2) + "="
            }
            return encrypted
        }

        return this.exec(value)
    }

    decrypt(value){
        if(value.includes("=")){
            value = value.split("=")
            let decrypted = ""
            for(  let v of value ){
                if( v === "" )
                    continue
                let d = this.exec(v).toString()

                for( let i = 0; i < 3; i++){
                    let s = d.substr(i * 2, (i * 2) + 2).substr(0,2)
                    decrypted += charCodeValue(parseInt( s ))
                }
                while(decrypted.substr(decrypted.length-1,decrypted.length) === "{")
                    decrypted = decrypted.substring(0, decrypted.length-1)
            }
            return decrypted
        }

        return this.exec(value)
    }

    exec( value ) {
        return modular_pow(value, this.exponent, this.modulus)
    }

}

function charCode(str){
    let value = str.charCodeAt(0) - 65
    if(value < 0){
        value = Math.abs(value) + 60
    }
    return value
}

function charCodeValue(charCode){
    if(charCode > 60){
        charCode = 0 - (charCode - 60)
    }
    return String.fromCharCode(charCode + 65)
}


function totient(p, q){
    return ( p - 1 ) * ( q - 1 )
}

function gcd(a,b) {
    a = Math.abs(a);
    b = Math.abs(b);
    if (b > a) {let temp = a; a = b; b = temp;}
    while (true) {
        if (b === 0) return a;
        a %= b;
        if (a === 0) return b;
        b %= a;
    }
}

function isPrime(number){
    let start = 2;
    while (start <= Math.sqrt(number)) {
        if (number % start++ < 1)
            return false;
    }
    return number > 1;
}

function modular_pow(base, exponent, modulus) {
    if ( modulus === 1 )
        return 0

    let result = 1
    base = base % modulus

    while( exponent > 0){
        if( exponent % 2 === 1){
            result = ( result * base ) % modulus
        }

        exponent = exponent >> 1
        base = ( base * base ) % modulus
    }

    return result
}


function isAlpha(str) {
    let code, i, len

    for (i = 0, len = str.length; i < len; i++) {
        code = str.charCodeAt(i);
        if (!(code > 64 && code < 91) && // upper alpha (A-Z)
            !(code > 96 && code < 123)) { // lower alpha (a-z)
            return false
        }
    }

    return true;
}
