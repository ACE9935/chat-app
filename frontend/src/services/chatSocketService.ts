export class ChatSocketService {
  private socket: WebSocket | null = null;

  constructor(private roomId: string, private onMessage: (msg: any) => void) {}

  connect() {
    this.socket = new WebSocket(`ws://localhost:8000/ws/private/${this.roomId}`);

    this.socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      this.onMessage(data);
    };
  }

  sendMessage(userId: string, text: string) {
    if (this.socket?.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify({ user_id: userId, text }));
    }
  }

  disconnect() {
    this.socket?.close();
  }
}
