import React, { useState } from "react";

interface OptionsTextBoxProps {
  options: string[];
  onSelect: (color: string) => void;
}

const OptionsTextBox: React.FC<OptionsTextBoxProps> = ({
  options,
  onSelect,
}) => {
  const [selectedOption, setSelectedOption] = useState("");

  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedOption(event.target.value);
    onSelect(event.target.value); // Notify the parent component about the selected color
  };

  return (
    <div>
      <h1>Resolution</h1>
      <label htmlFor="options-select">Select an option:</label>
      <select
        id="options-select"
        value={selectedOption}
        onChange={handleChange}
      >
        <option value="">Choose an option</option>
        {options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
      {selectedOption && <p>You selected: {selectedOption}</p>}
    </div>
  );
};

export default OptionsTextBox;
