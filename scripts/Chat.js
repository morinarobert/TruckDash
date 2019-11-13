import * as React from 'react';

import { Socket } from './Socket';


export class Chat extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            username: '', 
            message: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleUsernameChange = this.handleUsernameChange.bind(this);
        this.handleMessageChange = this.handleMessageChange.bind(this);
    }
    
    handleUsernameChange(event){
        this.setState({username: event.target.value});
        document.getElementById('ur').value = "";
    }
    
    handleMessageChange(event){
        this.setState({message: event.target.value});
        document.getElementById('msg').value = "";
    }
    
    handleChange(event){
        this.setState({username: event.target.value});
    }
    
    
    
    handleSubmit(event) {
        event.preventDefault();
        let usrmessage = this.state.message;
        // let usrnme = this.state.username;
        Socket.emit('new message',  {
            'Message': usrmessage
        });
        console.log('Sent a messages to server!');
        
        
        
    }
    
    
    
     
    

    

    render() {
        return (
            
            <form>
            <div>
                <form onSubmit={this.handleSubmit}>
                    <div>
                        
                        <ul id="messages"></ul>
                        <label>Username</label>
                     <input  type = "text"
                                id= "ur"
                             value= {this.state.username}
                                onChange= {this.handleUsernameChange}
                        />
                    </div>
                    <div>
                     <label>My Order: </label>
                        <textarea   id= "msg"
                        value= {this.state.message} 
                                    onChange= {this.handleMessageChange} 
                        />
                    </div>
                <input type="submit" value="Submit" />
            </form>
            </div>
            </form>
        );
    }
}
