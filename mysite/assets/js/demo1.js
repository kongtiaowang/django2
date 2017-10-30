import React from "react";
import ReactDOM from "react-dom";
//todo ----------- getData from list and pass data to items and itme
var people = [
            {name:"wang shen",age:38},
            {name:"wang ying",age:38},
            {name:"wang jia hang",age:9},
            {name:"wang zoe",age:3},
  	   	   ];

// Items component
class Items extends React.Component {
  constructor(props){
    super(props);

    this.state={
    	data:[],
    };
  }
  componentWillMount(){
    alert("items will mount");
           this.setState({data:this.props.data});
   }

  render() {
  const datas = this.state.data;
  var itemNode = datas.map((people,index)=>
    {
    	return (
         <Item data={people} id={index}/>
    	)
    }
  	);

  	return (
  	<div>
  	    {itemNode}
  	</div>
  	)
  }
};
//Item
class Item extends React.Component {
  constructor(props){
    super(props);
    this.state={
    	enableAdd:false,
    };
  }

  render() {
  const condition = this.state.enableAdd;
  if (condition) {
    return (
  	<div>
  	    <li className="list-group-item"><input type="text" id="name" value={this.props.data.name} /> <input type="text" id="age" value={this.props.data.age} /><a href="#">confirm</a></li>
  	</div>
  	)
  } else {
     return (
  	<div>
  	    <li className="list-group-item">{this.props.data.name} | {this.props.data.age} <a href="#">update</a> <span> | </span><a href="#">delete</a></li>
  	</div>
  	)
    }
  }
 };

//List
class List extends React.Component {
	constructor(props){
    super(props);
    this.state = {
      	addStatus:false,
        data:[]
        // insertStatus:false,
        };
  }
  componentWillMount(){
    this.setState({data:people});
  }

  handleAdd(){
    this.setState({addStatus:true});
  }
  //todo add newPeople to itmes
  handleChange(){
    alert("fjdlksk");
    let newname = document.getElementById("name").value;
    let newage = document.getElementById("age").value;
    // this.setState({newPeople: {"name":newname,"age":newage}});
    this.setState({addStatus:false});    //reload Items ???

    if (newname!==null)
             {
               people.push({name:newname,age:newage});
               this.setState({data:people});
             }

    // this.setState({insertStatus: true});
  }

  render()
  {

     //return (<div>hello</div>);
   let addCondition = this.state.addStatus;
   if (addCondition){
     return (
       <div className="container" id="container">
       		<button className="btn btn-default">Add</button>
     	  	<ul className="list-group">
     	  	<li className="list-group-item"><input type="text" id="name" /> <input type="text" id="age" /><a href="#" onClick={this.handleChange.bind(this)}>confirm</a></li>
              	<Items data={this.state.data} value={this.state.newPeople}/>
     	  	</ul>
     	</div>);
   } else {
     return (
       <div className="container" id="container">
       			<button className="btn btn-default" onClick={this.handleAdd.bind(this)}>Add</button>
     	  		<ul className="list-group">
              	<Items data={this.state.data} />
     	  		</ul>
     			</div>);
   }
    };
};

 ReactDOM.render(
    <List />,
  document.getElementById('react_demo')
)
