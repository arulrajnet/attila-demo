#!/usr/bin/env bash
set -ex

##
## Create some aliases
##
echo 'alias ll="ls -alF"' >> $HOME/.bashrc

WORKSPACE_DIR=/workspace

# Now install all dependencies
pip install .

chmod 600 -R ~/.ssh

echo "Done!"
