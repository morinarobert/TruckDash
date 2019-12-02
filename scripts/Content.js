 import * as React from 'react';
import { Socket } from './Socket';
import { Chat } from './Chat';



export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'messages': [], 
            'message_array': []
        };
    }
    
    componentDidMount() {
        Socket.on('message received', (data) => {
            this.setState({
                'message_received': data['Message']
            });
        
            
        });
    
        Socket.on('message array', (data) => {
            this.setState({
                'message_array': data['data']
            });
        });
        
        
    }
    

    render() {
        let my_message = this.state.message_received;
        let my_array = this.state.message_array;
        
        const listItems = this.state.message_array.map((a, index) =>
            <p className="number-item chatbubble" key={index}>{a}</p>
        );
        
        return (
            <html>
            <body>
                <div className="rcontainer">
                
                    <div className="container">
                    
                        <div className="chat-page">
                    
                        <div className="msg-inbox">
                            <div className="chats">
                                <div className="msg-page">
                                <div className="received-msg">
                                <p>"Welcome to Truck Dash! Here are some helpful tips:"</p>
                                <p>"Type: '!! Begin' to start your ordering process. If you need help at anytime type '!! help' "</p>
                                <div className="received-msg-inbox">
                                {listItems}
                                        
                                </div>
                                </div>
                                </div>
                                </div>
                        </div>
                    </div>
                </div>
                <div className="msg-bottom">
                    <div> <Chat /> </div>
                </div>
                </div>
            </body>
            </html>
        );
    }
}
