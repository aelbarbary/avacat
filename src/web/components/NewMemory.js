import React, { Component } from 'react';
import { Firebase, FirebaseRef } from '../../lib/firebase';
import { Alert, FormGroup, Button, Input } from 'reactstrap';

const valueStyle = {
  width: '100%'
}
const keyStyle = {
  width: '100%'
}

class NewMemory extends Component {

  constructor(props) {
    super(props);
    this.state = {
      alertVisible: false,
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

  handleKeyChange(e){
    this.setState({memoryKey: e.target.value});
  }
  handleValueChange(e){
    this.setState({memoryValue: e.target.value});
  }
  handleClick(e){
    console.log(this.state);

    const UID = Firebase.auth().currentUser.uid;
    if (!UID) return false;

    const ref = FirebaseRef.child(`memories`);
    const guid = this.guid()
    var newRef = ref.push({
        key: this.state.memoryKey,
        value: this.state.memoryValue
      }
    );

    var newDocRef = FirebaseRef.child('memories').doc(newRef);
    console.log(newDocRef);
    this.setState({memoryKey: "", memoryValue:"", alertVisible: true});

  }

  onDismiss() {
    this.setState({ alertVisible: false });
  }

  render() {
    {this.state.data}
    return (
          <form>
            <Alert color="success" isOpen={this.state.alertVisible} toggle={this.onDismiss.bind(this)}>
              Memory Saved.
            </Alert>
            <FormGroup>
              <Input
                type='text'
                name='key'
                placeholder="Memory Title"
                onChange={this.handleKeyChange.bind(this)}
                style={keyStyle}/>
            </FormGroup>
            <FormGroup>
              <Input
                type="textarea"
                name='value'
                placeholder="Memory Value"
                onChange={this.handleValueChange.bind(this)}
                style={valueStyle}
              />
            </FormGroup>
            <Button color="warning" onClick={this.handleClick.bind(this)}>Save</Button>
          </form>
    );
  }
}

export default NewMemory;
