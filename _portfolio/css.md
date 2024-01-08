---
title: "Coherent Compressed Sensor"
excerpt: "L0-Regularsied Compressed Sensing with Coherent Ising Machines"
collection: portfolio
---

<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>

<div style="text-align: justify"> It has been demonstrated that Coherent Ising Machines (CIM) are capable of solving combinatorial optimisation problems (COP). It has not, however, been used in practical applications. The goal of this project is to analyze CIM's capability to solve a famous COP called L0-Regularised Compressed Sensing (L0RBCS). In compressed sensing (CS), highly downsampled measurements are used to reconstruct a high-dimensional signal. This technique is very useful in a wide range of fields, including astronomy, radar technology, and Magnetic Resonance Imaging (MRI). Our objective here is to simulate large-scale CS problem instances (which include both random and real-world problem instances) using CIM and propose an algorithm that can outperform the most commonly used LASSO algorithm. </div> <br>

**Project Outline**

Intial approach for the Coherent Compressed Sensor was introduced by Prof. Toru Aonishi at the University of Tokyo ([Patent](https://patents.google.com/patent/WO2022178173A1/en?q=(L0+REGULARIZATION-BASED+COMPRESSED+SENSING+SYSTEM+AND+METHOD+WITH+COHERENT+ISING+MACHINES)&oq=L0+REGULARIZATION-BASED+COMPRESSED+SENSING+SYSTEM+AND+METHOD+WITH+COHERENT+ISING+MACHINES+)). <br>

Considering the below equation, <br>
$$
\begin{equation}
\label{l0init2}
    \hat{x} = \operatorname*{argmin}_{x \in \mathbb{R}^N}\|x\|_{p} \ \ subject \ to \ y = Ax .
\end{equation}
$$

**Related Publications** <br>

[CAC-CIM-CDP](https://doi.org/10.1038/s41598-023-43364-8) <br>
[Related code here](/404.html)

<!-- <img src="/images/gacs_Figure_6.png" alt="gacs" style="height: 500px; width:300px;"/> -->