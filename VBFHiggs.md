---
title: Vector Boson Fusion Higgs
layout: default
---

<h2>Description of the channel</h2>
Higgs boson produced by fusion of vector bosons emitted by the two incoming partons. The two
partons have small transverse momentum and hadronize producing forward jets (tag jets). The
signal is H->ZZ->mumubb.

<h2>Analysis strategy</h2>
Use a multivariate approach based on boosted decision trees (BDT). The TMVA package is used
for the training and testing of the algorithm and two distinct BDTs are used.
<p>
The first BDT is used to select the tag jets and the second to select the hadronic Z jets
(or give the final significance, still to be seen).

<h2>Training of the final BDT</h2>
The second BDT receives in input the result of the first BDT as well as the most discriminating
variables available. A first look at a full set of variables to decide what are the most discriminating
ones to be used is shown here:
<p>
Described in:
<a href="VBFHiggs/HadZBDTinputVariables.pdf">HadZBDTinputVariables.pdf</a>
</p>

<h2>Selection of the most discriminating variables</h2>
<p>
A subset of the most discriminating and less correlated variables is selected:
<ul>
<li> H_T </li>
<li> output of the first BDT </li>
<li> Pt of the second jet assigned to the hadronic Z </li>
<li> Pt of the leptonic Z </li>
<li> mass of the hadronic Z </li>
<li> mass of the leptonic Z </li>
<li> Delta R between the two Zs </li>
</ul>
More details are given here:
<a href="VBFHiggs/Training.pdf">Training.pdf</a>
</p>
