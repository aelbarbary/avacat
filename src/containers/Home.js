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

    ref.on("value", function(snapshot) {
      var memories = []
      snapshot.forEach( function(child){
        memories.push(child);
      });
      
      this.setState({memories: memories})
    }.bind(this), function (errorObject) {
      console.log("The read failed: " + errorObject.code);
    });
  }

  render() {
    const { Layout } = this.props;
    return (
      <Layout memories={this.state.memories}/>
    );
  }

}
// const mapDispatchToProps = {
//   getMemories,
// };

export default HomeContainer;
