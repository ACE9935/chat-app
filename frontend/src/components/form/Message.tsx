import { useEffect } from "react";
import type { MessageType } from "../../types/MessageType";
import type { UserType } from "../../types/UserType";
import { useUser } from "../context/UserContext";
import { useState } from "react";
import { formatDate } from "../../utility/formatDate";

function Message({msg, senderUser}:{msg: MessageType, senderUser?: UserType}) {
    const { user } = useUser();
    const [isLoggesInUserAuthor, setIsLoggesInUserAuthor] = useState(false);

    useEffect(() => {
        setIsLoggesInUserAuthor(msg.user_id === user?.user_id);
      }, [msg, user]);

    return ( 
      <div  className={`p-2 flex gap-2 ${
              isLoggesInUserAuthor
                ? "self-end"
                : "self-start"
            }`}>
        <img src="/user.png" alt="avatar" className="w-10 h-10 rounded-full" />
        <div className="flex flex-col gap-1">
        <div className="font-bold">{senderUser? senderUser.username : user?.username}{isLoggesInUserAuthor && " (You)"}</div>
        <div
            className={`p-2 w-fit max-w-[16rem] ${
              isLoggesInUserAuthor
                ? "bg-amber-500 text-white"
                : "bg-gray-200"
            }`}
          >
            {msg.text}
            <div className="text-xs text-gray-700 mt-1 w-full flex justify-end">
              {formatDate(msg.created_at)}
            </div>
          </div>
          </div>
        </div>
     );
}

export default Message;