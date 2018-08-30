import React, { Component } from 'react'
import marked from "marked"
import Header from "./Header"

class WriteUp extends Component {

    constructor(props){
        super(props)

        this.state = {
            markdown: "",
        }
    }

    componentWillMount() {
        const readmePath = require("../markdown/README.md");

        fetch(readmePath)
            .then(response => {
                return response.text()
            })
            .then(text => {
                this.setState({
                    markdown: marked(text)
                })
            })
    }

    render() {
        let { markdown } = this.state;

        return (
            <div>

                <Header
                    title={"Learn Encryption"}
                />

                <article dangerouslySetInnerHTML={{__html: markdown}} />

            </div>
        )
    }
}

export default WriteUp;
