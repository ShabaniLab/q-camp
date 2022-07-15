# Engineering microwave filters: design, implementation, and measurement

## Background 

### What are filters? 
Filters are essential components of both ordinary microwave systems (e.g. wireless communications) as well as current superconducting qubit technology. They are two-port circuits that are used to control the frequency response of systems by transmitting frequencies within the passband of the filter and attenuating frequencies in the stopband of the filter. There are different types of filters typically called low-pass, high-pass, band-pass, and band-reject. 

### Why are filters important in quantum computing hardware? 
Current quantum computers are made of superconducting qubits which are delicate micrometer scale circuits that need to be kept at cryogenic temperatures and isolated well from the environement and various sources of noise. Different types of filters are used to achieve that. 

### What is a waveguide? 
A waveguide is a structure that is used to guide and filter electromagnetic waves. They have a specific response to waves with different frequencies. The response is mostly determined by the geometry of the struture as well as the electromagnetic properties of the underlying materials (e.g. permittivity). They are used in power transmission lines, electronics, communication devices (cell phones, routers, etc), as well as superconducting qubits and resonators. 

### What is this project about? 
In this project, the goal is to design, implement, and measure a band-pass filter that transmits frequencies around the qubit frequency. The filter will be designed in a [coplanar waveguide](https://en.wikipedia.org/wiki/Coplanar_waveguide) structure. We will implement our design on a printed circuit board made of copper in the lab using a milling machine. Finally, after soldering connectors, we will measure the frequency response of our filter with the [network analyzer](https://en.wikipedia.org/wiki/Network_analyzer_(electrical)) and analyze the results.  

### technical specifications
qubit frequency: `f_0 = 6 GHz`  
bandwidth: `0.3 GHz`  
copper board's thickness: `3 mm`  
copper coat's thickness: `0.5 mm`    
milling machine's endmill size: `1/64 in`

## What to do 
### 1. Read about filters and coplanar waveguide 
Start by reading papers number 3 and 4.  
Use chapters 3 and 8 of Pozar's book for reference.

### 2. Find the lumped circuit elements for the filter 
What is the circuit configuration: pi, T, etc

### 3. Find the equivalent coplanar waveguide structure 
Calculate the geometry such as size of the gaps, width of the middle strip, etc.  
Write a code that takes the technical specifications as input and calculates all the relevant info about geometry of the waveguide.  

### 4. Design the printed circuit board (PCB)
Info about the software will be provided later.  
Don't forget to add [SMA](https://en.wikipedia.org/wiki/SMA_connector) connectors to your design. 

### 5. Build the printed circuit board using the milling machine 
Info about the operation of the machine will be provided later.  
[Here](https://core-electronics.com.au/othermill-compact-precision-cnc-pcb-milling-machine.html) are the specs of the machine  
https://www.scu.edu/engineering/makerlab/tools--equipment/othermill-cnc/  
https://www.youtube.com/watch?v=8LUEU7ECTu4  

### 6. Solder the SMA connectors to the PCB
soldering tutorial video will be posted. 

### 7. Connect to the VNA and measure and save the frequency response
manual will be provided later. 

### 8. Analyze the data 

### 9. Prepare a report + presentation 

## Resources 
1. **Microwave Engineering** by David M Pozar 
2. **[A Quantum Engineer's Guide to Superconducting Qubits](https://arxiv.org/abs/1904.06560)**
3. A sample thesis: [Development of a microwave low-pass filter for cryogenic superconducting quantum computing applications](https://qudev.phys.ethz.ch/static/content/science/Documents/semester/Bechstein_Daniel_SemesterThesis_090730_LowPassFilter.pdf)
4. A sample paper: [Narrow bandpass cryogenic filter for microwave measurements](https://aip.scitation.org/doi/10.1063/1.4807152)
