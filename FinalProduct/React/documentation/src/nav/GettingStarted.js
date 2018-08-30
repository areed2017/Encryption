import React, { Component } from 'react';
import Header from "./Header"

class GettingStarted extends Component {

    render(){
        return (
            <div>
                <Header
                    title={"Getting Started"}
                />

                <div className="row">

                    <div className="col-md-12 full">
                        <div className="intro1">
                            <ul>
                                <li><strong>Item Name : </strong>All In One Crypto</li>
                                <li><strong>Author : </strong> Andrew Reed</li>
                                <li><strong>Language : </strong>Python</li>
                                <li><strong>Downloads :</strong>
                                    <ul>
                                        <li><strong>Version 1.0 : </strong>
                                            <a href={"downloads/aio_crypto.zip"} download>Download</a>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </div>

                        <hr />
                        <div>
                            <p><br/>
                                All in one encryption was made to allow use of encryption in a easier
                                manor and teach one to use encryption as well
                            </p>

                        </div>
                    </div>


                </div>
                    {/*<div className="row">*/}
                        {/*<div className="col-md-12">*/}
                            {/*<p>Lorem the It is a long established fact that a reader will be distracted by the readable content*/}
                                {/*of a page when looking at its layout. The point of using Lorem Ipsum is that it has a*/}
                                {/*more-or-less normal distribution of letters, as opposed to using 'Content here, content here',*/}
                                {/*making it look like readable English.</p>*/}

                            {/*<h4>Bootstrap Grid System</h4>*/}

                            {/*<pre className="brush: html; highlight: [2,4]">*/}
                                {/*<div className="container">*/}
                                    {/*<div className="row">*/}
                                        {/*<div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">*/}
                                            {/*YOUR CODES GOES HERE*/}
                                        {/*</div>*/}
                                    {/*</div>*/}
                                {/*</div></pre>*/}

                            {/*<p>Our you can use the grid system with 2 columns like this;</p>*/}

                            {/*<pre className="brush: html">*/}
                                {/*<div className="container">*/}
                                    {/*<div className="row">*/}
                                        {/*<div className="col-lg-6 col-md-6 col-sm-6 col-xs-12">*/}
                                            {/*YOUR CODES GOES HERE*/}
                                        {/*</div>*/}
                                        {/*<div className="col-lg-6 col-md-6 col-sm-6 col-xs-12">*/}
                                            {/*YOUR CODES GOES HERE*/}
                                        {/*</div>*/}
                                    {/*</div>*/}
                                {/*</div>*/}
                             {/*</pre>*/}

                            {/*<p>Our you can use the grid system with 3 columns like this;</p>*/}

                            {/*<pre className="brush: html">*/}
                                {/*<div className="container">*/}
                                    {/*<div className="row">*/}
                                        {/*<div className="col-lg-4 col-md-6 col-sm-6 col-xs-12">*/}
                                            {/*YOUR CODES GOES HERE*/}
                                        {/*</div>*/}
                                        {/*<div className="col-lg-4 col-md-6 col-sm-6 col-xs-12">*/}
                                            {/*YOUR CODES GOES HERE*/}
                                        {/*</div>*/}
                                        {/*<div className="col-lg-4 col-md-6 col-sm-6 col-xs-12">*/}
                                            {/*YOUR CODES GOES HERE*/}
                                        {/*</div>*/}
                                    {/*</div>*/}
                                {/*</div>*/}
                             {/*</pre>*/}
                        {/*</div>*/}
                    {/*</div>*/}
                {/*</div>*/}
            </div>
        )
    }
}

export default GettingStarted;
