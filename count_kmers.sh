#! /bin/sh

FILES=./sequences/*
for f in $FILES; do
	NAME=$(echo "$f" | cut -d'/' -f3)
	if [ ! -f "./kmer_cnts/$NAME.jf" ]; then
		jellyfish count -o "./kmer_cnts/$NAME.jf" -m 30 -s 100M -t 8 -C "$f"
	fi
done
