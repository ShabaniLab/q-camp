# Quantum programming projects

Here is a list of quantum algorithm you can choose from. Ideally these projects are individual and everyone should have a different topic. You can come up with your own project as well if you think you can solve a problem more efficiently on a quantum computer compared to a classical one. There are more ideas in the [qiskit textbook](https://qiskit.org/textbook/preface.html) as well, check that out!

* [Quantum Key Distribution](https://en.wikipedia.org/wiki/Quantum_key_distribution): is a quantum algorithm that could be used for secure communication between two parties (Alice and Bob) where there is a third party (Charlie) evesdropping on the messages.  
[qiskit example](https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html)  
* Quantum Money: is based on the *[no cloning](https://en.wikipedia.org/wiki/No-cloning_theorem)* theorem which allows one to produce non-forgeable documents such as bills or id's.  
[Shor's slides](https://simons.berkeley.edu/sites/default/files/docs/15601/qmoney-berkeley.pdf)   
* [Quantum Teleportation](https://en.wikipedia.org/wiki/Quantum_teleportation): is an algorithm for transferring a generic quantum state (e.g. a qubit state). It is closely related to the [no-cloining theorem](https://en.wikipedia.org/wiki/No-cloning_theorem) in quantum computing.  
[qiskit example](https://qiskit.org/textbook/ch-algorithms/teleportation.html)  
* [Shor's algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm): is a quantum algorithm for factoring an integer number into it's prime factors. This algorithm promises an exponential speed up over classical factoring algorithms.  
[qiskit example](https://qiskit.org/textbook/ch-algorithms/shor.html). Also check out [this article](https://rajkk1.medium.com/finding-the-prime-factors-of-a-large-number-efficiently-with-the-help-of-shors-algorithm-e731f0aadff5). 
* 
* Variational Quantum Eigensolver: is a hybrid classical-quantum algorithm that could be used for optimization problems where you want to find the minimum or maximum of a function. It has broad applications in quantum computing since several combinatorial problems (e.g. graph partitioning) as well as physics problems (i.e. finding the lowest energy level of a system) can be solved using this algorithm.  
[qiskit example: Simulating molecules using VQE](https://qiskit.org/textbook/ch-applications/vqe-molecules.html)  

* [Quantum Approximate Optimization Algorithm](https://arxiv.org/abs/1411.4028) also has applications in solving difficult combinatorial problems.  
[qiskit example](https://qiskit.org/documentation/tutorials/algorithms/05_qaoa.html) on graph partitioning.  


# What to do

- read about the problem on its wiki page, 
- implement the solution using classical computation (e.g. in `python`)
- go through the `qiskit` example, if there is any. ([qiskit textbook](https://qiskit.org/textbook/preface.html))
- implement the quantum solution (i.e. in `qiskit`)
- analyze how different the classical and quantum solutions are (e.g. in terms of the probability of success, complexity of the problem, and etc)
- prepare a presentation (written doc, slides, or jupyter notebook)


