import React, {Component} from "react";
import Modal from "./components/Modal";
import axios from "axios";
import "./App.css";
import {Navigate} from 'react-router';


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            currentUser: null,
        }
    }

    componentDidMount() {
        this.refreshUser();
    }

    refreshUser = () => {
        axios.get(`/api/user_profile/`).then(
            (res) => {
                this.setState({currentUser: res.data});
            });
    }

    handleLike = () => {
        axios.post("/api/like/", {
            user: this.state.currentUser.user,
            like: true,
        }).then((res) => this.setState({currentUser: res.data})
        ).catch((res) => <Navigate to='/login' push={true}/>);
    };

    handleDislike = () => {
        axios.post("/api/like/", {
            user: this.state.currentUser,
            like: false,
        }).then((res) => this.setState({currentUser: res.data}));
    };

    renderUser = () => {
        const user = this.state.currentUser;
        if (user) {
            return (
                <div>
                    <div>{user.name}</div>
                    <img src={user.photos[0].photo} alt="Ошибка при загрузке изображения"/>
                </div>
            )
        } else {
            return null;
        }
    };

    render() {
        return (
            <main className="container">
                <h1 className="text-dark text-center my-4">Nastusa</h1>
                <div className="d-flex flex-column">
                    <div className="text-center">
                        {this.renderUser()}
                    </div>
                    <div className="text-center" style={{'fontSize': '60px', cursor: 'pointer', 'userSelect': 'none'}}>
                        <i onClick={this.handleLike} className="fa fa-thumbs-up flex-fill"/>
                        <i onClick={this.handleDislike} className="fa fa-thumbs-down flex-fill"/>
                    </div>
                </div>
            </main>
        );
    }
}

export default App;
