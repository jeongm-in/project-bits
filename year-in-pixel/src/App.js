import React from 'react';
import Year from './Components/Year';
import Count from './Components/Count';
import Front from './Components/Front';
import fire from './Fire';

import './App.css';

class App extends React.Component {
  // constructor(props) {
  //   super(props);
  // }

  render() {
    return (
      <div className="front-bg d-flex flex-row justify-content-around align-items-center">
        <div className="front-box-parent d-flex flex-row justify-content-around align-items-center">
        <div className="d-flex flex-column justify-content-around align-items-center">
        <Front/>
        </div>
        <Year/>

        </div>
      </div>
    );
  }
}

export default App;
