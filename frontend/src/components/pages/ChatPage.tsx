import { useUser } from "../context/UserContext";

function ChatPage() {
    const { user } = useUser();
    return ( 
        <div>
            <h1>Chat</h1>
            <h2>{user?.username}</h2>
        </div>
     );
}

export default ChatPage;