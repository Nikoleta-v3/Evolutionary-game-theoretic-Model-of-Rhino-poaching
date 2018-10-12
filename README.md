# An Evolutionary Game Theoretic Model of Rhino Horn Devaluation

**Authors**: @Nikoleta-v3 @drvinceknight @TamsinELee

This repository for the source code for a paper accepted for publication in
[Ecological Modelling](https://www.journals.elsevier.com/ecological-modelling).

A pre print is available here: https://arxiv.org/abs/1712.07640

## Software

A conda environment specifying all versions of libraries used is given in
`environment.yml`. To create and activate this environment run:

```
$ conda env create -f environment.yml
$ source activate rhino
```

Various functions corresponding to the mathematical definitions given in the
paper are written in `tools.py`. These are fully tested in `test_tools.py`. To
test run:

```
$ python -m unittest test_tools.py
```

All images and numerical simulations for the paper are obtained in
`nbs/main.ipynb`.

The software is released under an MIT license.
