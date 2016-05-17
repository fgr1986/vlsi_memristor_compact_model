# VLSI Memristor/RRAM SPICE Compact Model
## README

version v1.1.0, 17/05/2016

## Author contact:
* [Fernando García Redondo](http://www.fernandeando.com)
* [fgarcia@die.upm.es](mailto:fgarcia@die.upm.es)
* [Technical University of Madrid UPM](lsi.die.upm.es/)

## License:
Copyright of the model is maintained by the developers,
and the model is distributed under a Dual-Licence mode.

* **GPL License** apply for academic purposes.
If you use this model in your work, you are requested to cite [1] in the reference.
GitHub Repository and Downloads
* **Commercial license** for other purposes not meeting GPL license: Contact *fgarcia@die.upm.es*

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

### Compact model examples:
* Bipolar examples in **X/bipolar_aSiCCuTiN** and **spice/charge_controlled** folders.
* Unipolar examples in **X/unipolar_NiHfO2Si** folder.
* Variability (RTN and cycle/voltage dependent) examples in **spectre/bipolar_aSiCCuTiN** folder
* RRAM Multi-level examples in **spectre/bipolar_aSiCCuTiN** and **spice/bipolar_aSiCCuTiN** folders
* Pristine (Pre-forming) state examples in **spectre/bipolar_aSiCCuTiN** folder
* Temperature-dependency examples in **spectre/bipolar_aSiCCuTiN** folder
* Standard (phenomenological) charge controlled examples in **spice/charge_controlled** folder

![Variability example](http://vlsi.die.upm.es/Image?imageId=27&size=2)

## Full Description
See **SPICE Compact Modeling of Bipolar/Unipolar Memristor Switching Governed by Electrical Thresholds**,
*Fernando García-Redondo, Robert P. Gowers, A. Crespo-Yepes,Marisa López-Vallejo and Liudi Jiang*,
**IEEE Transactions on Circuits and Systems--I: Regular Papers**,
2016, DOI: 10.1109/TCSI.2016.2564703

## Proyect pages:
* https://github.com/fgr1986/vlsi_memristor_compact_model
* http://vlsi.die.upm.es/memristor_spice_model
* http://vlsi.die.upm.es/memristor

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
