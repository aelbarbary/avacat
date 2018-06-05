import React from 'react';
import { Row, Col, Jumbotron } from 'reactstrap';

const searchBoxStyle = {
  width: '100%'
}
const formStyle = {
  width: '100%'
}

const About = () => (
  <div>
    <Row>
        <form style={formStyle}>
          <input type="text" style={searchBoxStyle}/>
        </form>
    </Row>

  </div>
);


export default About;
