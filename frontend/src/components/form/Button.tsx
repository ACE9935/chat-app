import type { OverridableComponent } from "@mui/material/OverridableComponent";
import type { SvgIconTypeMap } from "@mui/material/SvgIcon";
import React, { useState } from "react";
import type { ButtonHTMLAttributes } from "react";

type ButtonProps = {
  children: React.ReactNode;
  variant?: "main" | "secondary";
  Icon?: OverridableComponent<SvgIconTypeMap<{}, "svg">> & { muiName: string };
} & ButtonHTMLAttributes<HTMLButtonElement>;

function Button({ children, Icon, variant = "main", ...props }: ButtonProps) {
  const [hovered, setHovered] = useState(false);

  return (
    <button
      type="submit"
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      {...props}
      className={`${variant === "main" ? "bg-main-black text-white" : "bg-main-yellow text-white border-2 border-black hover:bg-amber-600 !py-1 h-fit"} w-full flex gap-2 items-center justify-center cursor-pointer font-extrabold p-2 transition ${
        hovered&& variant === "main" ? "box-shadow-effect" : ""
      }`}
    >
      {children}
      {Icon && <Icon className="inline-block mr-2" />}
    </button>
  );
}

export default Button;
