#!/usr/bin/bash

RUNS=1000
FILENAMES=( ml mm gaps mvue )

rm -rf data
rm -rf figures
mkdir data
mkdir figures

# Create empty files
for name in ${FILENAMES[@]}; do
	rm -f data/${name}.txt
done

# Run it for the different Ns and separate the results
for N in {10..5000..200}; do
	output=$( ./SIM T $N $RANDOM $RUNS )

	for name in ${FILENAMES[@]}; do
		my_output=$( echo "$output" | grep OUTPUT | grep ":${name}:" | awk '{print $3,$4}' )
		echo $N $my_output >> data/${name}.txt
	done
done

for name in ${FILENAMES[@]}; do
	python generate_plots.py $name
done