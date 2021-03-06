---
title: Momentum Scale Calibration
layout: default
---

<h2>Improved background model</h2>
<p>
Described in:
<a href="MuScleFit/ImprovedBackgroundModel.pdf">ImprovedBackgroundModel.pdf</a><br>
The scripts and macros to do this are in <code>MuonAnalysis/MomentumScaleCalibration/test/Macros/BackgroundFunctionProducer</code>.<br>
An Instructions.txt file explaines how to use them.
</p>

<h2>J/Psi model - 9/6/2010</h2>
<p>
Described in:
<a href="MuScleFit/JPsiModel.pdf">JPsiModel.pdf</a>
</p>

<h2>Relative cross sections fit - 17/3/2010</h2>
<p>
Described in:
<a href="MuScleFit/RelativeCrossSectionsFit.pdf">RelativeCrossSectionsFit.pdf</a> 
</p>

<h2>Resolution function - 14/8/2009</h2>
<p>
Described in:
<a href="MuScleFit/Resolutions.pdf">Resolutions.pdf</a> 
</p>

<h2>Basic tests of the algorithm - 11/8/2009</h2>
<p>
Described in:
<a href="MuScleFit/BasicTests.pdf">BasicTests.pdf</a> 
</p>

<h2>First complete test 0.1/pb - 13/8/2009</h2>
<p>
The first complete test using all available resonances with events correspoding to 0.1/pb of integrated luminosity. The samples used are the same as
before (rescaled) and the InclusivePPmuX which also has J/Psi but not Psi(2S). Again background and scale fit are performed in this order.
The first time I used the same bias as in the previous tests with neutral initial parameters for the scale fit. The bias is so big that the peaks of
the Upsilons are shifted so that the Upsilon1S ends close to the Upsilon2S mass value and so on. Without background this is not a problem, but with
background the likelihood can use background events for the Upsilon(1S) peak and so it does not find very favorable to shift back the peaks to the
correct position (it finds a secondary minimum). This problem is corrected by giving better initial values (those from the previous test). This is
a rather extreme case, since we do expect biases much, much smaller than that even at startup, nevertheless it is fine to see that the fit is solid,
provided the initial conditions are sound.
<p>
The next test used initial bias with Pt = (1.005 + 0.001*Pt)*Pt. The results are shown here.
</p>
<p>
The results of the background fit:
<p>
<a href="images/ZeroOneInversePb/Background.jpg"><img src="images/ZeroOneInversePb/Background.jpg" width="400" height="300" /></a>
<p>
The results of the scale fit on the various resonances:
</p>
<a href="images/ZeroOneInversePb/JPsi.jpg"><img src="images/ZeroOneInversePb/JPsi.jpg" width="400" height="300" /></a>
<a href="images/ZeroOneInversePb/Upsilons.jpg"><img src="images/ZeroOneInversePb/Upsilons.jpg" width="400" height="300" /></a>
<a href="images/ZeroOneInversePb/Z.jpg"><img src="images/ZeroOneInversePb/Z.jpg" width="400" height="300" /></a>
<p>
JPsi mass vs Eta of the muons and results of the fits (before(left) after(right)):
</p>
<a href="images/ZeroOneInversePb/MassVsEta_JPsi.jpg"><img src="images/ZeroOneInversePb/MassVsEta_JPsi.jpg" width="400" height="300" /></a>
<p>
<a href="images/ZeroOneInversePb/JPsi_MassVsEta_Fits_0.jpg"><img src="images/ZeroOneInversePb/JPsi_MassVsEta_Fits_0.jpg" width="400" height="300"/></a>
<a href="images/ZeroOneInversePb/JPsi_MassVsEta_Fits_2.jpg"><img src="images/ZeroOneInversePb/JPsi_MassVsEta_Fits_2.jpg" width="400" height="300"/></a>
<p>
Mass vs Eta and Pt for the Upsilon1S:
</p>
<a href="images/ZeroOneInversePb/MassVsEta_Upsilon1S.jpg"><img src="images/ZeroOneInversePb/MassVsEta_Upsilon1S.jpg" width="400" height="300" /></a>
<a href="images/ZeroOneInversePb/MassVsPt_Upsilon1S.jpg"><img src="images/ZeroOneInversePb/MassVsPt_Upsilon1S.jpg" width="400" height="300" /></a>
<p>
Reconstructed vs generated Pt of the muons before (left) and after (right) the fit. The one before the fit does not match exactly with the bias, but the fit is only linear while the bias was parabolic and there are biases already in the reconstruction. The final fit shows that the Pt agrees much
better with the generated one, especially considering the low statistic available and the fact that we did not perform any resolution fit.
</p>
<a href="images/ZeroOneInversePb/PtRecoVsGen_0.jpg"><img src="images/ZeroOneInversePb/PtRecoVsGen_0.jpg" width="400" height="300" /></a>
<a href="images/ZeroOneInversePb/PtRecoVsGen_2.jpg"><img src="images/ZeroOneInversePb/PtRecoVsGen_2.jpg" width="400" height="300" /></a>


