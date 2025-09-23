import React, { createContext, useContext, useState, useEffect } from "react";
import { jwtDecode } from "jwt-decode";

export type UserInfos = {
  username: string;
  user_email: string;
  user_id: string;
};

interface UserContextType {
  user: UserInfos | null;
  signOut: () => void;
  setUser: React.Dispatch<React.SetStateAction<UserInfos | null>>;
  userStatus: "pending" | "success" | "error";
}

// Create the context
const UserContext = createContext<UserContextType | undefined>(undefined);

// Provider component
export const UserProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<UserInfos | null>(null);
  const [userStatus, setUserStatus] = useState<"pending" | "success" | "error">("pending");

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (token) {
      try {
        const decoded: UserInfos = jwtDecode(token);
        setUser(decoded);
        setUserStatus("success");
      } catch (error) {
        console.error("Invalid token", error);
        localStorage.removeItem("access_token");
        setUserStatus("error");
      }
    }else {
      setUserStatus("error");
    }
  }, []);

  const signOut = () => {
    localStorage.removeItem("access_token");
    setUserStatus("error");
    setUser(null);
  };

  return (
    <UserContext.Provider value={{ user, signOut, setUser, userStatus }}>
      {children}
    </UserContext.Provider>
  );
};

export const useUser = (): UserContextType => {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error("useUser must be used within a UserProvider");
  }
  return context;
};
