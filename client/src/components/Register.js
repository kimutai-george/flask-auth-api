import React, { Component } from 'react'
import { register } from './UserFunctions'
import FlashMassage from 'react-flash-message';

import { MDBContainer, MDBRow, MDBCol, MDBInput, MDBBtn, MDBCard, MDBCardBody } from 'mdbreact';
import "@fortawesome/fontawesome-free/css/all.min.css";
import "bootstrap-css-only/css/bootstrap.min.css";
import "mdbreact/dist/css/mdb.css";

class Register extends Component {
  constructor() {
    super()
    this.state = {
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      errors: {},
      response:'',
    }

    this.onChange = this.onChange.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }

  onChange(e) {
    this.setState({ [e.target.name]: e.target.value })
  }
  onSubmit(e) {
    e.preventDefault()
    e.target.className += " was-validated";

    const newUser = {
      first_name: this.state.first_name,
      last_name: this.state.last_name,
      email: this.state.email,
      password: this.state.password,
      response:this.state.response,

    }
    

    register(newUser).then(res => {
      
      this.props.history.push(`/register`)
      
    })
  }

  style = {
    marginTop:200,
    marginLeft:250
    }

  render() {
    return (
     
      <MDBContainer  style={this.style}> 
       <MDBRow>
        <MDBCol md="6">
       
          <form className="needs-validation" noValidate onSubmit={this.onSubmit}>
            <p className="h5 text-center mb-4">Sign up</p>
            <p>{this.state.response}</p>
            <div className="grey-text">
              <MDBInput
                label="First Name"
                icon="user"
                name="first_name"
                value={this.state.first_name}
                onChange={this.onChange}
                group
                type="text"
                validate
                error="wrong"
                success="right"
                required
              />
               <MDBInput
                label="Last Name"
                icon="user"
                name = "last_name"
                value={this.state.last_name}
                onChange={this.onChange}
                group
                type="text"
                validate
                error="wrong"
                success="right"
                required
              />
              <MDBInput
                label="Email Address"
                icon="envelope"
                name="email"
                value={this.state.email}
                onChange={this.onChange}
                group
                type="email"
                id="materialFormRegisterConfirmEx3"
                validate
                error="wrong"
                success="right"
                required
              />
            
              <MDBInput
                label="Password"
                icon="lock"
                name="password"
                value={this.state.password}
                onChange={this.onChange}
                group
                type="password"
                validate
                required
              />
            </div>
            <div className="text-center">
              <MDBBtn type="submit" color="primary">Register</MDBBtn>
            </div>
          </form>
        
        </MDBCol>
      </MDBRow>
    </MDBContainer>
 

    )
  }
}

export default Register
