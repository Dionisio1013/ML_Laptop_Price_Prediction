import React, { useState } from "react";
import axios from "axios";
import "./App.css";

import ListGroup from "./components/ListGroup";
import SSDGroup from "./components/SSDGroup";
import RamGroup from "./components/RamGroup";
import OptionsTextBox from "./components/OptionsTextBox";
import GhzSlider from "./components/GhzSlider";

function App() {
  const cities = ["Low", "Fair", "High", "Very High"];
  const SSDs = ["64 GB", "128 GB", "256 GB", "512 GB", "1 TB", "2 TB", "4 TB"];
  const Rams = [
    "4 GB",
    "8 GB",
    "12 GB",
    "16 GB",
    "20 GB",
    "24 GB",
    "32 GB",
    "40 GB",
    "64 GB",
    "128 GB",
  ];
  const colors = [
    "1366x768",
    "1536x1024",
    "1600x900",
    "1920x1028",
    "1920x1080",
    "1920x1200",
    "1920x1280",
    "2220x1080",
    "2240x1400",
    "2256x1504",
    "2260x1400",
    "2400x1600",
    "2496x1664",
    "2560x1440",
    "2560x1600",
    "2736x1824",
    "2800x1620",
    "2880x1620",
    "2880x1800",
    "2880x1920",
    "3000x2000",
    "3072x1920",
    "3200x2000",
    "3240x2160",
    "3300x2200",
    "3840x2160",
  ];

  const [selectedGhz, setSelectedGhz] = useState(2.0);
  const [selectedCity, setSelectedCity] = useState("");
  const [selectedColor, setSelectedColor] = useState("");
  const [showPrediction, setShowPrediction] = useState(false);
  const [selectedSSD, setSelectedSSD] = useState("");
  const [selectedRam, setSelectedRam] = useState("");
  const [userInteracted, setUserInteracted] = useState(false);
  const [predictionResult, setPredictionResult] = useState("");

  const handleGhzChange = (ghz: GLfloat) => {
    setSelectedGhz(ghz);
  };

  const handleUserInteraction = () => {
    setUserInteracted(true);
  };

  const handleSelectItem = (item: string) => {
    setSelectedCity(item);
  };

  const handleColorSelect = (color: string) => {
    setSelectedColor(color);
  };

  const handleSSDSelect = (SSD: Int16Array) => {
    setSelectedSSD(SSD);
  };

  const handleRamSelect = (Ram: Int16Array) => {
    setSelectedRam(Ram);
  };

  const handlePredict = () => {
    const data = {
      Ram: parseInt(removeUnitSuffix(selectedRam)),
      Ssd: parseInt(removeUnitSuffix(selectedSSD)),
      Ghz: selectedGhz,
      Graphics: selectedCity,
      Resolution: selectedColor,
    };

    axios
      .post("http://localhost:8080/predictdata", data)
      .then((response) => {
        setShowPrediction(true);
        const roundedResult = parseFloat(response.data.prediction).toFixed(2);
        setPredictionResult(roundedResult);
      })
      .catch((error) => {
        console.error("Error fetching prediction:", error);
      });
  };

  const removeUnitSuffix = (value) => {
    value = value.trim();
    if (value.endsWith("TB")) {
      const gbValue = parseFloat(value) * 1000;
      return gbValue;
    } else if (value.endsWith("GB")) {
      return parseFloat(value);
    } else {
      return value;
    }
  };

  return (
    <div className="container">
      <h1 className="title">Laptop Price Predictor</h1>
      <div className="flex-container">
        <div
          className={`options-container ${
            selectedCity ? "pane-contract" : "pane-expand"
          }`}
        >
          <OptionsTextBox options={colors} onSelect={handleColorSelect} />
          <GhzSlider value={selectedGhz} onChange={handleGhzChange} />
        </div>

        <div
          className={`options-container ${
            selectedCity ? "pane-expand" : "pane-contract"
          }`}
        >
          <ListGroup
            items={cities}
            heading="Graphics Quality"
            onSelectItem={handleSelectItem}
          />
          {selectedCity && <p>Selected Graphics Quality: {selectedCity}</p>}
        </div>

        <div
          className={`options-container ${
            selectedCity ? "pane-expand" : "pane-contract"
          }`}
        >
          <SSDGroup items={SSDs} heading="SSD" onSelectItem={handleSSDSelect} />
          {selectedSSD && <p>Selected SSD: {selectedSSD}</p>}
        </div>

        <div
          className={`options-container ${
            selectedCity ? "pane-expand" : "pane-contract"
          }`}
        >
          <RamGroup items={Rams} heading="Ram" onSelectItem={handleRamSelect} />
          {selectedRam && <p>Selected Ram: {selectedRam}</p>}
        </div>

        <div className="options-container">
          <button className="predict-button" onClick={handlePredict}>
            Predict
          </button>
          {showPrediction && <p>Prediction Result: ${predictionResult}</p>}
        </div>
      </div>
    </div>
  );
}

export default App;
