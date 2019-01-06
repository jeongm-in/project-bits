import React from 'react';
import fire from '../Fire';
class Year extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            invalid:{
                '1':[],
                '2':[29,30,31],
                '3':[],
                '4':[31],
                '5':[],
                '6':[31],
                '7':[],
                '8':[],
                '9':[31],
                '10':[],
                '11':[31],
                '12':[],
            },
            month: {
                "1": "Ja", "2": "Fe", "3": "Ma", '4': "Ap", '5': "Ma", "6": 'Ju',
                "7": 'Ju', '8': 'Au', '9': "Se", '10': 'Oc', '11': 'No', '12': 'De'
            },
            mood:{
                '0':['transparent','none'],'1':['#fbc531','Happy'],'2':['#74b9ff','Average'],'3':['#9980FA','Sad'],
                '4':['#ED4C67','Angry'],'5':['#4cd137','Lonely'],'6':['#7f8fa6','Tired'],
            },
            moodName:{
                
            },
            year:'',

        }
        this.onClick = this.onClick.bind(this);
        this.doNothing = this.doNothing.bind(this);
        this.onDoubleClick = this.onDoubleClick.bind(this);
        this.loadYear = this.loadYear.bind(this);
    }

    

    onDoubleClick=(event)=>{
        event.preventDefault();
        document.getElementById(event.target.id).setAttribute('style',
        'background:'+this.state.mood[0][0]);
        document.getElementById(event.target.id).setAttribute('mood',0);
    }



    onClick= (event)=>{
        let currentMood = event.target.getAttribute('mood');
        currentMood ++;
        currentMood %= 7;
        document.getElementById(event.target.id).setAttribute('style',
        'background:'+this.state.mood[currentMood][0]);
        document.getElementById(event.target.id).setAttribute('mood',currentMood);
    }

    doNothing=event=>{

    }
           
    componentDidMount(){
        this.loadYear();
    }
    
    loadYear(){
        var yearRef = fire.database().ref('users/0/jeongmin/year');
        let moodYear= 100;
        yearRef.on('value',function(snapshot){
            moodYear = snapshot.val();
            console.log(snapshot.val());
            // console.log(moodYear);
            // myMood = snapshot.val();           
        }, function(error){
            console.log('error:'+error.code);
        });
        console.log(this.state.year);
        this.setState({year:moodYear});
        console.log(this.state.year);
    }



    render() {
        let monthTitle = [];
        monthTitle.push(<th className="cell-size" key='first-row' 
        id="first-row">▼</th>)
        for (let m = 1; m < 13; m++) {
            monthTitle.push(<th className="cell-size"
             key={m + '_' + this.state.month[m]}
              id={this.state.month[m]}>{this.state.month[m]}</th>);
        }
        let days = [];
        for (let d = 1; d < 32; d++) {
            let dayBoxes = [];
            for (let i = 1; i < 13; i++) {
                dayBoxes.push(<th className=
                    {this.state.invalid[i].includes(d)?'cell-size cell-invalid':
                    'cell-size'}
                 key={'day_' + d + '_' + i} id={i + '_' + d} 
                 onClick={this.state.invalid[i].includes(d)?this.doNothing:this.onClick}
                 onDoubleClick = {this.onDoubleClick}
                 mood="0"></th>);
            }

            let dRow = (<tr key={"day_day_"+d}>
                <th className="cell-size" key={'day_'+d}>
                    {d < 10 ? '0' + d : d}
                </th>
                {dayBoxes}
            </tr>);
            days.push(dRow);
        }

        let moodLegend = [];
        for(let i = 1; i < 7; i++){
            moodLegend.push(<div key={this.state.mood[i][1]} className="d-flex
            flex-row justify-content-between align-items-center year-legend-row">
                <div className="year-legend-color" style={{'backgroundColor':this.state.mood[i][0]}}>
                </div>
                <div>
                {this.state.mood[i][1]}
                </div>    
            </div>);
        }
        
        return (
            <div className="year-pixel d-flex flex-row
             justify-content-around align-items-center">
                <table className="year-table">
                    <tbody>
                        <tr>
                            {monthTitle}
                        </tr>
                        {days}

                    </tbody>
                </table>
                <div className='year-legend d-flex flex-column justify-content-around align-items-center'>
                    <div className = "front-year-text">{this.state.year}</div>
                    {moodLegend}
                </div>
            </div>

        );
    }
}

export default Year;
