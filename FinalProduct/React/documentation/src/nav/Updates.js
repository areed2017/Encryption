import React, { Component } from 'react';
import Header from "./Header"

class Updates extends Component {

    render() {
        return (
            <div>

                <Header
                    title={"Version History"}
                />

                <div className="row">
                    <div className="col-md-12">

                        <hr />

                        <h4>Changelog</h4>

                        <pre className="brush: html">

                        -----------------------------------------------------------------------------------------<br/>
                        Version 1.0 - August 30th, 2018<br/>
                        -----------------------------------------------------------------------------------------<br/>

                        - AES Encryption/Decryption Support<br/>
                        - RSA Encryption/Decryption Support<br/>
                        - BlowFish Encryption/Decryption Support<br/>
                        - Triple DES Encryption/Decryption Support<br/>

                        </pre>

                    </div>
                </div>
            </div>
        )
    }
}

export default Updates;
