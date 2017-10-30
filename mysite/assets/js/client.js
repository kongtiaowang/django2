
import React from "react";
import ReactDOM from "react-dom";

// import Layout from "./components/Layout";

class Welcome extends React.Component {
  constructor(props){
    super(props)
     this.state = {
     	isEditable:true
     };
  }

  handleClick(){
  	let stateEditable = !this.state.isEditable;
  	this.setState({
        isEditable:stateEditable
    });
  }
  render() {
  	if (this.state.isEditable){
       return (
       	<div>
       	   <h1 onClick={this.handleClick.bind(this)}>Is Editable!</h1>
       	   <div>{this.props.propsData}
       	   </div>
        </div> 
        )

  	} else {
       return (
       	<div>
       	   <h1 onClick={this.handleClick.bind(this)}>Is not Editable?</h1>
        </div> 
        )
  	}
  }
};


ReactDOM.render(
  <Welcome propsData="{name:'ni',last:'hao'}"/>,
  document.getElementById('app')
);