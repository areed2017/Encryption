import React, { Component } from 'react';
import './App.css';
import Nav from "./nav/Nav"
import Getting_Started from "./nav/GettingStarted"
import Java from "./nav/Java"
import Python from "./nav/Python"
import Pres from "./nav/Pres"
import WriteUp from "./nav/WriteUp"
import Updates from "./nav/Updates"

class App extends Component {

    constructor(props) {
        super(props)

        this.state = {
            show_getting_started: true,
            show_java: false,
            show_python: false,
            show_pres: false,
            show_write_up: false,
            show_updates: false,
        }
    }

    changeTo = ( show ) => {
        let state = this.state

        for (let key in state) {
            if (!state.hasOwnProperty(key))
                continue;
            state[key] = false;
        }
        state[show] = true

        this.setState({...state})
    }

    render() {
        let {
            show_getting_started,
            show_java,
            show_python,
            show_pres,
            show_write_up,
            show_updates
        } = this.state


        return (
            <div className="App">

                <div className="row">
                    <div className="col-md-12">
                        <div className="big-title text-center">
                            <h1>All In One Encryption</h1>
                            <p className="lead">version 1.0</p>
                        </div>
                    </div>
                </div>



                <div className="row">
                    <hr width="50%"/>

                    <div className="col-md-3">
                        <Nav
                            show_getting_started={ () => this.changeTo("show_getting_started") }
                            show_java={() => this.changeTo("show_java") }
                            show_python = { () => this.changeTo("show_python") }
                            show_pres = { () => this.changeTo("show_pres") }
                            show_write_up = { () => this.changeTo("show_write_up") }
                            show_updates = { () => this.changeTo("show_updates") }
                        />
                    </div>

                    <div className="col-md-9">
                        <div style={{width:"90%"}} align="left">
                            { show_getting_started &&
                                <Getting_Started />
                            }

                            { show_java &&
                                <Java />
                            }

                            { show_python &&
                                <Python />
                            }

                            { show_pres &&
                                <Pres />
                            }

                            { show_write_up &&
                                <WriteUp />
                            }
                            { show_updates &&
                                <Updates />
                            }
                        </div>
                    </div>
                </div>

            </div>
        );
    }
}

export default App;
