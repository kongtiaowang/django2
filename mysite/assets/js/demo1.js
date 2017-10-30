import React from "react";
import ReactDOM from "react-dom";
//todo ----------- getData from list and pass data to items and itme
var people = [
            {name:"Tom",age:38},
            {name:"Jerry",age:38},
            {name:"Fox",age:19},
            {name:"Mickey",age:23},
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
         <Item data={people} id={index} handleDelete={this.props.handleDelete}/>
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
        enableUpdate:false,
    };
  }
  handleUpdate(){
     this.setState({enableUpdate:true});
  }
  render() {
  const id = this.props.id;
  const update = this.state.enableUpdate;
  if (update) {
    return (
  	<div>
  	    <li className="list-group-item"><input type="text" id="name" value={this.props.data.name} /> <input type="text" id="age" value={this.props.data.age} /><a href="#">confirm</a></li>
  	</div>
  	)
  } else {
     return (
  	<div>
        <li className="list-group-item">{this.props.data.name} | {this.props.data.age} <a href="#"onClick={this.handleUpdate.bind(this)}>update</a> <span> | </span><a href="#" onClick={()=>this.props.handleDelete(id)}>delete</a></li>
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
  handleDelete(id){
    alert("delete"+id);
    people.splice(id,1);
    this.setState({data:people});

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
                <Items data={this.state.data} value={this.state.newPeople} handleDelete={this.handleDelete.bind(this)} />
     	  	</ul>
     	</div>);
   } else {
     return (
       <div className="container" id="container">
       			<button className="btn btn-default" onClick={this.handleAdd.bind(this)}>Add</button>
     	  		<ul className="list-group">
                <Items data={this.state.data} handleDelete={this.handleDelete.bind(this)} />
     	  		</ul>
     			</div>);
   }
    };
};

 ReactDOM.render(
    <List />,
  document.getElementById('react_demo')
)
