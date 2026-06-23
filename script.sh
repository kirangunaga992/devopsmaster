#!/bin/bash
for i in linux kubernetes jenkins docker git terraform
do
	mkdir $i
	touch $i/notes.md
done
