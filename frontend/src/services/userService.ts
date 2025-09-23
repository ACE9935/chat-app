import api from "../api";

export const userService = {
  searchUsers: async (search: string) => {
    const res = await api.get(`/users?search=${encodeURIComponent(search)}`);
    return res.data;
  },

  getUserRooms: async (userId: string) => {
    const res = await api.get(`/users/${userId}/rooms`);
    return res.data;
  },
};
