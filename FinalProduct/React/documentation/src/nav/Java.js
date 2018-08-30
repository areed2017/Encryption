import React, { Component } from 'react';
import Header from "./Header"

class Java extends Component {

    render() {
        return (
            <div>
                <Header
                    title={"Java"}
                />

                <div className="intro2 clearfix">
                    <p>
                        <i className="fa fa-wordpress"> </i> Lorem the It is a long established fact that a reader will be
                        distracted..
                        <br /> Please read more about WordPress here. <a href="#">WordPress Installation via FTP.</a></p>
                </div>

                <hr />

                <h4>Upload via WordPress Admin</h4>

                <p>Lorem the It is a long established fact that a reader will be distracted by the readable content
                    of a page when looking at its layout. The point of using Lorem Ipsum is that it has a
                    more-or-less normal distribution of letters, as opposed to using 'Content here, content here',
                    making it look like readable English.</p>

                <a href="#" className="btn btn-primary">Get a Installation Service</a> <a href="#"
                                                                                          className="btn btn-info">Ask
                a Question</a>
                <div>
                    <div className="row">
                        <div className="col-md-8 col-md-offset-2">
                            <div className="media">
                                <iframe width="560" height="315" src="https://www.youtube.com/embed/snFzbPm_RUE"
                                        frameBorder="0" allowFullScreen> </iframe>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Java;
