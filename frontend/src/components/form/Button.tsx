import React, { useState } from "react";

function Button({ children }: { children: React.ReactNode }) {
  const [hovered, setHovered] = useState(false);

  return (
    <button
      type="submit"
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      className={`w-full bg-main-black cursor-pointer font-extrabold text-white py-2 animation-transition ${
        hovered ? "box-shadow-effect" : ""
      }`}
    >
      {children}
    </button>
  );
}

export default Button;
