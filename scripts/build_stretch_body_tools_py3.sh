#! /bin/bash
cd ../python3_tools
rm -rf dist
rm -rf build
rm -rf *.egg-info
python3 setup.py sdist bdist_wheel
python -m twine upload dist/*
echo 'Uploaded stretch_body_tools_py3 to Pypi'