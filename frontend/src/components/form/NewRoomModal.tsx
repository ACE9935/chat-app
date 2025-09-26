import Modal from '@mui/material/Modal';
import { useState, useEffect } from "react";
import { useUser } from '../context/UserContext';
import BasicInput from './BasicInput';
import { userService } from '../../services/userService';
import type { UserType } from '../../types/UserType';
import { Search } from '@mui/icons-material';
import UserTab from './UserTab';

function NewRoomModal({open, handleClose}: {open: boolean, handleClose: () => void}) {
    const [users, setUsers] = useState<UserType[]>([]);
    const [searchTerm, setSearchTerm] = useState('');
    const {user} = useUser();

    useEffect(() => {
        const fetchUsers = async () => {
          try {
            const data = await userService.searchUsers(searchTerm);
            setUsers(data);
          } catch (error) {
            console.error('Error fetching users:', error);
          }
        };
    
        fetchUsers();
    }, [searchTerm]);

    return ( 
        <Modal
         open={open}
         onClose={handleClose}
         className='grid place-items-center'
         aria-labelledby="New room modal"
         aria-describedby="Join a user and chat with them"
        >
         <div className="bg-white border-box p-6 w-full max-w-[30rem] flex gap-5 flex-col">
          <p id="New room modal" className='text-3xl font-extrabold text-center'>Join a user and chat with them</p>
          <BasicInput label={<><Search/> Username</>} variant='secondary' type="text" value={searchTerm} setValue={setSearchTerm} />
          <div className="flex flex-col gap-2 h-full max-h-[30rem] overflow-auto">
            <div className='font-bold pb-3'>Users - {users.length-1}</div>
            {users
              .filter((userx) => userx.id !== user?.user_id)
              .map((userx) => (
               <UserTab key={userx.id} user={userx} handler={handleClose} />
            ))}
          </div>
         </div>
        </Modal>
     );
}

export default NewRoomModal;