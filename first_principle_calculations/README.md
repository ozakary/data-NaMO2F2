# NaMO<sub>2</sub>F<sub>2</sub> (M = Nb<sup>5+</sup>, Ta<sup>5+</sup>) Geometry Optimization and NMR Parameters Calculations
**Author**: Ouail Zakary \
**ORCID**: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306) \
**E-mail**: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi) \
**Website**: [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)

This repository contains datasets from DFT calculations performed to optimize the local structures of NaMO<sub>2</sub>F<sub>2</sub> (M = Nb<sup>5+</sup>, Ta<sup>5+</sup>) and to compute their NMR parameters.

## Overview of the Data

The dataset includes both **inputs** (located in the folders: `INPUT_files`) and **outputs** (located in the folders: `OUTPUT_files`) for the following calculations:

1. **NMR Parameter Calculations for the Experimental Structure (ES):**  
   Based on X-ray powder diffraction patterns refined at room temperature using the Rietveld refinement method for NaNbO<sub>2</sub>F<sub>2</sub> and NaTaO<sub>2</sub>F<sub>2</sub>.  
   **Folder:** `./NaNbO2F2/ES_NMR` and `./NaTaO2F2/ES_NMR`

2. **Atomic Position Optimization (APO) of ES:**  
   **Folder:** `./NaNbO2F2/APO` and `./NaTaO2F2/APO`

3. **NMR Parameters Calculations of APO:**  
   **Folder:** `./NaNbO2F2/APO_NMR` and `./NaTaO2F2/APO_NMR`

4. **Full Optimization (FO) of ES:**  
   **Folder:** `./NaNbO2F2/FO` and `./NaTaO2F2/FO`

5. **NMR Parameters Calculations of FO:**  
   **Folder:** `./NaNbO2F2/FO_NMR` and `./NaTaO2F2/FO_NMR`

The `.slurm` files (named `<name>_jv_oz.slurm`, where `name` corresponds to each calculation) and the `.log` files (named `<name>_vasp_run.log`) can be found in their respective folders.

## Methods

### Geometry Optimization (APO and FO) using `VASP`

All first-principles calculations were performed using the **VASP** code (version 6.2.1). The **density functional theory (DFT)** approach used a wave function expanded on a plane-wave basis set, with a **550 eV** kinetic energy cut-off and a **(4 × 6 × 4)** shifted Monkhorst-Pack k-point mesh. The ground-state electronic structure was obtained by **the generalized gradient approximation (GGA)** using **the Perdew–Burke–Ernzerhof (PBE)** functional **(GGA-PBE)**. The interactions between core and valence electrons were treated using the **projector augmented wave (PAW)** method, incorporating the following PAW potentials and core electronic configurations:

- **O:** *O_s_GW*, core configuration: [He] 2s<sup>2</sup> 2p<sup>4</sup>
- **F:** *F_GW*, core configuration: [He] 2s<sup>2</sup> 2p<sup>5</sup>
- **Na:** *Na_sv_GW*, core configuration: [Ne] 3s<sup>1</sup>
- **Nb:** *Nb_sv_GW*, core configuration: [Kr] 4s<sup>2</sup> 4p<sup>6</sup> 4d<sup>4</sup> (5 electrons in the valence shell)
- **Ta:** *Ta_sv_GW*, core configuration: [Xe] 5s<sup>2</sup> 5p<sup>6</sup> 5d<sup>4</sup> (5 electrons in the valence shell)

Atomic positions were relaxed until forces converged to less than **0.1 meV/Å**, and total energy convergence was set to below **10<sup>–8</sup> eV**.

### NMR Parameters Calculations (ES_NMR, APO_NMR, and FO_NMR)

The **PAW** and **gauge including projector augmented wave (GIPAW)** methods were used to compute quadrupolar coupling NMR parameters (*C*<sub>Q</sub>, *η*<sub>Q</sub>) and magnetic shielding values (*σ*<sub>iso</sub>, *σ*<sub>CSA</sub>, *η*<sub>CSA</sub>). All parameters were set the same as those in the DFT relaxation process.

