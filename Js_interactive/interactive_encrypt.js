
function exec(){
    let text = document.getElementById("input").value + ""
    let key = document.getElementById("key").value
    let body = document.getElementById("body")
    let view = ""

    let div = (text) => {
        return "<div style='display: inline-block; padding: 20px;'>" + text + "</div>"
    }

    view += "<br /> <small><u>Note</u>: In rundown mode only the first block is shown ( first 16 bites of the text )</small><br />"

    key = prepareKey(key)
    let round_keys = new RoundKeys(key)
    view += "<h3>Create Round Keys</h3><br/>" + round_keys.toString()

    let state_arr = new StateArray(text)
    view += div("<h3>Load Text into state Array</h3><br/>" + state_arr.toString())

    view += div("<span style='font-size: 50px'>&#x2192;</span>")

    state_arr.rot13()
    view += div("<h3>Apply ROT13 to state Array</h3><br/>" + state_arr.toString())

    view += div("<span style='font-size: 50px'>&#x2192;</span>")

    state_arr.row_shift()
    view += div("<h3>Apply Row Shift to state Array</h3><br/>" + state_arr.toString())


    state_arr.round_xor(round_keys)
    view += div("<h3>Apply Row Xor to state Array</h3><br/>" + state_arr.toString())

    view += "<div style='font-size: 50px'>&#x2193;</div>"

    let encryptedStr = state_arr.getEncryptedString()
    view += "<h2>Encrypted String:</h2> " + encryptedStr
    view += "<br/><h2>Encrypted String length:</h2> " + encryptedStr.length
    view += "<hr /><hr /><br />"



    view += "<h1><u>Decryption</u></h1><br/>"
    view += "<h3>Encrypted String</h3><br/>"
    view += encryptedStr
    view += "<h3>Encrypted String Length</h3><br/>"
    view += encryptedStr.length

    view += "<br/><br/><h3>Create Round Keys</h3><br/>"
    round_keys = new RoundKeys(key)
    view += round_keys.toString()

    state_arr = new StateArray().createFromEncryptedString(encryptedStr)
    view += div("<h3>Derive the state array state Array</h3><br/>" + state_arr.toString())

    view += div("<span style='font-size: 40px'>&#x2192;</span>")

    state_arr.round_xor(round_keys)
    view += div("<h3>Apply Row Xor to state Array</h3><br/>" + state_arr.toString())

    view += div("<span style='font-size: 40px'>&#x2192;</span>")

    state_arr.row_un_shift()
    view += div("<h3>Apply Row Un-shift to state Array</h3><br/>" +  state_arr.toString())


    state_arr.reverse_rot13()
    view += "<br /><h3>Apply ROT13 to state Array</h3><br/>" + state_arr.toString()


    view += "<div style='font-size: 50px'>&#x2193;</div>"

    let decryptedStr = state_arr.getDecryptedString()
    view += "<h2>Decrypted String:</h2> " + decryptedStr
    view += "<br/><h2>Decrypted String length:</h2> " + decryptedStr.length

    for(let i = 0; i < 10; i ++)
        view += "<br/>"
    body.innerHTML = view
    return false
}

function exec_ecb() {
    let text = document.getElementById("input").value
    let key = document.getElementById("key").value

    key = prepareKey(key)

    let encryptedStr = ""
    for(let i = 0; i < text.length; i+=16)
        encryptedStr += new AES("ECB").encrypt(key, null, text.substring(i, i + 16))

    let decryptedStr = ""
    for(let i = 0; i < encryptedStr.length; i+=88)
        decryptedStr += new AES("ECB").decrypt(key, encryptedStr.substring(i, i + 88))

    return display (encryptedStr, decryptedStr)
}


function exec_cbc() {
    let text = document.getElementById("input").value + ""
    let key = document.getElementById("key").value
    let iv = document.getElementById("iv").value

    key = prepareKey(key)
    iv = prepareKey(iv)

    let encryptedStr = ""
    for(let i = 0; i < text.length; i+=16)
        encryptedStr += new AES("CBC").encrypt(key, iv, text.substring(i, i + 16))

    let decryptedStr = ""
    for(let i = 0; i < encryptedStr.length; i+=110)
        decryptedStr += new AES("CBC").decrypt(key, encryptedStr.substring(i, i + 110))

    display(encryptedStr, decryptedStr)

    return false
}


function display(encryptedStr, decryptedStr){

    let body = document.getElementById("body")
    let view = ""
    let div = (text) => {
        return "<div style='width: 700px; word-wrap: break-word; '>" + text + "</div>"
    }

    view += "<hr /><hr /><h2>Encrypted String:</h2> " + div(encryptedStr)
    view += "<br/><h2>Encrypted String length:</h2> " + encryptedStr.length
    view += "<hr /><hr /><br />"


    view += "<hr /><hr /><h2>Decrypted String:</h2> " + div(decryptedStr)
    view += "<br/><h2>Decrypted String length:</h2> " + decryptedStr.length

    for(let i = 0; i < 10; i ++)
        view += "<br/>"

    body.innerHTML = view
}