---
title: Root Macros
layout: default
---

<p>Several root macros are available <a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/DeMattia/RootMacros/">here</a>, what follows is an explaination of each of them.</p>
<p><a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/DeMattia/RootMacros/CompareHistograms.cc?view=markup">CompareHistograms.cc</a></p>
<p>This macro takes two histogram files and compares them.<br>
  It produces a &quot;compared.root&quot; file with the corresponding histograms superimposed (2nd in red).<br>
  It also gives an output with the result of the difference between the corresponding histograms. If everything is zero, the two files<br>
  have the same histograms.<br>
  <em></em></p>
<p>It can be used to make quick comparison and modified easily to draw superimposed plots from two files. It works fine with all TH1, but not with TH2 so they should be excluded from the loop. This can be done with the isInheritsFrom() method already present in the code.</p>
<p><a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/DeMattia/RootMacros/DirectDraw.cc?revision=1.1&view=markup">DirectDraw.cc</a></p>
<p>A simple macro usefull for quick looks at files. Shows how to take a TChain and create the aliases for the branches.</p>
<p><a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/DeMattia/RootMacros/HistoFinder.cc?revision=1.3&view=markup">HistoFinder.cc</a></p>
<p>This macro takes a file and the name of a histogram and looks for a histogram of the same name in all the subdirectories.<br>
  If it finds a match, it returns a pointer to it (but a TObject pointer needs a cast to use it outside), if not returns a null pointer and also does a cout saying it did not find it.<br>
  ATTENTION: if the same name matches more than one histogram in different subdirectories, only the last match will be returned and a warning will be given. In this case, the directory name can be passed to select the correct match.</p>
<p><a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/DeMattia/RootMacros/MergeRates.cc?revision=1.1&view=markup">MergeRates.cc</a> </p>
<p>This macro will add histograms multiplied by their cross-section from a list of root files and write them to a target root file.<br>
  The target file is newly created and must not be identical to one of the source files.</p>
<p><a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/DeMattia/RootMacros/Plots/Draw.cc?revision=1.1&view=markup">Draw.cc</a></p>
<p>This macro loops on all the histograms in a given file and draws them again with some modified settings.<br>
  Useful to restyle quickly all the plots (e.g. with the tdrstyle).</p>
<p><a href="http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/DeMattia/RootMacros/Plots/plot_backup.C?revision=1.1&view=markup">plot_backup.C</a></p>
<p> This macro draws two input histograms superimposed. If bands is passed as true, it will draw the simulation histogram 3 times, emulating error bands.<br>
  It shows how to draw error bands using multiple draws of TH1F.    </p>
