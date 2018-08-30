import React, { Component } from 'react';

class Header extends Component {

    render() {
        let { title } = this.props
        return (
            <div className="row">
                <div className="col-md-12 left-align">
                    <h2 className="dark-text">
                        {title}
                        <hr />
                    </h2>
                </div>
            </div>
        )
    }
}

export default Header;
