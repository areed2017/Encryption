
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

function display(encryptedStr, decryptedStr, includeLength=true){

    let body = document.getElementById("body")
    let view = ""
    let div = (text) => {
        return "<div style='width: 700px; word-wrap: break-word; '>" + text + "</div>"
    }

    view += "<br/><hr /><hr /><h2>Encrypted:</h2> " + div(encryptedStr)
    if(includeLength)
        view += "<br/><h2>Encrypted String length:</h2> " + encryptedStr.length
    view += "<hr /><hr /><br />"


    view += "<h2>Decrypted:</h2> " + div(decryptedStr)
    if(includeLength)
        view += "<br/><h2>Decrypted String length:</h2> " + decryptedStr.length
    view += "<hr /><hr />"

    for(let i = 0; i < 10; i ++)
        view += "<br/>"

    body.innerHTML = view
    return view
}

function exec_rsa() {

    let input = document.getElementById("rsa_input").value
    let modulus = document.getElementById("mod").value
    let public_exp = document.getElementById("public_exponent").value
    let private_exp = document.getElementById("private_exponent").value

    modulus = parseInt(modulus)
    public_exp = parseInt(public_exp)
    private_exp = parseInt(private_exp)

    let rsa_private = new RSA(modulus, private_exp)
    let rsa_public = new RSA(modulus, public_exp)

    let encryptedStr = rsa_public.encrypt(input)
    let decryptedStr = rsa_private.decrypt(encryptedStr)//"" //rsa_private.exec(encryptedStr)


    let view = "<br /><br /><h3>Process:</h3><br /> Result = ( <i>Input</i> <sup><i>Exponent</i></sup> ) * mod(<i>Modulus</i>) <br /> <br /> "
    view += display(btoa(encryptedStr), decryptedStr, false)

    document.getElementById("body").innerHTML = view
    return false
}

function exec_rsa_keys(){

    let rsa = new RSA()
    rsa.generate_pq()

    let modulus = rsa.setModulus()
    let phi = rsa.getPhi()

    let e = 0
    let value = Math.floor(Math.random() * (phi - 1)) + 2
    while( e === 0){
        if(value === 1)
            value = Math.floor(Math.random() * (phi - 1)) + 2

        if( gcd(phi, value) === 1 )
            e = value

        value--
    }

    let k = 1
    let possible = 1.1
    while( possible !== Math.floor(possible)){
        k += Math.floor(Math.random() * 10) + 1
        possible = (1 + k * phi) / e
    }
    let d = possible

    document.getElementById("mod").value = modulus
    document.getElementById("public_exponent").value = e
    document.getElementById("private_exponent").value = d
    return false
}

function exec_mod_and_exp(){
    let input = document.getElementById("rsa_input").value

    let rsa = new RSA()
    let body = document.getElementById("body")
    let view = ""

    let {p, q} = rsa.generate_pq()
    view += "<br /><br /><h3>Generate Two Prime Numbers</h3><br/>"
    view += "p = " + p + "<br />"
    view += "q = " + q + "<br />"

    let modulus = rsa.setModulus()
    view += "<br /><br /><h3>Find The Modulus</h3><br/>"
    view += "Modulus = p * q <br />"
    view += "Modulus = " + modulus + "<br />"

    let phi = rsa.getPhi()
    view += "<br /><br /><h3>Find a value for Φ(n)</h3><br/>"
    view += "Φ(n) = ( p - 1 ) ( q - 1 ) <br />"
    view += "Φ(n) = " + phi + " <br />"


    let e = 0
    let value = Math.floor(Math.random() * (phi - 1)) + 2
    while( e === 0){
        if(value === 1)
            value = Math.floor(Math.random() * (phi - 1)) + 2

        if( gcd(phi, value) === 1 )
            e = value

        value--
    }

    view += "<br /><br /><h3>Find a value for e ( e = public key's exponent )</h3><br/>"
    view += "e = Any value that is co-prime with Φ(n) and 1 < e < Φ(n) <br />"
    view += "e = " + e+ " <br />"


    let k = 1
    let possible = 1.1
    while( possible !== Math.floor(possible)){
        k += Math.floor(Math.random() * 10) + 1
        possible = (1 + k * phi) / e
    }
    let d = possible

    view += "<br /><br /><h3>Find a value for d ( d = private key's exponent )</h3><br/>"
    view += "d = Any value with a congruence relation of d e ≡ 1 <br />"
    view += "d = " + d + " <br />"


    let rsa_private = new RSA(modulus, d)
    let rsa_public = new RSA(modulus, e)

    let encryptedStr = rsa_public.exec(input)
    let decryptedStr = rsa_private.exec(encryptedStr)


    view += "<br /><br /><h3>Process:</h3><br /> Result = ( <i>Input</i> <sup><i>Exponent</i></sup> ) * mod(<i>Modulus</i>) <br /> <br /> "
    view += display(btoa(encryptedStr), decryptedStr, false)


    document.getElementById("mod").value = modulus
    document.getElementById("public_exponent").value = e
    document.getElementById("private_exponent").value = d

    for(let i = 0; i < 10; i ++)
        view += "<br/>"
    body.innerHTML = view
    return false
}
