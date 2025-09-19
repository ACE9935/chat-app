import type { OverridableComponent } from "@mui/material/OverridableComponent";
import type { SvgIconTypeMap } from "@mui/material/SvgIcon";
import React, { useState } from "react";

type ButtonProps = {
  children: React.ReactNode;
  Icon?: OverridableComponent<SvgIconTypeMap<{}, "svg">> & { muiName: string };
};

function Button({ children, Icon }: ButtonProps) {
  const [hovered, setHovered] = useState(false);

  return (
    <button
      type="submit"
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      className={`w-full bg-main-black cursor-pointer font-extrabold text-white py-2 transition ${
        hovered ? "box-shadow-effect" : ""
      }`}
    >
      {Icon && <Icon className="inline-block mr-2" />}
      {children}
    </button>
  );
}

export default Button;
