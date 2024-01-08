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
<div style="text-align: center"> 
$$
        \begin{equation}
        \label{l0init2}
            \hat{x} = \operatorname*{argmin}_{x \in \mathbb{R}^N}\|x\|_{p} \ \ subject \ to \ y = Ax ,
        \end{equation}
$$
 </div>
 
an observed signal $y \in \mathbb{R}^M$, an observation matrix $A \in \mathbb{R}^{M\times N}$, and a source signal $x \in \mathbb{R}^N$ can be stated. In CS, the ratio of the number of non-zero entries in $x$ to $N$ is defined as the sparseness $a$, and the ratio of $M$ to $N$ is defined as the compression ratio $\alpha$. If we consider where $p=1$, the problem becomes a $l_1$-norm CS problem which is convex and has many efficeint algorithms avaialble (FISTA, ISTA, etc.). However $p=0$ is non-convex and it is a combinatorial optimisation problem. 

Numerous attempts have been made to overcome the issue in $l_0$-norm CS optimisations. $l_0$-norm CS can be formulated as a two-fold optimisation.
<div style="text-align: center"> 
$$
        \begin{equation}
        \label{l0}
            (\hat{R}, \hat{\sigma}) = \operatorname*{argmin}_{\sigma \in \{0,1\}^{N}}\operatorname*{argmin}_{R\in\mathbb{R}^{N}} \left(\| y - A(\sigma \circ R)\|_{2}^{2}\right) \ \ subject \ to \   \|\sigma\|_{0} \le \Omega .
        \end{equation}
$$
 </div>

Here $R \in \mathbb{R}^N$ and $\sigma \in \left(0,1\right)^N$ correspond to the source signal and support vector, respectively. 
Especially, each entry in the support vector taking either 0 or 1 represents whether each entry in the source signal is zero or non-zero. The condition $\|\sigma\|_{0} \le \Omega$ is a sparsity-inducing prior for constraining the number of non-zero entries to be $\Omega$. Therefore, the optimisation with respect to $\sigma$ can be regarded as a quadratic-constrained binary optimisation problem to find a ground state of a two-state Potts Hamiltonian.

The $l_0$-norm CS implemented with the open-loop quantum-classical hybrid system by Aonishi $\textit{et al}.$, is given as a regularisation form as follows 

<div style="text-align: center"> 
$$
        \begin{equation}
        \label{doublel0}
            (R, \sigma) = \operatorname*{argmin}_{\sigma \in \{0,1\}^{N}}\operatorname*{argmin}_{R\in\mathbb{R}^{N}} \left(\frac{1}{2} \| y - A(\sigma \circ R)\|_{2}^{2} + {\lambda} \|\sigma\|_{0}\right) .
        \end{equation}
$$
 </div>

The element-wise representation of the above equation gives the following Hamiltonian.

<div style="text-align: center"> 
$$
        \begin{equation}
        \label{l0Hamiltonian}
            {H} = \sum_{r<r'}^{N}\sum_{k = 1}^{M} A_{r}^{k}A_{r'}^{k}R_{r}R_{r'}\sigma_{r}\sigma_{r'} - \sum_{r=1}^{N}\sum_{k =1}^{M} y^{k}A_{r}^{k}R_{r}\sigma_{r} + {\lambda} \sum_{r = 1}^{N} \sigma_r , 
        \end{equation}
$$
 </div>

where an element $A^k$ in $A$, an element $y^k$ in $y$, an element $R_r$ in $R$ and an element $\sigma_r$ in $\sigma$. In the quantum-classical hybrid approach to conducting $l_0$-regularised CS, $\sigma$ is optimised by the CIM while $R$ is optimised by a Classical Digital Processor (CDP).

<!-- <p>
    <img src="https://github.com/SuhiG/rasengan.github.io/blob/master/images/olccsarch.jpg" width="220" height="240" /> <br>
