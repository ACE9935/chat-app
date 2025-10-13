import { Chat, Login } from "@mui/icons-material"
import { useNavigate } from "react-router-dom"


function HomePage(){

 const navigate=useNavigate()

 return (
  <div className="flex items-center justify-center p-4 min-h-screen bg-blend-multiply bg-main-yellow/80 bg-contain" style={{ backgroundImage: "url('/pattern.jpg')" }}>
   <div className="flex gap-4">
    <div onClick={()=>navigate("/chat")} className="border-box p-6 aspect-[1] w-[20rem] bg-white cursor-pointer hover:-translate-y-3 transition-all"><div className="flex w-full flex-col gap-3 items-center justify-center"><Chat className="!text-7xl"/><h2 className="font-extrabold hover:underline text-center text-5xl">Start a Chat</h2></div></div> 
    <div onClick={()=>navigate("/auth")} className="border-box p-6 aspect-[1] w-[20rem] bg-main-yellow cursor-pointer hover:-translate-y-3 transition-all"><div className="flex w-full flex-col gap-3 items-center justify-center text-white"><Login className="!text-7xl"/><h2 className="font-extrabold hover:underline text-center text-5xl">Login & Signup</h2></div></div>
   </div>
  </div>)
}

export default HomePage