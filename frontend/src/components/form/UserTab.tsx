import type { UserType } from "../../types/UserType";
import { roomService } from "../../services/roomService";
import { useUser } from "../context/UserContext";
import { useNavigate } from "react-router-dom";
import Button from "./Button";

function UserTab({user,handler}:{user:UserType, handler?:() => void}) {
    const {user: loggedInUser} = useUser();
    const navigate = useNavigate();

    const handleJoinRoom = async (otherUserId: string) => {
      if (!loggedInUser) {
        return;
      }
        try {
            const room = await roomService.createRoom({user_ids: [loggedInUser.user_id, otherUserId]});
            handler && handler();
            navigate('/chat/'+room.id);
        } catch (error) {
            console.error('Error joining room:', error);
        }
    };

    return ( 
        <div key={user.id} className="flex justify-between gap-4">
                <img src="/user.png" alt="avatar" className="w-10 h-10 rounded-full" />
                <div className='grow'>
                 <div className='font-bold'>{user.username}</div>
                 <div className='text-sm text-slate-700'>{user.email}</div>
                </div>
                <Button variant='secondary' onClick={() => handleJoinRoom(user.id)} style={{width: "fit-content"}}>JOIN</Button>
              </div>
     );
}

export default UserTab;