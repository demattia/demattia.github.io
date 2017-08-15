#!/bin/bash

runList=( "111664" "111673" "111753" )
# runList=( "111664" "111753" )

for run in ${runList[@]}; do
    echo $run
    mkdir $run
    cat SiStripPedestalsMonitoring_cfg.py | sed -e "s/RUNNUMBER/${run}/g" > ${run}/SiStripPedestalsMonitoring_${run}_cfg.py
    cd ${run}
    cmsRun SiStripPedestalsMonitoring_${run}_cfg.py > log_${run}
    cd -
done
