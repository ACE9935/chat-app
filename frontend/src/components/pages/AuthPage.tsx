import { useState } from "react";
import BasicInput from "../form/BasicInput";
import Button from "../form/Button";
import {useNavigate} from 'react-router-dom';
import { useUser} from "../context/UserContext";
import { authService } from "../../services/authService";

export default function AuthPage() {
  const [isLogin, setIsLogin] = useState(true); 
  const { setUser } = useUser();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState(""); 
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const validatePassword = (pwd: string) => {
    // at least 8 chars, at least one letter, one digit
    const regex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    return regex.test(pwd);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    let new_user = null;
    try {
      if (isLogin) {
        new_user= await authService.login({ email, password });
        setUser(new_user);
      } else {
        // --- Signup validations ---
        if (!validatePassword(password)) {
          setMessage(
            "Password must be at least 8 characters long and contain both letters and numbers."
          );
          return;
        }
        if (password !== confirmPassword) {
          setMessage("Passwords do not match.");
          return;
        }

        new_user= await authService.signup({ email, username, password });
        setUser(new_user);
      }

      if(new_user){
       console.log(new_user);
       navigate('/chat')
      }
      
      setEmail("");
      setUsername("");
      setPassword("");
      setConfirmPassword("");
    } catch (err: any) {
      console.error(err);
      setMessage(err.response?.data?.detail || "Something went wrong");
    }
  };

  return (
    <div className="flex p-6 items-center justify-center min-h-screen bg-blend-multiply bg-main-yellow/80 bg-contain" style={{ backgroundImage: "url('pattern.jpg')" }}>
      <div className="p-8 w-full bg-main-yellow max-w-md border-box">
        <h2 className="text-5xl font-extrabold mb-6 text-center">
          {isLogin ? "Login" : "Signup"}
        </h2>

        <form onSubmit={handleSubmit} className="space-y-4">
        <BasicInput label="Email" type="email" value={email} setValue={setEmail} />

          {!isLogin && (
            <>
              <BasicInput label="Username" value={username} setValue={setUsername} />
              <BasicInput label="Confirm Password" value={confirmPassword} type="password" setValue={setConfirmPassword} />
            </>
          )}
          <BasicInput label="Password" value={password} type="password" setValue={setPassword}/>

          <Button>GO</Button>
        </form>

        <p className="mt-4 text-center text-sm text-gray-600">
          {isLogin ? "Don't have an account?" : "Already have an account?"}{" "}
          <button
            onClick={() => {setMessage(""); setIsLogin(!isLogin)}}
            className="text-blue-500 font-bold cursor-pointer hover:underline"
          >
            {isLogin ? "Signup" : "Login"}
          </button>
        </p>

        {message && <p className="mt-4 text-center text-red-500 border-2 border-red-500 p-2 bg-red-200">{message}</p>}
      </div>
    </div>
  );
}
