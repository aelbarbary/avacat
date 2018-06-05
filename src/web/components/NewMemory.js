import React, { Component } from 'react';

class NewMemory extends Component {

  constructor(props) {
    super(props);
    this.state = {
      
    };
  }

  handleChange(e){
    this.setState({memory: e.target.value});
  }
  handleClick(e){
    console.log(this.state);
  }
  render() {
    {this.state.data}
    return (
      <form>
        <input type='text' name='title' onChange={this.handleChange.bind(this)}/>
        <input type='button' value="create" onClick={this.handleClick.bind(this)}/>
      </form>

    );
  }

}

export default NewMemory;
