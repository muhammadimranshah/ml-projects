import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import ChatBox from "../components/ChatBox";

import "../styles/dashboard.css";

function Dashboard(){

    return(

        <div className="dashboard">

            <Navbar/>

            <div className="main">

                <Sidebar/>

                <ChatBox/>

            </div>

        </div>

    );

}

export default Dashboard;