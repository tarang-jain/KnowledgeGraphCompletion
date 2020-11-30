#!/usr/bin/env bash

ALL_OCC_PHASE=all_occurence_phases_list
OCC_PHASE_SUBSTR='Phase of Operation:'
for f in */*/*; do
  while IFS= read -r line; do
    if [[ "$line" == *"$OCC_PHASE_SUBSTR"* ]]; then
      echo $line>>ALL_OCC_PHASE
    fi
  done < "$f"
done
