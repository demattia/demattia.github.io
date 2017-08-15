---
title: "Efficiency Object: linear representation of N-dimensional matrix"
layout: default
---

<p>The full code is here: <a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/DeMattia/DisplacedVertex/Analysis/TrackingEfficiencyFromCosmics/interface/Efficiency.h?view=markup">Efficiency.h</a>.<br>
  It compiles and works in CMSSW, but the only dependencies are from boost. The class can be easily exported and used in a standalone C++ executable as needed.</p>
<p>What follows is an explaination of the crucial parts.</p>
<p><strong>Compute the index of a linear representation of a matrix with a recursive function.</strong></p>
Given a N dimensional matrix where each dimension has its own number of elements it is useful to have a linear representation of it so that the number of dimensions can be dynamically changed.<br />
  One way of doing this is by using recursion.
<p>The total number of elements in the matrix is simply the product of the sizes of all dimensions: <em>S = Prod(s_i) with i=1...N</em></p>
<p>If we denote with “<em>i</em>” the index running from <em>1</em> to <em>N</em> and given “<em>x_i</em>” as the i-th index in the matrix, the index <em>S</em> of the element given by the vector of <em>x_i</em> is:</p>
<p><em>I = x_i + s_i*(x_(i-1) + size(x_(i-1))*(...))</em></p>
<p>This index can be computed with a recursive function:</p>
<code>
unsigned int linearIndex(unsigned int i, unsigned int previous) { <br />
&nbsp; if( i&lt; N ) return( linearIndex(i+1, x_i + size(x_i)*previous) );<br />
&nbsp; return (x_i + size(x_i)*previous);<br />
}
</code>
<p>by calling it with the first element:<br />
</p>
<p><code>linearIndex(1, 0)<br />
  </code>  </p>
<p>it will return the <em>I</em> of the linearized representation.</p>
<p>This defines the order of the variables. The <em>i=1</em> is the most external variable, this means that it must be the first also in any loop.</p>
<p><strong>Initialization</strong></p>
<p>Fill the array (or vector) from 0 to S.</p>
<p><strong>N-k dimensional projections</strong></p>
<p>The N dimensions are good to store the data, but sometimes there can be a need to visualize them or to reduce some of the dimensions.<br />
  Selecting the k dimensions that must be kept, a new array of size <em>Prod(s_i)</em> is created, where the product is now only on the k dimensions, or if you want, the other dimensions have sizes set to 0.</p>
<p>The values of the (N-k) variables must be collapsed into the remaining k.</p>
<p>The important thing is to compute indexes from the index “<em>L</em>” in the linear representation.</p>
<p>Starting from the first variable its index can be computed as:</p>
<p><code>int(L/size(N-1))<br />
</code> </p>
<p>where <em>size(N-1)</em> is the product of the sizes for all the variables minus the first one.<br />
  Then the remainder of this division can be passed for the computation of the next variable:</p>
<p><code>return(L%size(N-1))<br />
  </code> </p>
<p>and the indexes can be computed recursively stopping at the biggest x among the k selected.<br />
  Note that when the value returned is 0 the computation can be stopped immediately and all the rest of the indexes set to 0.</p>
<p><strong>Filling</strong></p>
<p>When a set of values are passed the corresponding bins need to be found and the counters increased.<br />
  Finding the bins is just a matter of computing:</p>
<p><code>index = (value-min)/bins<br />
  </code> </p>
<p>and</p>
<p><code>if( value &lt; min ) index = 0;</code></p>
<p>Note that this is <strong>not</strong> automatic when using <em>unsigned int</em>, see here: http://stackoverflow.com/questions/50605/signed-to-unsigned-conversion-in-c-is-it-always-safe.<br />
</p>
<p><code>if( index &gt; bins ) index = bins-1;</code></p>
<p>Once the array of indexes is built it can be fed to the linearIndex function to get the index in the linear representation and use it to fill the value.</p>
