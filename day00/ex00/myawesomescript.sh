#!/bin/sh
curl -Is $1 | grep Location | cut -d ' ' -f2
