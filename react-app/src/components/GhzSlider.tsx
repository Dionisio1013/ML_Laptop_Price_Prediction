import React, { useState } from "react";

interface GhzSliderProps {
  onChange: (ghz: number) => void;
  value: number;
}

const GhzSlider: React.FC<GhzSliderProps> = ({ onChange, value }) => {
  const minGhz = 0.9;
  const maxGhz = 4.0;
  const step = 0.1;

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const newValue = parseFloat(event.target.value);
    onChange(newValue);
  };

  return (
    <div>
      <label htmlFor="ghzSlider">GHz: {value}</label>
      <input
        type="range"
        id="ghzSlider"
        min={minGhz}
        max={maxGhz}
        step={step}
        value={value}
        onChange={handleChange}
      />
    </div>
  );
};

export default GhzSlider;
