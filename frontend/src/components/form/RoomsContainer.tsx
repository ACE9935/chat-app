import type { RoomType } from "../../types/RoomType";
import { useState, useEffect } from "react";
import { useUser } from "../context/UserContext";
import { roomService } from "../../services/roomService";
import RoomTab from "./RoomTab";
import Loader from "../utility/Loader";

function RoomsContainer() {
    const [rooms, setRooms] = useState<RoomType[]>([]);
    const [roomsLoading, setRoomsLoading] = useState(true);
    const {user} = useUser();
    
    useEffect(() => {
        const fetchRooms = async () => {
        try {
            setRoomsLoading(true);
            if (!user) {
                return;
            }
            const data = await roomService.getUserRooms(user.user_id);
            setRooms(data);
            } catch (error) {
                console.error('Error fetching rooms:', error);
            }
            finally {
                setRoomsLoading(false);
            }
        };
        
        fetchRooms();
    }, [user]);

    return ( 
        <div className="flex flex-col border-box bg-main-yellow">
            <div className="text-3xl text-center text-main-black font-extrabold py-3">Your Rooms</div>
            {roomsLoading ? <Loader /> : rooms.length === 0 ? <div className="text-center text-2xl py-6">No rooms found</div> : rooms.map((room) => ( <RoomTab key={room.id} roomId={room.id} handler={() => {}} /> ))}
        </div>
     );
}

export default RoomsContainer;