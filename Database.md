---
title: Tracker Offline Database
layout: default
---

<h2>New Tags for Virgin Raw data - 31/8/2009</h2>

Runs 111664 and 111673 are in deconvolution mode, Run 111753 is in peak mode. You can see the results of the condDB Monitoring in the following directories:
<ul>
<li> <a href="Database/NoisesMonitor">Noises</a> </li>
<li> <a href="Database/PedestalMonitor">Pedestals</a> </li>
</ul>

<h2> DCS Trend Plot Development - 1/3/2011</h2>

To check the status of the DCS database tag I developed an interactive plot on a web page. It is written in javascript,
it is based on the <a href="http://code.google.com/p/flot/">Flot</a> package and uses jQuery. A first working example can be found here: <a href="SiStrip/DCSTrend.html"><font color="red">DCSTrend</font></a>.

It accepts a json file containing the values and to produce this file a python script is used. This python script
must be run on top of the CheckAllIOVs.py macro that I wrote during the development of the DCS O2O to check the
content of the DCS tags in the offline database.

<font size="3" color="red"><b>The official one is now in place at this page: <a href="https://test-stripdbmonitor.web.cern.ch/test-stripdbmonitor/DCSTrend/index.html">https://test-stripdbmonitor.web.cern.ch/test-stripdbmonitor/DCSTrend/index.html</a>. It is updated automatically by a cron running every hour.</b></font>

<h4> Motivation </h4>
The DCS information is going to be used in the prompt reconstruction in 2011. This requires the prompt calibration loop
to be in place (48 hours delay from run start).
It is important to check that the DCS information is available before the start of the prompt reconstruction, otherwise
the status might be inconsistent: we might end up masking the Tracker if the last IOV before the start was Tracker full
OFF.
To avoid this, three checks are to be done:
<ol>
  
  <li> Check that the cron has run at least once after the run has ended:
    <ul>
      <li> go to this page: <a href="http://cms-conddb.cern.ch/">conddb</a> and select "PopCon RecentActivities"
        <li> in the search box put "DetVOff" to remove updates from other tags and the first one in the list will
          be the last update of the DCS O2O cron.
          <li> The EXEC TIME will tell you the time when the cron started.
          <li> The Last Since will tell you the last IOV when it started.
          <li> The last IOV is in long long format, to get the human readable date you can use python. In the python interpreter just do:
            <ul>
              <li> import time
              <li> time.ctime(5569159693323438656>>32)
            </ul>
        </ul>
    
  <li> Check the content of the database:
    <ul>
      <li> look at the trend plot and see that it is consistent with what actually happened
        </ul>
    
  <li> Check that the PVSS database update time is recent
    <ul>
      <li> The PVSS database should be always up to date (can be few seconds back, not more)
        <li> If there is more than a few seconds discrepancy it must be reported immediately
      </ul>
</ol>

<strong>Update 15/06/2011</strong>

Changed the DCSTrend.py script to force the jQuery visualization to be in the correct order. A 1millisecond is added to each first IOV so that it always appears correctly after the end of the previous IOV (which is at the same time otherwise causing the ambiguity in the visualization). When zooming in (a lot) the points will appear slightly shifted. This is not an exact representation, but it is within the precision, at the second level. In any case, the popup message will always give the IOV with precision to the second level, so it that information is correct.

<h2> Select events with high percentage of FED errors - 8/3/2011</h2>

A few events were identified where the full Tracker is in error. As of this date it is not yet clear what is the
source of these events. They manifest as cases where all the FEDs of the SiStrip Tracker give an error and
consequently no digis and then no tracks are reconstructed.

To save these events in the error stream automatically produced by the reconstruction I added a LogError to the
SiStripRawToDigiUnpacker which reads the raw data and produces the list of bad detIds to be used by the tracking.<br>
The LogError is written when the number of fibers in error is greater than a configurable threshold (and different
from 0). The threshold is set to 7174 which is 95% of the number of fibers in the subdetector with the smallest
number of fibers (which is TEC, given that: Full TRK = 36392; TIB = 6984; TID = 2208; TOB = 12096; TEC = 15104 and
TIB/TID go together).

The modified package is <a href="http://cmslxr.fnal.gov/lxr/source/EventFilter/SiStripRawToDigi/">EventFilter/SiStripRawToDigi</a> and as
a consquence two additional modules required changes: SiStripDigiToRawModule, SiStripRawToClustersLazyUnpacker.
The first one was changed to read the parameter configuring the threshold from cfg. The parameter is called
ErrorThreshold and is defined in the SiStripDigis_cfi.py in the same package. The second one instead sets this
parameter automatically to 0 as it only uses the unpacker to dump the raw data to std::out if required.

The modification was tested in CMSSW_3_9_7 reconstructing the events with the above errors. A skim was produced:
<code>
/castor/cern.ch/user/m/mgalanti/nostripevents/nostripevent_run2010b_raw_photon_v1.root
</code>
contaning 29 events and they were verified to all give the error message:
<br>
<code>Total number of errors = 35682</code>
<br>
