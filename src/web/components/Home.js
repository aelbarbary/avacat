import React, {Component} from 'react';
import { Row, Col, Jumbotron, CardGroup, Card, CardImg, CardText, CardBody,
  CardTitle, CardSubtitle, Button } from 'reactstrap';

const searchBoxStyle = {
  width: '100%'
}
const formStyle = {
  width: '100%'
}

const cardGroupStyle ={
  margin: '50'
}

class Home extends Component {
  state= {memoriesList: []};
  constructor(props) {
    super(props);
    this.state = {};
  }

  // componentDidMount() {
  //
  //   console.log(memories);
  //   var memoriesList = memories.map(memory => <li> {memory.key} </li>);
  //   this.setState({memoriesList:memoriesList});
  // }
  render() {
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

    return (
      <div>
        <Row>
            <form style={formStyle}>
              <input type="text" style={searchBoxStyle}/>
            </form>
        </Row>
        <Row>
          <CardGroup style={cardGroupStyle}>
            {memoriesList}
          </CardGroup>
        </Row>
      </div>
    );
  }
}

export default Home;
