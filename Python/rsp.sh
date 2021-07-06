#!/bin/bash
targetZone=$(aws route53 list-hosted-zones)

for zone in fringe2 fringe3 fringe4 fringe5 ai angelfish avc bb8 cdxx cheezeforce docker doublebrown dsrpt ff gotg growth hakuna lcfc2016 mint mobile nala navigation reporting2 sb slabs soa thunderbirds tne
do

thisZone=$(echo $targetZone | jq ".HostedZones[] | select(.Name==\"branch.$zone.abc-test.com.\") | .Id" | xargs)
sets="$(aws route53 list-resource-record-sets --hosted-zone-id $thisZone | jq -c '.ResourceRecordSets[]')"

if [[ $sets == *"branch-wildcard"* ]]; then
        echo "$zone,false"
else
        echo "$zone,true"
fi

done