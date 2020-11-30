#!/usr/bin/env bash

FACTUAL_INFO_STR='Factual Information'
FACTUAL_INFO_FLAG=false
FACTUAL_INFO_COUNT=0
ALL_REPORT_COUNT=0
for f in {1962..2006}/*/*; do
  if [[ ! -f $f ]]; then
    continue
  fi
  ALL_REPORT_COUNT=$((ALL_REPORT_COUNT+1))
  while IFS= read -r line; do
    if [[ "$line" == *"$FACTUAL_INFO_STR"* ]]; then
      FACTUAL_INFO_FLAG=true
      continue
    fi
    if $FACTUAL_INFO_FLAG; then
      echo $line >> ALL_FAC
      if [[ "$line" != 'Pilot Information' ]]; then
	if [[ "${#line}" -ge 0 ]]; then
	  FACTUAL_INFO_COUNT=$((FACTUAL_INFO_COUNT + 1))
        fi
      fi
      FACTUAL_INFO_FLAG=false
    fi	   
  done < "$f"
done

echo $FACTUAL_INFO_COUNT
echo $ALL_REPORT_COUNT
