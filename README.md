# CitationPEP

Proposing a new guideline for defining software citations, and a new builtin function for retrieving citations.

For example:

```
>>> import astropy
>>> astropy.__citation__
http://dx.doi.org/10.1051/0004-6361/201322068
>>> citation(astropy)
http://dx.doi.org/10.1051/0004-6361/201322068
```
