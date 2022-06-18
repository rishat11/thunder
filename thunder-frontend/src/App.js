import React, {Component} from "react";
import Modal from "./components/Modal";
import axios from "axios";


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
        axios.post("/api/likes/", {
            user: this.state.currentUser,
            like: true,
        }).then((res) => this.setState({currentUser: res.data}));
    };

    handleDislike = () => {
        axios.post("/api/likes/", {
            user: this.state.currentUser,
            like: false,
        }).then((res) => this.setState({currentUser: res.data}));
    };

    renderUser = () => {
        const user = this.state.currentUser;
        console.log(user)
        if (user) {
            return (
                <div>{user.name}</div>
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
                    <div className="text-center">
                        <button
                            className="btn btn-primary"
                            onClick={this.handleLike}
                        >
                            Like
                        </button>
                        <button
                            className="btn btn-primary"
                            onClick={this.handleDislike}
                        >
                            Dislike
                        </button>
                    </div>
                </div>
            </main>
        );
    }
}

export default App;
