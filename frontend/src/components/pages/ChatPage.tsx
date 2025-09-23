import { useUser } from "../context/UserContext";
import Button from "../form/Button";
import { Add } from "@mui/icons-material";
import { useState } from "react";
import NewRoomModal from "../form/NewRoomModal";
import RoomsContainer from "../form/RoomsContainer";
import NavBar from "../utility/NavBar";

function ChatPage() {
    const { user } = useUser();
    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    
    return ( 
        <div className="flex flex-col items-center justify-center p-4 min-h-screen bg-blend-multiply bg-main-yellow/80 bg-contain" style={{ backgroundImage: "url('pattern.jpg')" }}>
             <NavBar />
             <NewRoomModal open={open} handleClose={handleClose} />
             <div className="flex flex-col gap-6 w-full max-w-[33rem]">
              <div className="text-6xl text-center text-main-black font-extrabold">
                Welcome <span className="text-white">{user?.username}</span>
              </div>
             <div>
             </div>
             <RoomsContainer />
             <Button Icon={Add} onClick={handleOpen}>NEW CHAT</Button>
             </div>
        </div>
     );
}

export default ChatPage;