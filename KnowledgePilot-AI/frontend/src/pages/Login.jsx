import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import api from "../api/api";

function Login() {

  const navigate = useNavigate();

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const login = async () => {

    try {

      const response = await api.post(
        "/auth/login",
        {
          email,
          password
        }
      );

      localStorage.setItem(
        "token",
        response.data.access_token
      );

      navigate("/dashboard");

    }

    catch (err) {

    console.log("================");

    console.log(err);

    console.log(err.response);

    console.log(err.response?.status);

    console.log(err.response?.data);

    console.log("================");

    }

  };

  return (

    <div style={{padding:"40px"}}>

      <h1>KnowledgePilot AI</h1>

      <input
        placeholder="Email"
        onChange={(e)=>setEmail(e.target.value)}
      />

      <br/><br/>

      <input
        type="password"
        placeholder="Password"
        onChange={(e)=>setPassword(e.target.value)}
      />

      <br/><br/>

      <button onClick={login}>
        Login
      </button>

      <br/><br/>

      <Link to="/signup">
        Create Account
      </Link>

    </div>

  );

}

export default Login;