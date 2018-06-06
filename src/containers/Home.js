import React, { Component } from 'react';
import PropTypes from 'prop-types';
// import { getMemories } from '../actions/memories';
import { Firebase, FirebaseRef } from '../lib/firebase';

class HomeContainer extends Component {
  state= {memories: []}
  static propTypes = {
    Layout: PropTypes.func.isRequired,
  }

  constructor(props) {
    super(props);
  }

  componentDidMount(){
    if (Firebase === null) return () => new Promise(resolve => resolve());

    const ref = FirebaseRef.child(`memories`);
    const { Layout } = this.props;
    ref.on("value", function(snapshot) {
      var memories = []
      snapshot.forEach( function(child){
        memories.push(child);
      });
      var memoriesList = <Layout memories={memories}/>
      this.setState({memories: memoriesList})
    }.bind(this), function (errorObject) {
      console.log("The read failed: " + errorObject.code);
    });
  }

  render() {
    console.log(this.state.memories);
    return (
      this.state.memories
    );
  }
}

export default HomeContainer;
