
const bytes_in_state = 16
const bytes_per_row = Math.sqrt(bytes_in_state)

class StateArray{

    constructor(sixteenByteString = "") {
        this.state_arr = []
        this.buffer = String.fromCharCode(bytes_in_state - sixteenByteString.length)

        for(let i =0; i < bytes_in_state; i++) {
            if (i < sixteenByteString.length)
                this.state_arr[i] = sixteenByteString.charAt(i)
            else
                this.state_arr[i] = this.buffer
        }
    }

    rot13() {
        for(let i =0; i < bytes_in_state; i++) {
            let char = this.state_arr[i].charCodeAt(0)
            this.state_arr[i] = String.fromCharCode(char + 13);
        }
    }


    reverse_rot13() {
        for(let i =0; i < bytes_in_state; i++) {
            let char = this.state_arr[i]
            this.state_arr[i] = String.fromCharCode(char - 13);
        }
    }


    row_shift() {

        let state_arr_cpy = this.state_arr.slice()


        for(let i = 1; i < bytes_per_row; i++){
            for(let j = 0; j < bytes_per_row; j++){
                let shift = Math.abs(j - i) % bytes_per_row
                if(j === i - 1)
                    shift = bytes_per_row - 1
                if(j === 0 && i === 3)
                    shift = 1

                this.state_arr[index(i,j)] = state_arr_cpy[index(i, shift)]
            }
        }
    }

    row_un_shift() {
        this.row_shift()
        this.row_shift()
        this.row_shift()
    }

    round_xor(round_keys) {

        for(let i = 0; i < bytes_per_row; i++){
            for(let j = 0; j < bytes_per_row; j++){
                let value = this.state_arr[index(i, j)]
                if(typeof value === 'string')
                    value = value.charCodeAt(0)
                this.state_arr[index(i,j)] = round_keys.apply(value, i)
            }
        }
    }

    getEncryptedString(){
        let encryptedStr = ""
        for(let i = 0; i < this.state_arr.length; i++){
            let value = this.state_arr[i]
            encryptedStr += String.fromCharCode(value & 255)
            encryptedStr += String.fromCharCode((value >> 8) & 255)
            encryptedStr += String.fromCharCode((value >> 16) & 255)
            encryptedStr += String.fromCharCode((value >> 24) & 255)
        }
        return btoa(encryptedStr)
    }

    getDecryptedString() {
        let decryptedStr = ""
        for (let i = 0; i < this.state_arr.length; i++)
            decryptedStr += this.state_arr[i]

        if(!isAlphaNumeric(decryptedStr.charAt(decryptedStr.length-1)))
            decryptedStr = decryptedStr.substring(0, decryptedStr.length - decryptedStr.charAt(decryptedStr.length-1).charCodeAt(0))


        return decryptedStr
    }


    createFromEncryptedString(encryptedStr){
        this.state_arr = []
        encryptedStr = atob(encryptedStr)

        while(encryptedStr !== ""){
            let i = 0
            for(let j = 0; j < 4; j++){
                let st = encryptedStr.substring(encryptedStr.length-1, encryptedStr.length)
                let charCode = st.charCodeAt(0)
                let shift = 8 * (3-j)
                i = i | ((charCode)<< shift)
                encryptedStr = encryptedStr.substring(0,encryptedStr.length-1)
            }
            this.state_arr.unshift(i)
        }
        return this
    }

    toString(){

        let str  = "State Array = <br><table>"
        for(let i = 0; i < bytes_per_row; i++){
            str += "<tr>"
            for(let j = 0; j < bytes_per_row; j++){
                str += "<td>" + this.state_arr[(i *bytes_per_row + j)] + "<td/>"
            }
            str += "</tr>"
        }
        return str + "</table>"
    }

}

function index(i,j){
    return (i *bytes_per_row + j)
}

function isAlphaNumeric(str) {
    let code, i, len

    for (i = 0, len = str.length; i < len; i++) {
        code = str.charCodeAt(i);
        if (!(code > 47 && code < 58) && // numeric (0-9)
            !(code > 64 && code < 91) && // upper alpha (A-Z)
            !(code > 96 && code < 123)) { // lower alpha (a-z)
            return false
        }
    }

    return true;
}