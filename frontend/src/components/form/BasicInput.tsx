import React from "react";

type BasicInputProps = {
  label: React.ReactNode;
  value: string;
  variant?: "main" | "secondary";
  setValue: React.Dispatch<React.SetStateAction<string>>;
  type?: string;
  className?: string
}& React.InputHTMLAttributes<HTMLInputElement>;

function BasicInput({ label, value, setValue, type = "text", variant="main", className, ...props }: BasicInputProps) {
  return (
    <div className={className}>
      <label className="block mb-1 font-bold">{label}</label>
      <input
        {...props}
        type={type}
        value={value}
        onChange={(e) => setValue(e.target.value)}
        required
        className={`w-full border-box px-3 py-2 outline-0 font-medium ${variant === "main" ? "focus:bg-white" : "bg-white focus:bg-amber-100"}`}
      />
    </div>
  );
}

export default BasicInput;
