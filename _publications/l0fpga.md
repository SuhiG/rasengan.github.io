---
title: "Highly Versatile FPGA-Implemented Cyber Coherent Ising Machine"
collection: publications
permalink: /publications/l0fpga
excerpt: ''
date: 2024-06-08
venue: 'arXiv (under review)'
paperurl: ''
citation: ''

---
<div style="text-align: justify"> In recent years, quantum Ising machines have drawn a lot of attention, but due to physical implementation constraints, it has been difficult to achieve dense coupling, such as full coupling with sufficient spins to handle practical large-scale applications. Consequently, classically computable equations have been derived from quantum master equations for these quantum Ising machines. Parallel implementations of these algorithms using FPGAs have been used to rapidly find solutions to these problems on a scale that is difficult to achieve in physical systems. We have developed an FPGA implemented cyber coherent Ising machine (cyber CIM) that is much more versatile than previous implementations using FPGAs. Our architecture is versatile since it can be applied to the open-loop CIM, which was proposed when CIM research began, to the closed-loop CIM, which has been used recently, as well as to Jacobi successive over-relaxation method. By modifying the sequence control code for the calculation control module, other algorithms such as Simulated Bifurcation (SB) can also be implemented. Earlier research on large-scale FPGA implementations of SB and CIM used binary or ternary discrete values for connections, whereas the cyber CIM used FP32 values. Also, the cyber CIM utilized Zeeman terms that were represented as FP32, which were not present in other large-scale FPGA systems. Our implementation with continuous interaction realizes N=4096 on a single FPGA, comparable to the single-FPGA implementation of SB with binary interactions, with N=4096. The cyber CIM enables applications such as CDMA multi-user detector and L0 compressed sensing which were not possible with earlier FPGA systems, while enabling superior calculation speeds, more than ten times faster than a GPU implementation. The calculation speed can be further improved by increasing parallelism, such as through clustering. </div>

[Download paper here](ttps://doi.org/10.48550/arXiv.2406.05377){:target="_blank"}  <br>
<!-- [Related code here](/404.html){:target="_blank"}  -->


**Recommended citation:** Aonishi, T, Nagasawa, T, Koizumi, T, Gunathilaka, M.D.S.H. et al. Highly Versatile FPGA-Implemented Cyber Coherent Ising Machine. arXiv.2406.05377 (2024).