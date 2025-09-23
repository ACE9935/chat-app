import { jwtDecode } from "jwt-decode";
import api from "../api";
import type { UserInfos } from "../components/context/UserContext";

interface SignupData {
  email: string;
  username: string;
  password: string;
}

interface LoginData {
  email: string;
  password: string;
}

export const authService = {
  signup: async (data: SignupData) => {
    const res = await api.post("/auth/signup", data);
    if (res.data.access_token) {
      localStorage.setItem("access_token", res.data.access_token);
    }
    const user: UserInfos = jwtDecode(res.data.access_token);
    return user;
  },

  login: async (data: LoginData) => {
    const res = await api.post("/auth/login", data);
    if (res.data.access_token) {
      localStorage.setItem("access_token", res.data.access_token);
    }
    const user: UserInfos = jwtDecode(res.data.access_token);
    return user;
  },

  logout: () => {
    localStorage.removeItem("access_token");
  },
};
