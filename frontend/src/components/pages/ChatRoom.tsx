import React, { useEffect, useState, useRef } from "react";
import { useParams } from "react-router-dom";
import { useUser } from "../context/UserContext";
import { roomService } from "../../services/roomService";
import { ChatSocketService } from "../../services/chatSocketService";
import BasicInput from "../form/BasicInput";
import Button from "../form/Button";
import { Send } from "@mui/icons-material";
import type { UserType } from "../../types/UserType";
import Message from "../form/Message";
import type { MessageType } from "../../types/MessageType";

const ChatRoom: React.FC = () => {
  const { roomId } = useParams<{ roomId: string }>();
  const { user } = useUser();
  const [otherUser, setOtherUser] = useState<UserType | null>(null);
  const [messages, setMessages] = useState<MessageType[]>([]);
  const [inputText, setInputText] = useState("");
  const socketRef = useRef<ChatSocketService | null>(null);

  useEffect(() => {
    if (!roomId) return;

    const fetchMessages = async () => {
      try {
        const data = await roomService.getMessages(roomId);
        setMessages(data);
      } catch (err) {
        console.error("Error fetching messages:", err);
      }
    };
    fetchMessages();

    // Setup WebSocket
    socketRef.current = new ChatSocketService(roomId, (msg) => {
      setMessages((prev) => [...prev, msg]);
    });
    socketRef.current.connect();

    return () => {
      socketRef.current?.disconnect();
    };
  }, [roomId]);

  useEffect(() => {
    const fetchOtherUser = async () => {
      if (!roomId) return;
      try {
        const data: UserType[] = await roomService.getUserInRooms(roomId);
        const otherUser = data.find((userx: UserType) => userx.id !== user?.user_id)!;
        setOtherUser(otherUser);
      } catch (err) {
        console.error("Error fetching other user:", err);
      }
    };
    fetchOtherUser();
  }, [roomId]);

  const handleSend = (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputText.trim() || !user) return;
    socketRef.current?.sendMessage(user.user_id, inputText.trim());
    setInputText("");
  };

  return (
    <div className="flex items-center justify-center p-4 min-h-screen bg-blend-multiply bg-main-yellow/80 bg-contain" style={{ backgroundImage: "url('/pattern.jpg')" }}>
     <div className="flex flex-col gap-4 border-box bg-main-yellow p-6 w-full max-w-[35rem]">
      <h2 className="text-3xl font-extrabold"><div className="text-5xl pb-1">Chat Room:</div> <div className="text-white">{roomId}</div></h2>
      <div className="border-box bg-white overflow-auto p-2 flex flex-col gap-2 h-[25rem]">
        {messages.map((msg) => (
          <Message key={msg.id} msg={msg} senderUser={otherUser?.id === msg.user_id ? otherUser:undefined} />
        ))}
      </div>
      <form onSubmit={handleSend} className="flex gap-2">
        
        <BasicInput
          type="text"
          label=""
          variant="secondary"
          className="grow"
          value={inputText}
          setValue={setInputText}
          placeholder="Type a message..."
        />
        <Button
          style={{ width: "fit-content" }}
          type="submit"
          Icon={Send}
        >
          Send
        </Button>
       </form>
      </div>
    </div>
  );
};

export default ChatRoom;
