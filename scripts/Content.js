    
import * as React from 'react';
import { Socket } from './Socket';
import { Button } from './Button';
import { Chat } from './Chat';



export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'messages': []
        };
    }
    
    componentDidMount() {
        Socket.on('message received', (data) => {
            this.setState({
                'message_received': data['Message']
            });
        });
    }
   

    render() {
        //let my_message = this.state.message_received;
        return (
            
            <body>
                <div>
                    <h1> Truck Dash </h1>
                    <h2> Food Truck Menu </h2>
                    <ul>
                        <li>Fries</li>
                        <li>Cheese Burger</li>
                        <li>Hot Dog</li>
                    </ul>
                    
                   
                    <Chat />
                   
                </div>
            </body>
        );
    }
}

//     render() {
//         return (
//             <div>
//                 <h1>Hello from React! testing</h1>
//                 <div>
//                     Data: {this.state.data}
//                 </div>
//             </div>
//         );
//     }
// }
