import React from "react";

type BasicInputProps = {
  label: string;
  value: string;
  setValue: React.Dispatch<React.SetStateAction<string>>;
  type?: string;
};

function BasicInput({ label, value, setValue, type = "text" }: BasicInputProps) {
  return (
    <div>
      <label className="block mb-1 font-bold">{label}</label>
      <input
        type={type}
        value={value}
        onChange={(e) => setValue(e.target.value)}
        required
        className="w-full border-box px-3 py-2 outline-0 font-medium focus:bg-white"
      />
    </div>
  );
}

export default BasicInput;
