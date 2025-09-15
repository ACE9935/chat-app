// ChatApp.tsx
import React, { useState, useRef } from "react";

const ChatApp: React.FC = () => {
  const [username, setUsername] = useState("");
  const [connected, setConnected] = useState(false);
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState<string[]>([]);
  const ws = useRef<WebSocket | null>(null);

  const connectWebSocket = () => {
    if (!username) return;
    ws.current = new WebSocket(`ws://localhost:8000/ws/${username}`);

    ws.current.onopen = () => {
      setConnected(true);
      console.log("Connected to WebSocket");
    };

    ws.current.onmessage = (event) => {
      setMessages((prev) => [...prev, event.data]);
    };

    ws.current.onclose = () => {
      setConnected(false);
      console.log("Disconnected from WebSocket");
    };
  };

  const sendMessage = () => {
    if (ws.current && message.trim()) {
      ws.current.send(message);
      setMessage("");
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-4 border rounded shadow">
      {!connected ? (
        <div className="flex flex-col gap-2">
          <input
            type="text"
            placeholder="Enter your username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="p-2 border rounded"
          />
          <button
            onClick={connectWebSocket}
            className="bg-blue-500 text-white p-2 rounded"
          >
            Join Chat
          </button>
        </div>
      ) : (
        <div className="flex flex-col gap-2">
          <div className="h-64 overflow-y-auto border p-2 rounded bg-gray-50">
            {messages.map((msg, idx) => (
              <div key={idx} className="mb-1">
                {msg}
              </div>
            ))}
          </div>
          <div className="flex gap-2">
            <input
              type="text"
              placeholder="Type a message..."
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyPress={handleKeyPress}
              className="flex-1 p-2 border rounded"
            />
            <button
              onClick={sendMessage}
              className="bg-green-500 text-white p-2 rounded"
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatApp;
