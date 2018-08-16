
const Rcon = [2,4,8,16,32,64,128,27,54,108]

class RoundKeys{

    constructor(key) {
        this.round = [[],[],[],[],[],[],[],[],[],[],[]]
        this.key = key

        if( key.length < 16 )
            return

        for(let i = 0; i < 4; i++){
            let value = 0

            for( let j = 0; j < 4; j++){
                let ind = index(i,j)
                value ^= this.key.charAt(ind).charCodeAt(0) << (j * 8)
            }

            this.round[0].push(value)
        }

        for( let i = 1; i < this.round.length; i++){

            this.round[i][0] = this.round[i-1][0] ^ this.round[i-1][3] >> 8 ^ Rcon[i]

            for(let j = 1; j < 4; j++)
                this.round[i][j] = this.round[i-1][j] ^ this.round[i][0]

        }

    }

    apply( value, key ) {
        for(let k = 1; k < this.round.length; k++)
            value = value ^ this.round[k][key]
        return value
    }

    toString() {
        let str = "<table cellpadding='10px'>" +
            "<tr>" +
                "<th>Key</th>" +
                "<th>Weight 0</th>" +
                "<th>Weight 1</th>" +
                "<th>Weight 2</th>" +
                "<th>Weight 3</th>" +
            "</tr>"

        for (let i = 1; i < this.round.length; i++) {
            str += "<tr><td>" + i + "</td>"
            for( let j = 0; j < this.round[i].length; j++ ){
                str += "<td>" + this.round[i][j] + "</td>"
            }
            str += "</tr>"
        }
        return str + "</table>"
    }



}