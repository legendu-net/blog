#!/bin/bash

echo '$0: '$0
echo '$(readlink -f $0): '$(readlink -f $0)
echo '${BASH_SOURCE[0]}: '${BASH_SOURCE[0]}
echo ' $(readlink -f ${BASH_SOURCE[0]}): '$(readlink -f ${BASH_SOURCE[0]})