import React from 'react';
import Year from './Components/Year';
import Count from './Components/Count';
import Front from './Components/Front';

import './App.css';

class App extends React.Component {
  // constructor(props) {
  //   super(props);
  // }

  render() {
    return (
      <div className="front-bg d-flex flex-row justify-content-around align-items-center">
        <Year/>
        <div className="d-flex flex-column justify-content-around align-items-center">
        <Count/>
        <Front/>
        </div>
      </div>
    );
  }
}

export default App;
