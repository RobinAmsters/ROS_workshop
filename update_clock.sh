#!/bin/bash

# Get current time since epoch
DATE_PC=`date "+%s"`

# Convert to pi date locale
DATE_PI=`ssh rosberrypi@192.168.42.1 date -d @$DATE_PC`

# Save date in shell script
echo sudo date -s \'"$DATE_PI"\'> pi_updateclock.sh
echo groupRBP >> pi_updateclock.sh

# Set date of pi over SSH with shell script
ssh rosberrypi@192.168.42.1 -tt 'bash -s' < pi_updateclock.sh
