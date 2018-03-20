# CitationPEP

Proposing a new guideline for defining software citations, and a new builtin function for retrieving citations.

Packages can implement whatever they want in `__citation__`: This can be a DOI,
bibtex entry, list of bibtex entries, or custom object.

For example:

```python
>>> import astropy
>>> astropy.__citation__
https://doi.org/10.1051/0004-6361/201322068
>>> citation(astropy)
https://doi.org/10.1051/0004-6361/201322068
```

Calling `citation()` with no argument returns the citations of all imported
modules as a dictionary keyed by the package name:
```python
>>> import astroML
>>> citations = citation()
>>> print(citations['astroML'])
@INPROCEEDINGS{astroML,
 author={{Vanderplas}, J.T. and {Connolly}, A.J.
         and {Ivezi{'c}}, {
                            Z}. and {Gray}, A.},
 booktitle={Conference on Intelligent Data Understanding (CIDU)},
 title={Introduction to astroML: Machine learning for astrophysics},
 month={Oct.},
 pages={47 -54},
 doi={10.1109/CIDU.2012.6382200},
 year={2012}
}
>>> print(citations['citationpep']) # included as an example
This is a demo citation! See https://github.com/adrn/CitationPEP/blob/master/citationpep/__init__.py
```

See [the NOTES](https://github.com/adrn/CitationPEP/blob/master/NOTES.md) for
more information.

## Authors

* Adrian Price-Whelan ([@adrn](https://github.com/adrn))
* Kelle Cruz ([@kelle](https://github.com/kelle))
* Tom Robitaille ([@astrofrog](https://github.com/astrofrog))
* Arfon Smith ([@arfon](https://github.com/arfon))
* Erik Tollerud ([@eteq](https://github.com/eteq))
* Jake Vanderplas ([@jakevdp](https://github.com/jakevdp))