### Tensor Convention and Magnetic Shielding to Chemical Shift Conversion

Magnetic shielding tensors and experimental chemical shift parameters follow the **Haeberlen convention**. Definitions include:

- **Isotropic magnetic shielding (*σ*<sub>iso</sub>):** *σ*<sub>iso</sub> = (*σ*<sub>xx</sub> + *σ*<sub>yy</sub> + *σ*<sub>zz</sub>)/3  
- **Anisotropy of magnetic shielding (*σ*<sub>CSA</sub>):** *σ*<sub>CSA</sub> = *σ*<sub>zz</sub> – *σ*<sub>iso</sub>  
- **Asymmetry parameter (*η*<sub>CSA</sub>):** *η*<sub>CSA</sub> = (*σ*<sub>yy</sub> – *σ*<sub>xx</sub>)/*σ*<sub>CSA</sub>

In this study, NMR chemical shift values (*δ*<sub>iso</sub>) for **<sup>23</sup>Na** and **<sup>93</sup>Nb** were obtained from established linear regressions. For **<sup>19</sup>F**, new linear regressions from NaF and NaNbO<sub>2</sub>F<sub>2</sub> or NaTaO<sub>2</sub>F<sub>2</sub> were used.

## Directory Structure

The following directories contain the datasets:

- **NaNbO<sub>2</sub>F<sub>2</sub> Datasets:**
  - [APO INPUT files](./NaNbO2F2/APO/INPUT_files)
  - [APO OUTPUT files](./NaNbO2F2/APO/OUTPUT_files)
  - [APO_NMR INPUT files](./NaNbO2F2/APO_NMR/INPUT_files)
  - [APO_NMR OUTPUT files](./NaNbO2F2/APO_NMR/OUTPUT_files)
  - [ES_NMR INPUT files](./NaNbO2F2/ES_NMR/INPUT_files)
  - [ES_NMR OUTPUT files](./NaNbO2F2/ES_NMR/OUTPUT_files)
  - [FO INPUT files](./NaNbO2F2/FO/INPUT_files)
  - [FO OUTPUT files](./NaNbO2F2/FO/OUTPUT_files)
  - [FO_NMR INPUT files](./NaNbO2F2/FO_NMR/INPUT_files)
  - [FO_NMR OUTPUT files](./NaNbO2F2/FO_NMR/OUTPUT_files)

- **NaTaO<sub>2</sub>F<sub>2</sub> Datasets:**
  - [APO INPUT files](./NaTaO2F2/APO/INPUT_files)
  - [APO OUTPUT files](./NaTaO2F2/APO/OUTPUT_files)
  - [APO_NMR INPUT files](./NaTaO2F2/APO_NMR/INPUT_files)
  - [APO_NMR OUTPUT files](./NaTaO2F2/APO_NMR/OUTPUT_files)
  - [ES_NMR INPUT files](./NaTaO2F2/ES_NMR/INPUT_files)
  - [ES_NMR OUTPUT files](./NaTaO2F2/ES_NMR/OUTPUT_files)
  - [FO INPUT files](./NaTaO2F2/FO/INPUT_files)
  - [FO OUTPUT files](./NaTaO2F2/FO/OUTPUT_files)
  - [FO_NMR INPUT files](./NaTaO2F2/FO_NMR/INPUT_files)
  - [FO_NMR OUTPUT files](./NaTaO2F2/FO_NMR/OUTPUT_files)

## Requirements

The calculations in this folder were performed on the **IMMM cluster** in Le Mans Université using the **charger (node with 48 CPUs and 192Go memory)**. To run the calculations in this folder, you will need:

- **VASP** installed on your local machine or accessible on a supercomputer cluster (more information about **VASP** can be found in [VASP - website](https://www.vasp.at/)).
- A compatible **CPU** (e.g., Intel or AMD) with sufficient computational resources for running DFT calculations.
- The job batch script is configured for the SLURM workload manager and includes specifications for nodes, tasks, runtime, memory, and other settings. Modify the script to suit your specific calculation needs.

---

For further details, please refer to the respective folders or contact the author via the provided email.
