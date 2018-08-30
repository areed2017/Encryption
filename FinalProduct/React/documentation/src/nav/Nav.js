import React, { Component } from 'react';

class Nav extends Component {

    render() {
        let {
            show_getting_started,
            show_java,
            show_python,
            show_pres,
            show_write_up,
            show_updates
        } = this.props

        return (
            <nav className="docs-sidebar" data-spy="affix" data-offset-top="300" data-offset-bottom="200"
                 role="navigation">
                <ul className="nav">
                    <li><a onClick={() => show_getting_started() }>Getting Started</a></li>
                    <li><a onClick={() => show_java() }>Java</a></li>
                    <li><a onClick={() => show_python() }>Python</a></li>
                    <li><a onClick={() => show_pres() }>Presentation</a>
                    </li>
                    <li><a onClick={() => show_write_up() }>Write Up</a>
                    </li>
                    <li><a onClick={() => show_updates() }>Updates</a></li>
                </ul>
            </nav>
        )
    }
}

export default Nav;
