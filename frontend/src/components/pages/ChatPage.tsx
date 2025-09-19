import { useUser } from "../context/UserContext";
import Button from "../form/Button";
import { Add } from "@mui/icons-material";

function ChatPage() {
    const { user } = useUser();
    return ( 
        <div className="flex items-center justify-center min-h-screen bg-blend-multiply bg-main-yellow/80 bg-contain" style={{ backgroundImage: "url('pattern.jpg')" }}>
            <div className="flex flex-col gap-6">
             <div className="text-6xl text-center text-main-black font-extrabold">
                Welcome <span className="text-white">{user?.username}</span>
             </div>
             <div>
                <Button Icon={Add}>NEW CHAT</Button>
             </div>
            </div>
        </div>
     );
}

export default ChatPage;