pipenv run sphinx-build -a -b html source build
pipenv run sphinx-autobuild -b html --watch "../pygame_colliders" --open-browser --delay 1 source build
