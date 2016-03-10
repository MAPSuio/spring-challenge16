#!/usr/bin/env sh

if [[ ! $# -eq 1 ]] ; then
    echo "Usage: $0 path"
    exit 0
fi

# Dessverre klarer ikke grep å telle antall forekomster i
# binærfiler. Men det fungerer i dette tilfellet fordi det står i
# oppgaveteksten av "crap" ikke dukker opp i noen av binærfilene.

grep -ior $1 -e "crap" | wc -l
