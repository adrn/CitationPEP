# CitationPEP

Proposing a new guideline for defining software citations, and a new builtin function for retrieving citations.

For example:

```python
>>> import astropy
>>> astropy.__citation__
http://dx.doi.org/10.1051/0004-6361/201322068
>>> citation(astropy)
http://dx.doi.org/10.1051/0004-6361/201322068
```

## Authors

* Adrian Price-Whelan ([@adrn](https://github.com/adrn))
* Kelle Cruz ([@kelle](https://github.com/kelle))
* Tom Robitaille ([@astrofrog](https://github.com/astrofrog))
* Arfon Smith ([@arfon](https://github.com/arfon))
* Erik Tollerud ([@eteq](https://github.com/eteq))
* Jake Vanderplas ([@jakevdp](https://github.com/jakevdp))
