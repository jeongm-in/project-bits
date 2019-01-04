import React from 'react';


class Navigation extends React.Component {
    constructor(props) {
        super(props);

    }


    render() {
        let navBarComp = (
            <nav className='navbar navbar-expand-lg navbar-light nav-bar-bg nav-s'>
                <div className="navbar-brand text-ligt font-weight-bold">Jeong Min Lim</div>
                <button className="btn btn-sm btn-primary">home</button>
                <button className="btn btn-sm btn-primary"></button>
            </nav>
        );
        return (
            <div>{navBarComp}</div>
        )

    }
}

export default Navigation;