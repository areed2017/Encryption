function prepareKey(key) {
    while(key.length < 16){
        key += String.fromCharCode(Math.floor((Math.random() * 55) + 1))
    }
    return key
}

class AES {

    constructor(mode){

        if(mode === "ECB")
            this.mode = 0
        else if(mode === "CBC")
            this.mode = 1
        else
            this.mode = -1

    }

    encrypt(key, iv, text){

        if(this.mode === 0){
            let state_arr = new StateArray(text)
            let round_keys = new RoundKeys(key)

            state_arr.rot13()
            state_arr.row_shift()
            state_arr.round_xor(round_keys)

            return state_arr.getEncryptedString()
        }
        else if(this.mode === 1){
            let state_arr = new StateArray(text)
            let round_keys = new RoundKeys(key)
            let iv_keys = new RoundKeys(iv)

            state_arr.rot13()
            state_arr.row_shift()
            state_arr.round_xor(round_keys)
            state_arr.round_xor(iv_keys)

            return btoa(iv).substring(0,btoa(iv).length - 2) + state_arr.getEncryptedString()
        }

        return null
    }

    decrypt(key, text){

        if(this.mode === 0){

            let state_arr = new StateArray().createFromEncryptedString(text)
            let round_keys = new RoundKeys(key)

            state_arr.round_xor(round_keys)
            state_arr.row_un_shift()
            state_arr.reverse_rot13()

            return state_arr.getDecryptedString()
        }
        else if(this.mode === 1){

            let iv = text.substring(0,22) + "=="
            text = text.substring(22, text.length)

            let state_arr = new StateArray().createFromEncryptedString(text)
            let round_keys = new RoundKeys(key)
            let iv_keys = new RoundKeys(atob(iv))

            state_arr.round_xor(iv_keys)
            state_arr.round_xor(round_keys)
            state_arr.row_un_shift()
            state_arr.reverse_rot13()

            return state_arr.getDecryptedString()
        }

        return null
    }


}