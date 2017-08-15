---
title: IPython Notebook
layout: default
---

The IPython Notebook provides a rich interface where to store notes, code and results. Since it natively runs Python it is a good candidate for analyzing the data collected by the CMS experiment.
For more information on the IPython Notebook see the <a href="http://ipython.org/notebook.html">official page</a>.

<a href="http://root.cern.ch/drupal/">ROOT</a> already provides Python bindings (called Pyroot) and it can be integrated in the notebook.

Furthermore, the CMS software itself (CMSSW) can be integrated in the notebook. FWLite has Python bindings that can be used to streamline the analysis of official dataformats (anything from GEN to PAT).

I integrated the IPython Notebook with ROOT and CMSSW to allow analyzing CMS data from its rich web interface.

The setup has been presented at the CMS Data Analysis School (CMSDAS) in India (November 2013) and in a Hands On Tutorial (HATS) at the LPC in Fermilab (November 20). A TWiki was setup:
<a href="https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolModernToolsForInteractiveAnalysisExercise"></a> and servers were provided to the students.

The collection of notebooks for the exercise is available on github under <a href="https://github.com/demattia/usercode/tree/master/Tutorials/InteractiveAnalysis/Notebooks/HATS_2013">HATS_2013</a> and they cover the following topics (with links to the notebooks on nbviewer):
<ul>
    <li><a href="http://nbviewer.ipython.org/urls/raw.github.com/demattia/usercode/master/Tutorials/InteractiveAnalysis/Notebooks/HATS_2013/Introduction.ipynb">Introduction</a>: introduction to the IPython Notebook (Note: the progress bar will appear as a single line in an IPython Notebook)</li>
    <li><a href="http://nbviewer.ipython.org/urls/raw.github.com/demattia/usercode/master/Tutorials/InteractiveAnalysis/Notebooks/HATS_2013/Pyroot%2520Basics.ipynb">Pyroot basics</a>: provides a selection of basic commands for Pyroot</li>
    <li><a href="http://nbviewer.ipython.org/urls/raw.github.com/demattia/usercode/master/Tutorials/InteractiveAnalysis/Notebooks/HATS_2013/FWLite.ipynb">FWLite</a>: shows how to access EDM information in Pyroot</li>
    <li><a href="http://nbviewer.ipython.org/urls/raw.github.com/demattia/usercode/master/Tutorials/InteractiveAnalysis/Notebooks/HATS_2013/RooFit%2520Basics.ipynb">RooFit basics</a>: shows how to perform fits using RooFit in Pyroot</li>
    <li><a href="http://nbviewer.ipython.org/urls/raw.github.com/demattia/usercode/master/Tutorials/InteractiveAnalysis/Notebooks/HATS_2013/TMVA.ipynb">TMVA</a>: shows how to run training, testing and application of a BDT using TMVA in Pyroot</li>
    <li><a href="http://nbviewer.ipython.org/urls/raw.github.com/demattia/usercode/master/Tutorials/InteractiveAnalysis/Notebooks/HATS_2013/TagAndProbe.ipynb">TagAndProbe</a>: computes trigger efficiency for a dimuon trigger using the tag and probe method. Applies most of what was learned in previous exercises</li>
    <li><a href="http://nbviewer.ipython.org/urls/raw.github.com/demattia/usercode/master/Tutorials/InteractiveAnalysis/Notebooks/HATS_2013/RooStats-CLs.ipynb">RooStats-CLs</a>: shows how to run a CLs exclusion limit calculation using RooStats in Pyroot</li>
    <li><a href="http://nbviewer.ipython.org/urls/raw.github.com/demattia/usercode/master/Tutorials/InteractiveAnalysis/Notebooks/HATS_2013/Parallel.ipynb">Parallel</a>: shows how to parallelize jobs using the parallel cluster feature of IPython in the Notebook</li>
</ul>
