import { useEffect } from "react";
import { roomService } from "../../services/roomService";
import { useUser } from "../context/UserContext";
import { useState } from "react";
import type { UserType } from "../../types/UserType";
import { useNavigate } from "react-router-dom";
import type { MessageType } from "../../types/MessageType";
import { formatDate } from "../../utility/formatDate";

function RoomTab({roomId, handler}:{roomId:string, handler?:() => void}) {
    const {user: loggedInUser} = useUser();
    const [user, setUser] = useState<UserType>({} as UserType);
    const [roomMessages, setRoomMessages] = useState<MessageType[]>([]);
    const navigate = useNavigate();
    const [isNewRoom, setIsNewRoom] = useState(false);
    const [isLastMessageAuthor, setIsLastMessageAuthor] = useState(false);

    useEffect(() => {
     const fetchRoomData = async () => {
      if (!loggedInUser) {
        return;
      }
        try {
            const room_users: UserType[] = await roomService.getUserInRooms(roomId);
            const room_messages = await roomService.getMessages(roomId);
            setIsNewRoom(room_messages.length === 0);
            setRoomMessages(room_messages);
            const otherUser = room_users.find((user: UserType) => user.id !== loggedInUser.user_id)!;
            setUser(otherUser);
            handler && handler();
        } catch (error) {
            console.error('Error joining room:', error);
        }
     };
     fetchRoomData();
    }, []);

    useEffect(() => {
        if (roomMessages.length > 0) {
            const lastMessage = roomMessages[roomMessages.length - 1];
            setIsLastMessageAuthor(lastMessage.user_id === loggedInUser?.user_id);
        }
    }, [roomMessages]);

    return ( 
        <div onClick={() => navigate('/chat/'+roomId)} className="flex justify-between gap-4 hover:bg-amber-600 cursor-pointer p-3 border-b">
                <img src="/user.png" alt="avatar" className="w-10 h-10 rounded-full" />
                <div className='grow'>
                 <div className="flex justify-between"><div className='font-bold'>{user.username}</div><div>{formatDate(roomMessages[roomMessages.length - 1]?.created_at)}</div></div>
                 {isNewRoom ? <div className='text-xs text-white bg-green-600 w-fit p-1 font-bold rounded'>New room</div> : <div className='text-sm text-slate-700'>{isLastMessageAuthor ? "You: " : ""}{roomMessages[roomMessages.length - 1]?.text}</div>}
                </div>
        </div>
     );
}

export default RoomTab;