</p>  -->
[Quantum-Classical Hybrid architecture](https://github.com/SuhiG/rasengan.github.io/blob/master/images/olccsarch.jpg) <br>

**CCS versions** <br>

> **Open-Loop CCS**

<div style="text-align: center"> 
$$
        \begin{equation}
        \label{localfieldmain}
            \left(\dfrac{dc_{r}}{dt}\right)_{inj,r} = \left(|h_r| - \eta\right).
        \end{equation}
$$
 </div>
  
<div style="text-align: center"> 
$$
        \begin{equation}
        \label{localfieldSparse}
                h_{r} = -{\sum_{r' = 1 (\neq r)}^{N}\sum_{k = 1}^{M}} A_r^k A_{r'}^k R_{r'}H(c_{r'}) + \sum_{k=1}^M A_{r}^k y^{k},
        \end{equation}
$$
 </div>
 
<div style="text-align: center"> 
$$
        \begin{equation}
        \label{WSDE0}
                \frac{d}{dt}c_r = \left[-1 + p - {\left(c_r^2 + s_r^2\right)} \right]c_r + \widetilde{K}\left(\dfrac{dc_{r}}{dt}\right)_{inj,r} + {g^2}\sqrt{\left(c_r^2 + s_r^2\right) + \frac{1}{2}} W_{r,1},
        \end{equation}
$$
 </div>
 
<div style="text-align: center"> 
$$
        \begin{equation}
        \label{WSDE1}
                \frac{d}{dt}s_r = \left[-1 - p - {\left(c_r^2 + s_r^2\right)}\right]s_r + {g^2}\sqrt{\left(c_r^2 + s_r^2\right) + \frac{1}{2}} W_{r,2} .
        \end{equation}
$$
</div>
 

> **Closed-Loop CCS (truncated-Wigner)**

<div style="text-align: center"> 
$$
        \begin{equation}
        \label{GACSlocalfieldmain}
            \left(\dfrac{d\mu_{r}}{dt}\right)_{inj,r} = je_r\left( R_r h_r - \dfrac{\eta^2}{{2}}\sqrt{\dfrac{\tau}{g^2}}\right),
        \end{equation}
$$
 </div>
 
<div style="text-align: center"> 
$$
        \begin{equation}
        \label{GaussianEC5}
                {\dfrac{d}{dt}e_{r} = -\beta\left(g^2\tilde{\mu}_{r}^2 - \tau\right)e_{r}},
        \end{equation}
$$
 </div>
 
<div style="text-align: center"> 
$$
        \begin{equation}
        \label{GACsCIM3}
                \tilde{\mu}_{r} = \mu_{r} + \sqrt{\frac{1}{4j}}W_{R,r},
        \end{equation}
$$
 </div>

<div style="text-align: center"> 
$$ 
        \begin{equation}
        \label{localfieldGACS}
            h_r = -{\sum_{r' = 1 (\neq r)}^{N}\sum_{k = 1}^{M}} A_{r}^{k}A_{r'}^{k}R_{r'}\dfrac{1}{2}\left(\tilde{\mu}_{r'} + \sqrt{\dfrac{\tau}{g^2}} \right) {+} \sum_{k = 1}^{M} \sqrt{\dfrac{\tau}{g^2}}{A_{r}^{k}y^{k}},
        \end{equation}
$$
 </div>
 
 <div style="text-align: center"> 
$$
        \begin{equation}
        \label{GACsCIM1}
                \dfrac{d}{dt}\mu_{r} = - \left(1 -p + j\right)\mu_{r} - g^2\mu_{r}^3 + \sqrt{j}\left(V_{r} - \frac{1}{2}\right)W_{R,r} + {{K}}\left(\frac{d\mu_{r}}{dt}\right)_{inj,r},
        \end{equation}
$$
 </div>
 
 <div style="text-align: center"> 
$$
        \begin{equation}
        \label{GACsCIM2}
                \dfrac{d}{dt}V_{r} = -2 \left(1 -p + j\right)V_{r} - 6g^2\mu_{r}^2V_{r} + 1 + j + 2g^2\mu_{r}^2 - 2j\left(V_{r} -\frac{1}{2}\right)^2 .
        \end{equation}
$$
 </div>
 

> **Closed-Loop CCS (Positive-$$\textit{P}$$)**

<div style="text-align: center"> 
$$
        \begin{equation}
            \left(\dfrac{d\mu_{r}}{dt}\right)_{inj,r} = je_r\left( R_rh_r - \dfrac{\eta^2}{{2}}\sqrt{\dfrac{\tau}{g^2}}\right),
        \end{equation}
$$
 </div>

<div style="text-align: center"> 
$$
        \begin{equation}
                {\dfrac{d}{dt}e_{r} = -\beta\left(g^2\tilde{\mu}_{r}^2 - \tau\right)e_{r}},
        \end{equation}
$$
 </div>
 
<div style="text-align: center"> 
$$
        \begin{equation}
                \tilde{\mu}_{r} = \mu_{r} + \sqrt{\frac{1}{4j}}W_{R,r},
        \end{equation}
$$
 </div>
 
<div style="text-align: center"> 
$$
        \begin{equation}
            h_r = -{\sum_{r' = 1 (\neq r)}^{N}\sum_{k = 1}^{M}} A_{r}^{k}A_{r'}^{k}R_{r'}\dfrac{1}{2}\left(\tilde{\mu}_{r'} + \sqrt{\dfrac{\tau}{g^2}} \right) {+} \sum_{k = 1}^{M} \sqrt{\dfrac{\tau}{g^2}}{A_{r}^{k}y^{k}},
        \end{equation}
$$
 </div>
  
<div style="text-align: center"> 
$$
        \begin{equation}
                \dfrac{d}{dt}\mu_{r} = - \left(1 -p + j\right)\mu_{r} - {g^2\mu_{r}\left(\mu_{r}^{2} + 2n_r + m_r\right)} + \sqrt{j}\left(m_r + n_r\right)W_{R,r}\\ + {{K}}\left(\frac{d\mu_{r}}{dt}\right)_{inj,r},
        \end{equation}
$$
 </div>
  
<div style="text-align: center"> 
$$
        \begin{equation}
                {\dfrac{d}{dt}n_{r} = -2 \left(1 + j\right)n_r + 2pm_r - 2g^{2}\mu_{r}^2\left(2n_r + m_r\right)} {- j\left(m_r + n_r\right)^{2}},
        \end{equation}
$$
 </div>
 
<div style="text-align: center"> 
$$ 
        \begin{equation}
                {\dfrac{d}{dt}m_{r} = -2 \left(1 + j\right)m_r + 2p n_r - 2g^{2}\mu_{r}^{2}\left(2m_r + n_r\right) + } p\\ -  g^{2}\left(\mu_{r}^{2} + m_r\right) - j\left(m_r + n_r\right)^{2} .
        \end{equation}
$$
 </div>

**Related Publications** <br>

[CAC-CIM-CDP](https://doi.org/10.1038/s41598-023-43364-8) <br>
[Related code here](/404.html)

<!-- <img src="/images/gacs_Figure_6.png" alt="gacs" style="height: 500px; width:300px;"/> -->