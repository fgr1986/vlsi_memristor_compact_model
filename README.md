# VLSI Memristor/RRAM SPICE Compact Model
## README

version v1.0.0, 10/05/2016

Author: Fernando García Redondo, Technical University of Madrid UPM

Copyright of the model is maintained by the developers,
and the model is distributed under a Dual-Licence mode.

* **GPL License** apply for academic purposes.
If you use this model in your work, you are requested to cite [1] in the reference.
GitHub Repository and Downloads
* **Commertial license** for other purposes not meeting GPL license: Contact *fgarcia@die.upm.es*

## Short Description
Physical memristor/RRAM/resistive switching device SPICE compact model,
that is able to accurately fit both unipolar/bipolar devices settling to its
current-voltage relationship.

Main capabilities:
* Accurate modeling of dynamic resistance, mimicking physical device response.
* Modeling switching behavior for bipolar/unipolar devices.
* Cycle and switching event count.
* Modular and extensible: Temperature aware case of study.
* Variability aware: voltage/cycle dependent RTN, cycle to cycle conduction changes.
* Provision of variability dynamics and resistive state
retention handling, defining how the device degrades
through time/cycle stress.
* Explicit support for multi-level storage, allowing
the modeling of Pristine State -the initial High
Resistive State (HRS) prior any electroforming-.
* Project page: http://vlsi.die.upm.es/memristor

Both LT-Spice and Cadence Spectre compact models/test benches
are provided.

## Full Description
See **SPICE Compact Modeling of Bipolar/Unipolar Memristor Switching Governed by Electrical Thresholds**,
*Fernando García-Redondo, Robert P. Gowers, A. Crespo-Yepes,Marisa López-Vallejo and Liudi Jiang*,
**IEEE Transactions on Circuits and Systems--I: Regular Papers**,
2016, DOI: 10.1109/TCSI.2016.2564703

## Proyect pages:
* http://vlsi.die.upm.es/memristor_spice_model
* http://vlsi.die.upm.es/memristor

## Author contact:
* [Fernando García Redondo](http://www.fernandeando.com)
* [fgarcia@die.upm.es](mailto:fgarcia@die.upm.es)

## Memristor Publications:
### Compact Model Publications
* **[1] SPICE Compact Modeling of Bipolar/Unipolar Memristor Switching Governed by Electrical Thresholds**
  *Fernando García-Redondo, Robert P. Gowers, A. Crespo-Yepes,Marisa López-Vallejo and Liudi Jiang*
  **IEEE Transactions on Circuits and Systems--I: Regular Papers**
  > 2016, DOI: 10.1109/TCSI.2016.2564703

### Memristor Application Framework Publications
* **[2] Building Memristor Applications: From Device Model to Circuit Design**
  *Fernando García-Redondo; Marisa López-Vallejo; Pablo Ituero*
  **IEEE Transactions on Nanotechnology**
  > 2014, DOI: 10.1109/TNANO.2014.2345093

* **[3] A CAD Framework for the Characterization and Use of Memristor Models**
  *Fernando García-Redondo, Marisa López-Vallejo, Pablo Ituero, Carlos López Barrio*
  **Synthesis, Modeling, Analysis and Simulation Methods and Applications to Circuit Design (SMACD), 2012 International Conference on**
  > 2012, DOI: 10.1109/SMACD.2012.6339408

* **[4] Model Validation and Simulation Framework for Novel Nanometer Devices**
  *Fernando García-Redondo, Marisa López-Vallejo, Pablo Ituero, Carlos López Barrio*
  **Conference on Design of Circuits and Integrated Systems 2012 (DCIS 2012), At Avignon (France)**
  > 2012, DOI: 10.13140/2.1.1323.8721

### Memristor In Circuit Simulators, Mathematical Description Publications
* **[5] The tractability index of memristive circuits: branch-oriented and tree-based models.**
  *Fernando García-Redondo, Ricardo Riaza*
  **Mathematical Methods in the Applied Sciences.**
  > 2012 DOI: 10.1002/mma.2544
