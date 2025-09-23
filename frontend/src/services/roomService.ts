import api from "../api";

interface CreateRoomPayload {
  room_id?: string;
  user_ids: string[];
}

interface MessagePayload {
  text: string;
}

export const roomService = {
  getRoom: async (roomId: string) => {
    const res = await api.get(`/rooms/${roomId}`);
    return res.data;
  },

  createRoom: async (payload: CreateRoomPayload) => {
    const res = await api.post("/rooms/", payload);
    return res.data;
  },

  postMessage: async (roomId: string, payload: MessagePayload) => {
    const res = await api.post(`/rooms/${roomId}/messages`, payload);
    return res.data;
  },

  getMessages: async (roomId: string) => {
    const res = await api.get(`/rooms/room/${roomId}`);
    return res.data;
  },

  getUserRooms: async (userId: string) => {
    const res = await api.get(`rooms/${userId}/rooms`);
    return res.data;
  },
    getUserInRooms: async (roomId: string) => {
    const res = await api.get(`rooms/${roomId}/users`);
    return res.data;
  },
};
