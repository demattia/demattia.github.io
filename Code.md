---
title: Code
layout: default
---

This page contains some code snippets, classes or programs that might be of general use.

<strong>Root Macros</strong>

A collection of macros to perform common tasks. The full list and explaination is <a href="RootMacros.html">here</a>.
<strong>Efficiency Object</strong>

A generic N dimensional matrix to store efficiencies. Allows for projections on any number of variables and rebinnings. The object stores numerator and denominator and only computes the ration when asked for the efficiency values.
Internally it uses array rather than vectors. They are dynamically allocated and garbage collecting is ensured by the use of boost::shared_array.
The matrix is represented by a linear array and there are methods to convert a set of indexes to the index in the linear representation.
Recursivity is used extensively to deal with the unknown number of dimensions and sizes.
More details are given in this page: <a href="EfficiencyObject.html">Efficiency</a>.

<h4> Recursive class to compute all possible unordered combinations of k elements out of N </h4>
This can be useful for example to compute the alpha_t variable (see the VBF Higgs analysis <a href=VBFHiggs.html>page</a>)

Requires root.

<a href=code/Recursive.cpp>Recursive.cpp</a>

<h4> Multilayer perceptron </h4>
This is a simple multilayer perceptron in C++. It learns the XOR by default and can be easily extended
to other inputs. The learning algorithm is back propagation. <br>
It also produces some root histograms showing the error as a function of the iteration. <br>
To compile just do "./configure" and then "make" (of course you need root installed).

<a href=code/NN_root.zip>NN_root.zip</a>

<h4> Autotools to link root in a standalone executable </h4>
A small package preparing an area to compile and link root classes in a standalone executable. <br>
<ul>
  <li> Checkout the autotool package from my usercode area: <code>cvs co UserCode/DeMattia/AutomakeRoot</code></li>
  <li> Run the script Newpackage.sh passing the name of the executable you want to create</li>
</ul>
It will setup the code and compile it in the src subdirectory. To recompile after any changes are made
to the .cpp file in src use "make".
