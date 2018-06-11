import React, {Component} from 'react';
import { Row, Col, Jumbotron, CardGroup, Card, CardImg, CardText, CardBody,
  CardTitle, CardSubtitle, Button, CardColumns } from 'reactstrap';

class Home extends Component {
  state= {memoriesList: []};
  constructor(props) {
    super(props);
    this.state = {};
  }

  componentWillMount() {
    const memories =  this.props.memories;
    console.log(memories);
    const memoriesList = memories.map(memory =>
         <Card>
           <CardBody>
             <CardTitle>{memory.val().key}</CardTitle>
             <CardText>{memory.val().value}</CardText>
             <Button>Like</Button>
           </CardBody>
         </Card>
       );

    this.setState({memoriesList:memoriesList});
  }

  setSearchText(event) {
     let searchText = event.target.value;
     console.log(searchText);
     this.setState({searchText});

     const memories =  this.props.memories;
     let filteredData = this.filterMemories(searchText, memories);
     console.log(filteredData);
     this.setState({
         memoriesList: filteredData.map(memory =>
              <Card>
                <CardBody>
                  <CardTitle>{memory.val().key}</CardTitle>
                  <CardText>{memory.val().value}</CardText>
                  <Button>Like</Button>
                </CardBody>
              </Card>
            ),
         rawData: memories,
       });
  }

  filterMemories(searchText, memories) {
    let text = searchText.toLowerCase();
    console.log(text);
    return memories.filter( function(m) {
      console.log(m);
      let memory = m.val().key.toLowerCase();
      return memory.search(text) !== -1;
    });
  }

  render() {

    return (
      <div>
        <Row>
            <form className="search">
              <input type="text" onChange={this.setSearchText.bind(this)} placeholder="Search"/>
            </form>
        </Row>
        <Row>
          <CardColumns>
            {this.state.memoriesList}
          </CardColumns>
        </Row>
      </div>
    );
  }
}

export default Home;
