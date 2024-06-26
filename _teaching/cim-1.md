<!-- ---
title: "Coherent Ising Machines"
collection: teaching
type: "Research"
permalink: /teaching/cim-1
# venue: "University 1, Department"
date: 2024-01-009
location: "Tokyo, Japan"
---

This post introduces the basic concept of the Coherent Ising Machine (CIM)

What is a the Coherent Ising Machine?
======

In recent years, Quantum Computing has gained global attention because of the exponential speedup which can be achieved compared to classical computers on solving combinatorial optimisation problems. These problems are a special group of problems called NP-hard, that are difficult to solve in polynomial time. Several different quantum architectures and simulators have been proposed around the world to tackle these problems using different techniques such as superconducting qubits \cite{dwave1, super1}, trapped-ion \cite{ion1, ion2}, etc. Coherent Ising machine (CIM) is a system of optical parametric oscillators (OPOs), where OPO oscillations that are strong enough to exceed the threshold limit can be interpreted as an optimum answer for a given Hamiltonian \cite{Yamamoto2}.

With the use of a Phase-sensitive amplifier (PSA) with an optical cavity shown in Fig:\ref{FigMFBCIM}, a coherent state can be achieved in the CIM. This gives the freedom to consider the spin-up-state as 0 and spin-down-state as $\pi$ and the overall state as an Ising spin model. The $J_{ij}$ matrix or the mutual coupling matrix is created using a mutual injection field. Then the mathematical model of the CIM which is approximately described by the following c-number Langevin equations can be obtained \cite{Yamamoto1, Yamamoto2}.

\begin{tcolorbox}
\begin{equation}
\label{initCIM}
\begin{split}
        \frac{d}{dt}c_i = (-1 + p - P_i )c_i + N_c + \sum_{j=1, j \neq i} J_{ij}c_j\\\\
        \frac{d}{dt}s_i = (-1 - p - P_i )s_i + N_s + \sum_{j=1, j \neq i} J_{ij}s_j
\end{split}
\end{equation}
\end{tcolorbox}

In (\ref{initCIM}), $c$ and $s$ corresponds to the in-phase and quadrature-phase amplitudes of the system. Normalised pump rate is indicated by \emph{p} where $P_i = c_i^2 + s_i^2$. In the equation, the in-phase amplitudes get amplified and quadrature-phase amplitudes get de-amplified by the pump. Because of this only in-phase amplitudes survives to go beyond the oscillation threshold. \cite{Takesue}

\begin{figure}[!ht]
    \centering
    \includegraphics[scale=0.4]{coherentstate.png}
    \caption{CIM States \cite{cim1}}
    \medskip
    \footnotesize
    {During the transition stage from below threshold, which is a squeezed state, when the CIM system reaches the threshold limit, coherent states appear. These bi-stable coherent states in a single OPO can be stated as spin-up and spin-down, otherwise 0 and $\pi$ states.}
    \label{coherentstatel}
\end{figure}
\begin{figure}[!ht]
    \centering
    \includegraphics[scale=0.4]{pitchfork.png}
    \caption{Pitchfork Bifurcation}
    \medskip
    \footnotesize
    {Representation of the pitchfork bifurcation diagram of in-phase amplitudes. Solid lines represent a "stable point", whereas dashed lines represent "unstable".}
    \label{pitchfork}
\end{figure}

\begin{figure}[!ht]
    %\centering
    \includegraphics[scale=0.5]{cim.png}
    \caption{MFB-CIM architecture}
    \medskip
    \footnotesize
    {Coherent Ising Machine (CIM) consists of a Degenerated Optical Parametric Oscillator network with a Measurement-Feedback module. The pump pulses are injected into the main cavity by a second harmonic generation (SHG). For generating optical parametric oscillations, Periodically Poled Lithium Niobate (PPLN), which is a highly efficient optical parametric medium, is used.  If the round-trip time of the ring cavity is correctly adjusted to \textit{N} times the pump pulse interval, \textit{N} independent DOPO pulses can simultaneously coexist inside the cavity. Each of these pulses is either in the $0$-phase state or in the $\pi$-phase state because of the non-linearity of the PPLN. A small portion of the in-phase amplitudes of DOPO pulses are collected by out-coupling it through an output coupler. The measurement is done by using an LO pulse which is directly injected from the pump laser and an optical balanced homodyne detectors. The outputs are converted into digital signals and input to a digital circuit (in this case an FPGA), where the feedback signal is generated.  And then an injection stage creates the optical feedback signal by phase and intensity modulation of local oscillator (LO) pulses and injects it into the cavity. PD: photon-detector; PM: phase modulator; IM: intensity modulator.\cite{Yamamoto1, Yamamoto2, Sasaki}}
    \label{FigMFBCIM}
\end{figure}

%CIM has been a system that is actively being researched to understand how to apply for real-world applications. But the initial physical implementation of the CIM consisted of a significantly small number of DOPO pulses \cite{Yamamoto}. Real-world problems in general is large-scale, requires large number of qubits to simulate. In 2019 Takesue \textit{et al}. proposed a \textit{stable} 2000 DOPO pulse CIM which is called the Large-Scale Coherent Ising Machine (LS-CIM).  LS-CIM enabled researchers to consider variations of CIM to tackle large-scale problems than the initial CIM.

As shown in Fig:\ref{coherentstatel}, above threshold, CIM consists of bi-stable coherent states, $\pi$ and 0, corresponds to spin down and spin up states. This can be stated as a pitchfork bifurcation Fig:\ref{pitchfork}. The second term in (\ref{initCIM}), $\left(N_c = \dfrac{\sqrt{P_i + 0.5}}{A_s}\right)$ and $N_s$ which is, $\left(N_s = \dfrac{\sqrt{P_i + 0.5}}{A_s}\right)$ corresponds to the vacuum fluctuations injected from the external reservoirs and the pump fluctuations coupled into the OPO system via gain saturation. $A_s$ represents the saturation parameter which indicates the nonlinear increase of photon number at OPO threshold. In this thesis we are considering $\dfrac{1}{A_s} = 10^{-7}$ which is closer to the value of experimental CIM (the physical CIM system). 
Inside the cavity, $N$ independent DOPO pulses coexist simultaneously if the round-trip time of the fibre cavity is correctly adjusted to $N$ times the pump pulse interval. The homodyne measurement measures a slight portion of the in-phase amplitudes to create a feedback signal. This feedback signal is created by considering the measurement results from the previous round-trip. In the injection stage, the optical feedback signal is created (using phase and intensity modulation of local oscillator pulses) with the calculated results and injected into the optical cavity by an input coupler.

To derive (\ref{initCIM}), here the Hamiltonian for the whole OPO system was considered only focusing on the observation noise following the recipe suggested by Wiseman and Milburn \cite{wisemen1, wisemen2, wisemen3}. The OPOs are coupled via the measurement feedback in the system. Then by taking the Ito form and using the ensemble average for observation noise, the master equation for the system (for non-conditioned state operators) can be derived. Here we consider the Wigner representation \cite{wisemen5} (a quasi-probability distribution function which results in Fokker-Plank equations when applied to the master equation) of the state operators in the master equation mentioned earlier, and applying the Ito rule \cite{wisemen5}, the mutually correlated noise in OPOs can be obtained.  The injection fields for the phase components (in-phase and quadrature-phase) are stated in the third components in (\ref{initCIM}).  -->