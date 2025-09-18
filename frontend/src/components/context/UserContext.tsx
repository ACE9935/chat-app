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
}

// Create the context
const UserContext = createContext<UserContextType | undefined>(undefined);

// Provider component
export const UserProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<UserInfos | null>(null);

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (token) {
      try {
        const decoded: UserInfos = jwtDecode(token);
        setUser(decoded);
      } catch (error) {
        console.error("Invalid token", error);
        localStorage.removeItem("access_token");
      }
    }
  }, []);

  const signOut = () => {
    localStorage.removeItem("access_token");
    setUser(null);
  };

  return (
    <UserContext.Provider value={{ user, signOut, setUser }}>
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