<h2>Background Fits with new BackgroundHandler - 11/8/2009</h2>
<p>

Introduced a new BackgroundHandler class to handle the background. The mass spectrum is divided in three regions:
<ul>
  <li> - Region 0 includes the Z </li>
  <li> - Region 1 includes Upsilon 1S, 2S and 3S </li>
  <li> - Region 2 includes J/Psi and Psi 2S </li>
</ul>
Each region is centered on the mean value of the mass of corresponding resonances and its width is configurable.
<ul>
  <li> - When the background is fitted the regions are used, parameters for the functions are determined and the fraction of background events. </li>
  <li> - When the background is not fitted the background fractions are rescaled to the resonance windows so that they provide an estimate for
the scale and resolution fits. </li>
</ul>
<p>
Tested the new BackgroundHandler class applying a bias on the muon pt scale and performing a background fit followed by a scale fit on a sample of 53317 InclusivePPmuX events (those include also prompt J/Psi, but not Psi2S) and 3131 Upsilon 1S. The Upsilon 1S correspond to approximately 0.3/pb, while the InclusivePPmuX to about 0.09/pb. The results of the background fits are shown in the following figure.
<p>
<a href="images/BackgroundHandler/BackgroundCheck_JPsiAndUpsilon.jpg"><img src="images/BackgroundHandler/BackgroundCheck_JPsiAndUpsilon.jpg" width="400" height="300" /></a>
<p>
After the background fit we perform a scale fit to recover the bias we introduced. The results are shown in the next figure.
<p>
<a href="images/BackgroundHandler/MassComparison_JPsi.jpg"><img src="images/BackgroundHandler/MassComparison_JPsi.jpg" width="400" height="300" /></a>
<a href="images/BackgroundHandler/MassComparison_Upsilon.jpg"><img src="images/BackgroundHandler/MassComparison_Upsilon.jpg" width="400" height="300" /></a>
<l>
<p>
The background fit gave an estimate of the fraction good enough to allow the scale fit to correct the bias.

<h2>Multiple resonance fits with 1/pb - 11/8/2009</h2>

Test the capacity to fit multiple resonances with a statistic of 1/pb. I use:
<table border="1" frame="box">
  <tbody align="center">
    <tr>
      <td>Resonance</td>
      <td>events in 1/pb</td>
    </tr>
    <tr>
      <td>Z</td>
      <td>1184</td>
    </tr>
    <tr>
      <td>Upsilon 1S</td>
      <td>10873</td>
    </tr>
    <tr>
      <td>Upsilon 2S</td>
      <td>5147</td>
    </tr>
    <tr>
      <td>Upsilon 3S</td>
      <td>1477</td>
    </tr>
  </tbody>
</table>
Of course the uncertainty on the cross sections gives a big error on the expected number of events. I list in the table the exact number of events used in this test, computed as xSection*filtersEfficiencies*IntegratedLuminosity.
<p>
The results are shown in the next two figures:
<p>
<a href="images/OneInversePbSignalOnly/Upsilons.jpg"><img src="images/OneInversePbSignalOnly/Upsilons.jpg" width="400" height="300" /></a>
<a href="images/OneInversePbSignalOnly/Z.jpg"><img src="images/OneInversePbSignalOnly/Z.jpg" width="400" height="300" /></a>
<p>
The normalizations for the reconstructed mass and probability for the Upsilons are different because presently all the pdf are normalized to unity
and have a weight = 1. It is possible to set relative weights consistent with the cross sections, but it is not yet done. It is expected to be a
minor correction, influencing mostly the superposition regions betweent the Upsilons and J/Psi and Psi 2S.
