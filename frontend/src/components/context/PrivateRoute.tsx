import React, { useEffect } from "react";
import { useUser } from "./UserContext";
import { useNavigate } from "react-router-dom";

// Provider component
export const PrivateRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { user, userStatus } = useUser();
  const navigate = useNavigate();

  useEffect(() => {
    console.log(user, userStatus);
    if (!user && userStatus=="error") {
      navigate('/auth');
    }
  }, [userStatus, navigate, user]);

  return <>{children}</>;
};

