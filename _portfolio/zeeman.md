---
title: "Coherent Ising Machines with Artificial Zeemans"
excerpt: "Exploring an effective implementation scheme for artificial Zeeman terms in an Ising Hamiltonian for CIM simulations"
collection: portfolio
---

<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>

<div style="text-align: justify"> Mathematically, combinatorial optimisation problems can be represented using an Ising model combined with a Zeeman term. However, soft-spin-based computing architectures like Coherent Ising Machines (CIMs) and Simulated Bifurcation Machines (SBMs) have difficulty realising Zeeman terms because of the size mismatch between the linear and quadratic terms in the Ising Hamiltonians. The objective of this project is to investigate if the Chaotic Amplitude Control (CAC) method can be used to simulate artificial Zeeman terms effectively on a CIM. </div> <br>

**Method Outline**

The Ising Hamiltonian, including Zeeman term, can be expressed as follows.

<div style="text-align: center"> 
$$
        \begin{equation}
        \label{IsingHamiltonian}
                H = -  \dfrac{1}{2}\sum_{r=1}^N\sum_{r'=1}^NJ_{rr'}\sigma_r \sigma_{r'} - {\zeta}\sum_{r=1}^N h_r\sigma_r .
        \end{equation}
$$
 </div>

<div style="text-align: justify"> 
where $\sigma_r$ represents the Ising spin variable taking either $+1$ or $-1$, and $J_{rr'}$ implies the coupling weight between spins $r$ and $r'$. Here the diagonal entries are set to 0.
The second term in eq. (\ref{IsingHamiltonian}) indicates the external field present for each spin which is generally called the Zeeman term. $\zeta$ is the Zeeman strength adjustment parameter. Using the Ising Hamiltonian definition (eq. (\ref{IsingHamiltonian})), the local field of each Ising spin can be described as follows.   </div> 

<div style="text-align: center"> 
$$
        \begin{equation}
        \label{IsingLocal}
                f_r = \sum_{r'=1 (\neq r)}^N J_{rr'}\sigma_{r'} + {\zeta} h_r .
        \end{equation}
$$
 </div>

<div style="text-align: justify"> 
Eq. (\ref{IsingLocal}) contains two terms, the first of which indicates the interaction term and the second of which indicates the Zeeman term.  </div> 

<div style="text-align: justify"> 
In the conventional case the Ising Hamiltonian, which includes the Zeeman term (eq. (\ref{IsingHamiltonian})), as well as the local field (eq. (\ref{IsingLocal})) for each Ising spin, is defined based on the assumption that each spin variable takes either $+1$ or $-1$. In CIMs, as well as SBMs, the spin amplitudes are continuous values that are different from $\pm 1$, so the interaction term and Zeeman term's contribution to the local field (e.g. for CIMs, eq. (\ref{mfeq4})) depend on the amplitude of the spin variable. As a consequence of the size mismatch between the interaction term and the Zeeman term, Ising machines may produce biased solutions which are inconsistent with the Hamiltonian defined by eq. (\ref{IsingHamiltonian}).  </div> 

**Methods used previously in CIMs to realise the Zeeman term**
 
> **Absolute Mean Amplitude**

<div style="text-align: justify"> 
In the early stages of CIM research, it was suggested that the Zeeman term could be efficiently incorporated into the injection field by scaling it with the absolute mean of the amplitudes of the OPO pulses. </div> 

<div style="text-align: center"> 
$$
        \begin{equation}
        \label{absamp}
            I_{inj,r} = j\left(\sum_{r' = 1}^N J_{rr'}x_{r'}  +  \zeta h_{r}\dfrac{1}{N} \sum_{r}|x_{r}|\right)  .  
        \end{equation}
$$
 </div>

<div style="text-align: justify"> 
Here, $I_{inj,r}$ is the injection field for the OPO pulse $r$. $x_r$ states the normalized in-phase amplitude of the OPO pulse $r$ while   $J_{rr'}$ and $h_{r}$ are the coupling weight and the Zeeman term described above. $\zeta$ is the adjustment parameter for the strength of the Zeeman term. Here $j$ represents the feedback strength. </div> 

> **Auxiliary Spin**

<div style="text-align: justify"> 
In this case, the Zeeman term is incorporated into the two-body interaction term through the introduction of auxiliary spins to be included in a product with the Zeeman term as follows.  </div> 

<div style="text-align: center"> 
$$
        \begin{equation}
        \label{auxamp}
            I_{inj,r} = j\left(\sum_{r' = 1}^N J_{rr'}x_{r'}  +  \zeta h_{r}x_{(N+1)}\right) \rightarrow  j\left(\sum_{r' = 1}^{(N+1)} J_{rr'}x_{r'}\right),\\  \left(r=1,..,N, N+1\right) .
        \end{equation}
$$
 </div>

<div style="text-align: justify"> 
where $x_{N+1}$ is an auxiliary amplitude to match the size of the Zeeman term to the interaction term and to transform the Zeeman term to an additional interaction term. As indicated in eq. (3), the injection field is reformulated only by the interaction term given in $J_{rr'} \in \mathbb{R}^{(N+1) \times (N+1)}$ and $x \in \mathbb{R}^{(N+1)}$. The extended coupling matrix can be constructed by giving additional column and row vectors as $J_{r N+1} = \zeta h_{r}$ and $J_{N+1 r’} = \zeta h_{r’}$, and taking $J_{N+1,N+1}=0$. Currently, CIMs only support two-body interactions, which makes this method effective.  </div> 

**Related Publications** <br>

[GATW & GAPP](https://doi.org/10.1038/s42005-022-00927-x)
[MFZ-CIM](https://doi.org/10.1063/5.0176248) <br>
[Related code here](/404.html)
<!-- <img src="/images/gac.webp" alt="gac" style="height: 500px; width:300px;"/><br/>
<img src="/images/mfz_Figure_1.png" alt="mfz" style="height: 500px; width:300px;"/> -->

