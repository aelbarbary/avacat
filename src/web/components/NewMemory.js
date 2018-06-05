import React, { Component } from 'react';
import { Firebase, FirebaseRef } from '../../lib/firebase';

class NewMemory extends Component {

  constructor(props) {
    super(props);
    this.state = {

    };

    this.guid.bind(this);
    this.s4.bind(this);
  }

  s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  }

  guid() {
   return this.s4() + this.s4() + '-' + this.s4() + '-' + this.s4() + '-' + this.s4() + '-' + this.s4() + this.s4() + this.s4();
  }

  handleChange(e){
    this.setState({memory: e.target.value});
  }
  handleClick(e){
    console.log(this.state);


    const UID = Firebase.auth().currentUser.uid;
    if (!UID) return false;

      const ref = FirebaseRef.child(`memories`);
      const guid = this.guid()
      ref.set({
        [guid]: {
          memory: this.state.memory
        }
      });

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
