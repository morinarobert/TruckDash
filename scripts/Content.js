    
import * as React from 'react';
import { Socket } from './Socket';
import { Button } from './Button';
import { Chat } from './Chat';



export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'numbers': []
        };
    }
    
    componentDidMount() {
        Socket.on('number received', (data) => {
            this.setState({
                'number_received': data['number']
            });
        })
    }
   

    render() {
        
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
