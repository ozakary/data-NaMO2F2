# Powder X-Ray Diffraction Data for NaMO<sub>2</sub>F<sub>2</sub> (M = Nb<sup>5+</sup>, Ta<sup>5+</sup>)

**Author:** Ouail Zakary  
**ORCID:** [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
**E-mail:** [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
**Website:** [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)

This repository contains datasets of **Powder X-Ray Diffraction (PXRD)** data for the compounds NaNbO<sub>2</sub>F<sub>2</sub> and NaTaO<sub>2</sub>F<sub>2</sub>, recorded under both room temperature (RT) and variable temperature conditions.

## Overview of the Data

The dataset is organized into two main families of experiments:

1. **Room Temperature PXRD Data:**  
   **Folder:** `./room_temperature_experiments`
   - **NaNbO<sub>2</sub>F<sub>2</sub> Data:**  
     - [Raw Data](./room_temperature_experiments/NaNbO2F2/raw_data/)
     - [Rietveld Refinement Data](./room_temperature_experiments/NaNbO2F2/Rietveld_refinement/)
   - **NaTaO<sub>2</sub>F<sub>2</sub> Data:**  
     - [Raw Data](./room_temperature_experiments/NaTaO2F2/raw_data/)
     - [Rietveld Refinement Data](./room_temperature_experiments/NaTaO2F2/Rietveld_refinement/)

2. **Variable Temperature PXRD Data:**  
   **Folder:** `./variable-temperature_experiments`
   - **NaNbO<sub>2</sub>F<sub>2</sub> Data:**  
     - [Raw Data](./variable-temperature_experiments/NaNbO2F2/raw_data/)
     - [Rietveld Refinement Data](./variable-temperature_experiments/NaNbO2F2/Rietveld_refinement/)
   - **NaTaO<sub>2</sub>F<sub>2</sub> Data:**  
     - [Raw Data](./variable-temperature_experiments/NaTaO2F2/raw_data/)
     - [Rietveld Refinement Data](./variable-temperature_experiments/NaTaO2F2/Rietveld_refinement/)

## Methods

### PXRD Data Collection

Both RT and temperature-controlled PXRD patterns were recorded using a **PANalytical θ/θ Bragg–Brentano EMPYREAN** diffractometer (CuKα<sub>1+2</sub> radiations) equipped with a **PIXcel1D detector**. The collection methods are as follows:

- **Room Temperature PXRD Patterns:**  
  - **2θ Range:** 5° to 135°  
  - **Step Size:** 0.0131°  
  - **Total Acquisition Time:** Approximately 7h 30m  
  - **Sample Preparation:** Raw powders were dusted through a 63 μm sieve on a glass holder to minimize preferential grain orientation.

- **Temperature-Controlled PXRD Patterns:**  
  - **Temperature Range:** RT to 300°C using a **HTK 900 Anton Paar furnace attachment**  
  - **Sample Holder:** Glass ceramic Macor  
  - **Data Collection Intervals:** 20°C (25–220°C) and 10°C (220–300°C) increments with a heating rate of 5°C/min  
  - **Temperature Stabilization:** 20 minutes before each measurement  
  - **2θ Range:** 10° to 100°  
  - **Step Size:** 0.0131°  
  - **Total Acquisition Time:** 3 hours for each pattern.

### Rietveld Refinement

The **Rietveld refinement method** was employed for both the RT and temperature-controlled PXRD data using the **FullProf** software.

## Directory Structure

The following directories contain the datasets:

- **Room Temperature PXRD Data:**
  - [NaNbO<sub>2</sub>F<sub>2</sub> Raw Data](./room_temperature_experiments/NaNbO2F2/raw_data/)
  - [NaNbO<sub>2</sub>F<sub>2</sub> Rietveld Refinement Data](./room_temperature_experiments/NaNbO2F2/Rietveld_refinement/)
  - [NaTaO<sub>2</sub>F<sub>2</sub> Raw Data](./room_temperature_experiments/NaTaO2F2/raw_data/)
  - [NaTaO<sub>2</sub>F<sub>2</sub> Rietveld Refinement Data](./room_temperature_experiments/NaTaO2F2/Rietveld_refinement/)

- **Variable Temperature PXRD Data:**
  - [NaNbO<sub>2</sub>F<sub>2</sub> Raw Data](./variable-temperature_experiments/NaNbO2F2/raw_data/)
  - [NaNbO<sub>2</sub>F<sub>2</sub> Rietveld Refinement Data](./variable-temperature_experiments/NaNbO2F2/Rietveld_refinement/)
  - [NaTaO<sub>2</sub>F<sub>2</sub> Raw Data](./variable-temperature_experiments/NaTaO2F2/raw_data/)
  - [NaTaO<sub>2</sub>F<sub>2</sub> Rietveld Refinement Data](./variable-temperature_experiments/NaTaO2F2/Rietveld_refinement/)

## Requirements

To successfully conduct the PXRD experiments and perform the Rietveld refinements, the following requirements must be met:

- **Equipment:**  
  - A **PANalytical θ/θ Bragg–Brentano EMPYREAN** diffractometer with a **PIXcel1D detector**.
  - An **HTK 900 Anton Paar furnace attachment** for temperature-controlled experiments.

- **Software:**  
  - **FullProf** for Rietveld refinements. You can download this software from the [FullProf Suite](https://www.ill.eu/sites/fullprof/php/downloads.html).
  - **VESTA** (download: [VESTA](https://jp-minerals.org/vesta/en/download.html)) and **Diamond** (download: [Diamond](https://www.crystalimpact.com/diamond/download.htm)) for 3D visualization of crystal structures and for computing structural features such as bond lengths, distances, angles, volume of the unit cell, quadratic elongation, and distortion index.

---

For further details, please refer to the respective folders or contact the author via the provided email.
