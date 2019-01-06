import React from 'react';
class Front extends React.Component {
    // constructor(props) {
    //     super(props);
    // }

    render() {
        return (
            <div className="front-parent d-flex flex-column
            justify-content-between align-items-center">
                <div className = "front-title-box">
                <div className = "front-title-text">
                    Year in Pixels
                </div>
                </div>
                <div className = "front-other-box d-flex flex-column justify-content-between align-items-ceneter">
                    <div>

                    </div>
                </div>
                <div className = 'front-other-footer d-flex flex-row'>
                <div>#YearInPixels by Camille</div>&nbsp;
                    <a href="https://www.instagram.com/passioncarnets/">(@passioncarnets)</a>
                </div>
            
            
            
            </div>
        );
    }
}

export default Front;
