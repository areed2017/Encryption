import React, { Component } from 'react';
import Header from "./Header"

class Python extends Component {

    render() {
        return (
            <div>
                <Header
                    title={"Python"}
                />

                <h4>Upload via WordPress Admin</h4>

                <p>Lorem the It is a long established fact that a reader will be distracted by the readable content
                    of a page when looking at its layout. The point of using Lorem Ipsum is that it has a
                    more-or-less normal distribution of letters, as opposed to using 'Content here, content here',
                    making it look like readable English.</p>

                <a href="#" className="btn btn-primary">Get a Installation Service</a>
                <a href="#" className="btn btn-info">Ask a Question</a>

                <hr />

                <h4>Upload via FTP Server</h4>

                <p>Lorem the It is a long established fact that a reader will be distracted by the readable
                    content of a page when looking at its layout. The point of using Lorem Ipsum is that it has
                    a more-or-less normal distribution of letters, as opposed to using 'Content here, content
                    here', making it look like readable English.</p>

                <a href="#" className="btn btn-primary">Get a Installation Service</a> <a href="#"
                                                                                          className="btn btn-info">Ask
                a Question</a>
                <hr />

                <div className="row">
                    <div className="col-md-6">
                        <div className="media">
                            <iframe width="560" height="315" src="https://www.youtube.com/embed/yQnQyI5WlKs"
                                    frameBorder="0" allowFullScreen></iframe>
                        </div>

                    </div>
                    <div className="col-md-6">
                        <div className="media">
                            <iframe width="560" height="315" src="https://www.youtube.com/embed/z0kEVwJB_go"
                                    frameBorder="0" allowFullScreen></iframe>
                        </div>

                    </div>
                </div>
            </div>
        )
    }
}

export default Python;
