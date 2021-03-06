# Quantum programming projects

Here is a list of quantum algorithm you can choose from. Ideally these projects are individual and everyone should have a different topic. You can come up with your own project as well if you think you can solve a problem more efficiently on a quantum computer compared to a classical one. There are more ideas in the [qiskit textbook](https://qiskit.org/textbook/preface.html) as well, check that out!

## Quantum Key Distribution
* [Quantum Key Distribution](https://en.wikipedia.org/wiki/Quantum_key_distribution): is a quantum algorithm that could be used for secure communication between two parties (Alice and Bob) where there is a third party (Charlie) evesdropping on the messages.  
[qiskit example](https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html)  

## Quantum money
* Quantum Money: is based on the *[no cloning](https://en.wikipedia.org/wiki/No-cloning_theorem)* theorem which allows one to produce non-forgeable documents such as bills or id's.  
[Shor's slides](https://simons.berkeley.edu/sites/default/files/docs/15601/qmoney-berkeley.pdf)   

## Quantum finance 
Here are two review articles: 
* [A survey of quantum computing for finance](https://arxiv.org/abs/2201.02773)
* [Prospects and challenges of quantum finance](https://arxiv.org/abs/2011.06492)

## Quantum teleportation 
* [Quantum Teleportation](https://en.wikipedia.org/wiki/Quantum_teleportation): is an algorithm for transferring a generic quantum state (e.g. a qubit state). It is closely related to the [no-cloining theorem](https://en.wikipedia.org/wiki/No-cloning_theorem) in quantum computing.  
[qiskit example](https://qiskit.org/textbook/ch-algorithms/teleportation.html)  

## Shor's algorithm 
* [Shor's algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm): is a quantum algorithm for factoring an integer number into it's prime factors. This algorithm promises an exponential speed up over classical factoring algorithms.  
[qiskit example](https://qiskit.org/textbook/ch-algorithms/shor.html). Also check out [this article](https://rajkk1.medium.com/finding-the-prime-factors-of-a-large-number-efficiently-with-the-help-of-shors-algorithm-e731f0aadff5). 

## Variational Quantum Eigensolver 
* Variational Quantum Eigensolver: is a hybrid classical-quantum algorithm that could be used for optimization problems where you want to find the minimum or maximum of a function. It has broad applications in quantum computing since several combinatorial problems (e.g. graph partitioning) as well as physics problems (i.e. finding the lowest energy level of a system) can be solved using this algorithm.  
[qiskit example: Simulating molecules using VQE](https://qiskit.org/textbook/ch-applications/vqe-molecules.html)  
[Hardware-efficient VQE for small molecules](https://arxiv.org/abs/1704.05018)

## Quantum Approximate Optimization Algorithm 
* [Quantum Approximate Optimization Algorithm](https://arxiv.org/abs/1411.4028) is an algorithm used for finding optimal solutions in combinatorial problems.   
A set of problems that can be solved using QAOA algorithm is called [Quadratic Unconstrained Binary Optimization](https://en.wikipedia.org/wiki/Quadratic_unconstrained_binary_optimization). Examples of these problems are maximum cut, graph coloring, and the partition problem.  
[qiskit example](https://qiskit.org/documentation/tutorials/algorithms/05_qaoa.html) on graph partitioning.  
other ideas: [Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem)

## Quantum Machine Learnning 
* [qiskit tutorials](https://qiskit.org/documentation/machine-learning/tutorials/index.html)
* [Quantum advantage in learning from experiments](https://arxiv.org/abs/2112.00778)

# What to do

- read about the problem on its wiki page, 
- implement the solution using classical computation (e.g. in `python`)
- go through the `qiskit` example, if there is any. ([qiskit textbook](https://qiskit.org/textbook/preface.html))
- implement the quantum solution (i.e. in `qiskit`)
- analyze how different the classical and quantum solutions are (e.g. in terms of the probability of success, complexity of the problem, and etc)
- prepare a presentation (written doc, slides, or jupyter notebook)


