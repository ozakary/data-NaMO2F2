# Solid-State Nuclear Magnetic Resonance (ssNMR) Spectroscopy of NaMO<sub>2</sub>F<sub>2</sub> (M = Nb<sup>5+</sup>, Ta<sup>5+</sup>)
Author: Ouail Zakary  
ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
E-mail: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
Website: [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)

This folder contains the solid-state nuclear magnetic resonance (ssNMR) spectroscopy data for the compounds **NaNbO<sub>2</sub>F<sub>2</sub>** and **NaTaO<sub>2</sub>F<sub>2</sub>**, recorded for the nuclei **<sup>19</sup>F**, **<sup>23</sup>Na**, and **<sup>93</sup>Nb**.

## Overview of the Data
The dataset is divided into two main folders for **NaNbO<sub>2</sub>F<sub>2</sub>** and **NaTaO<sub>2</sub>F<sub>2</sub>**, with subfolders for each nucleus. The NMR spectra were recorded and fitted using Bruker TopSpin and DMFit software, respectively.

### Folders and Data Structure
1. **NaNbO<sub>2</sub>F<sub>2</sub>**
   - **<sup>19</sup>F Nucleus:**  
     Path: [./NaNbO2F2/19F](./NaNbO2F2/19F)  
     Fit File: [1R.fxml](./NaNbO2F2/19F/43/pdata/1/1R.fxml)
   
   - **<sup>23</sup>Na Nucleus:**  
     Path: [./NaNbO2F2/23Na](./NaNbO2F2/23Na)  
     Fit File: [1R.fxml](./NaNbO2F2/23Na/3/pdata/1/1R.fxml)
   
   - **<sup>93</sup>Nb Nucleus:**  
     Path: [./NaNbO2F2/93Nb](./NaNbO2F2/93Nb)  
     Fit File: [1R.fxml](./NaNbO2F2/93Nb/210/pdata/20/1R.fxml)

2. **NaTaO<sub>2</sub>F<sub>2</sub>**
   - **<sup>19</sup>F Nucleus:**  
     Path: [./NaTaO2F2/19F](./NaTaO2F2/19F)  
     Fit File: [1R.fxml](./NaTaO2F2/19F/1/pdata/1/1R.fxml)
   
   - **<sup>23</sup>Na Nucleus:**  
     Path: [./NaTaO2F2/23Na](./NaTaO2F2/23Na)  
     Fit File: [1R.fxml](./NaTaO2F2/23Na/1/pdata/1/1R.fxml)

### Methods
**<sup>19</sup>F (I = 1/2) MAS NMR** spectra were recorded using a Bruker Avance III spectrometer operating at 7 T (Larmor frequency of 282.4 MHz) and a 1.3 mm CP-MAS probe-head. The Hahn echo sequence was applied with an interpulse delay of one rotor period and a recycle delay of 20 s. A 90° pulse (RF field: 160 kHz, pulse duration: 1.56 μs) was used. For NaNbO<sub>2</sub>F<sub>2</sub>, SPINAL-64 decoupling of <sup>93</sup>Nb was employed during acquisition (RF field: ~106 kHz).

**<sup>23</sup>Na (I = 3/2) MAS NMR** spectra were recorded at 20 T (Larmor frequency: 224.9 MHz) with a 2.5 mm CP-MAS probe-head. The spectra were acquired using a heteronuclear <sup>23</sup>Na–<sup>19</sup>F SPINAL-64 decoupling sequence at a RF field of 132 kHz, with a 1 s recycle delay and a small pulse flip angle of 10° (pulse duration: 0.35 μs).

**<sup>93</sup>Nb (I = 9/2) MAS NMR** spectra were recorded using a 1.3 mm CP-MAS probe-head at 20 T (Larmor frequency: 208.1 MHz). The Hahn echo sequence was applied with a 1 s recycle delay, using a CT 90° selective pulse (RF field: 125 kHz, pulse duration: 2 μs).

**References:**  
- **<sup>19</sup>F** spectra were referenced to CFCl<sub>3</sub>.  
- **<sup>23</sup>Na** spectra were referenced to a 1 M NaCl aqueous solution.  
- **<sup>93</sup>Nb** spectra were referenced to a saturated K[NbCl<sub>6</sub>]/CH<sub>3</sub>CN solution.

### Data Analysis
The raw ssNMR data was processed using **Bruker TopSpin** software and fitted using **DMFit**. The fitting files (`1R.fxml`) for each experiment are provided in their respective directories, and the fits can be visualized using DMFit.

### Raw Data and Fits:
- **NaNbO<sub>2</sub>F<sub>2</sub>:**
  - <sup>19</sup>F: [Raw Data and Fit](./NaNbO2F2/19F)
  - <sup>23</sup>Na: [Raw Data and Fit](./NaNbO2F2/23Na)
  - <sup>93</sup>Nb: [Raw Data and Fit](./NaNbO2F2/93Nb)
  
- **NaTaO<sub>2</sub>F<sub>2</sub>:**
  - <sup>19</sup>F: [Raw Data and Fit](./NaTaO2F2/19F)
  - <sup>23</sup>Na: [Raw Data and Fit](./NaTaO2F2/23Na)

### Requirements
To analyze and visualize the ssNMR data, the following equipment and software are required:

- **Equipment Requirements:**
  - **Bruker Avance III** spectrometer (7 T and 20 T) or equivalent, along with **CP-MAS probe-heads**.
  
- **Software Requirements:**
  - **Bruker TopSpin:** Required to process and visualize the raw NMR data. You can obtain the software from [Bruker's website](https://www.bruker.com/en/products-and-solutions/mr/nmr-software/topspin.html?s_kwcid=AL!14677!3!648890112603!p!!g!!nmr%20software%20free%20download&utm_source=Advertising&utm_medium=GoogleAd&utm_campaign=BBIO-Software-Cross-All-Software-H2-2024&gad_source=1&gclid=Cj0KCQjwgL-3BhDnARIsAL6KZ6-3cOPvJBH5UNxRvUrDug2NC94E8Bw_iE3Ey2GcHur_1z1SLIEYV5caApz2EALw_wcB).
  - **DMFit:** Required to fit the NMR spectra. The software is available for download at the [DMFit website](https://nmr.cemhti.cnrs-orleans.fr/).

---

For further details, please refer to the respective folders or contact the author via the provided email.
