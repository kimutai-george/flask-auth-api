import React, { Component } from 'react'
import { login } from './UserFunctions'
import FlashMassage from 'react-flash-message';
import { MDBContainer, MDBRow, MDBCol, MDBInput, MDBBtn } from 'mdbreact';
import "@fortawesome/fontawesome-free/css/all.min.css";
import "bootstrap-css-only/css/bootstrap.min.css";
import "mdbreact/dist/css/mdb.css";


class Login extends Component {
  constructor() {
    super()
    this.state = {
      email: '',
      password: '',
      errors: {},
      message: {},
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

    const user = {
      email: this.state.email,
      password: this.state.password
    }
   
    login(user).then(res => {
      if (!res.error) {
        this.props.history.push(`/profile`)
       
      }
    })
  }

  style = {
    marginTop:200,
    marginLeft:250
    }

  render() {
    return (
      <MDBContainer style={this.style}>
      <MDBRow>
        <MDBCol md="6">
          <form noValidate onSubmit={this.onSubmit}>
            <p className="h5 text-center mb-4">Sign in</p>
            <div className="grey-text">
              <MDBInput
                label="Type your email"
                icon="envelope"
                name="email"
                value={this.state.email}
                onChange={this.onChange}
                group
                type="email"
                validate
                error="wrong"
                success="right"
              />
              <MDBInput
                label="Type your password"
                icon="lock"
                name="password"
                value={this.state.password}
                onChange={this.onChange}
                group
                type="password"
                validate
              />
            </div>
            <div className="text-center">
              <MDBBtn type="submit">Login</MDBBtn>
            </div>
          </form>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
      
    )
  }
}

export default Login
