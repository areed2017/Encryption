import React, { Component } from 'react';

import { Document, Page } from 'react-pdf'

class Pres extends Component {

    constructor(props){
        super(props)

        this.state = {
            numPages: null,
            pageNumber: 1,
        }
    }

    onDocumentLoad = ({ numPages }) => {
        this.setState({ numPages });
    }

    render() {
        let { pageNumber, numPages } = this.state;

        return (
            <div>
                <div align="center">
                    <Document
                        file="slides/Encryption.pdf"
                        onLoadSuccess={this.onDocumentLoad}
                    >
                        <Page
                            width={1100}
                            pageNumber={pageNumber}
                        />
                    </Document>

                    <hr />

                    <button
                        onClick={() => {this.setState({pageNumber:pageNumber-=1})}}
                        style={{marginRight:"10px"}}
                    >
                        Previous Page
                    </button>
                    Page {pageNumber} of {numPages}
                    <button
                        onClick={() => {this.setState({pageNumber:pageNumber+=1})}}
                        style={{marginLeft:"10px"}}
                    >
                        Next Page
                    </button>
                </div>
            </div>
        )
    }
}

export default Pres;
