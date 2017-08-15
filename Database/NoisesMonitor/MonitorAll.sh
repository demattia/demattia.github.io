#!/bin/bash

runList=( "111664" "111673" "111753" )
# runList=( "111664" "111753" )

for run in ${runList[@]}; do
    echo $run
    mkdir $run
    cat SiStripNoisesMonitoring_cfg.py | sed -e "s/RUNNUMBER/${run}/g" > ${run}/SiStripNoisesMonitoring_${run}_cfg.py
    cd ${run}
    cmsRun SiStripNoisesMonitoring_${run}_cfg.py > log_${run}
    cd -
done
