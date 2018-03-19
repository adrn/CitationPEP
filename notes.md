# Notes

* See thread: https://twitter.com/jakevdp/status/524329573580697600
* Discussion here: https://github.com/scikit-learn/scikit-learn/pull/3789

### Packages that use `__bibtex__`

(many hits in GitHub search, but mostly duplicates)

* [Matplotlib](https://github.com/matplotlib/matplotlib/pull/6204)
* [Emcee](https://github.com/dfm/emcee/blob/70690ae872b929cb3ad8f90db928e82104cb9517/emcee/__init__.py)
* [astropy](https://github.com/astropy/astropy)

### Packages that use `__citation__`:

[(40 hits in GitHub search)](https://github.com/search?utf8=%E2%9C%93&q=__citation__+extension%3Apy+language%3APython+language%3APython&type=Code&ref=advsearch&l=Python&l=Python)

* [astroML](https://github.com/astroML/astroML/blob/0287fe00c429b28b3ddf52435a32543f43246349/astroML/__init__.py)
* [PeakPro](https://github.com/SHDShim/PeakPo)
* [instamatic](https://github.com/stefsmeets/instamatic/blob/b741a5d119f16f79a94adb9c96dfb4b48fafb784/instamatic/version.py)

# API

This is just an initial proposal, meant to be discussed and edited. You can also
run demos for each of the cases listed below from within the `scripts/`
directory by doing:

    % python demo.py 1
    % python demo.py 2
    % python demo.py 3

* Calling `citation` with a string will use `importlib` to try to import the
  package and will just return the contents of `__citation__`. For example:

    ```python
    >>> print(citation('astroML'))
    @INPROCEEDINGS{astroML,
     author={{Vanderplas}, J.T. and {Connolly}, A.J.
             and {Ivezi{'c}}, { Z}. and {Gray}, A.},
     booktitle={Conference on Intelligent Data Understanding (CIDU)},
     title={Introduction to astroML: Machine learning for astrophysics},
     month={Oct.},
     pages={47 -54},
     doi={10.1109/CIDU.2012.6382200},
     year={2012}
    }
    >>> import astroML
    >>> citation('astroML') == astroML.__citation__
    True
    ```

* Calling `citation` with a package or module just returned `__citation__`:

    ```python
    >>> import astroML
    >>> print(citation(astroML))
    @INPROCEEDINGS{astroML,
     author={{Vanderplas}, J.T. and {Connolly}, A.J.
             and {Ivezi{'c}}, { Z}. and {Gray}, A.},
     booktitle={Conference on Intelligent Data Understanding (CIDU)},
     title={Introduction to astroML: Machine learning for astrophysics},
     month={Oct.},
     pages={47 -54},
     doi={10.1109/CIDU.2012.6382200},
     year={2012}
    }
    ```

* Calling `citation` with no arguments finds all imported modules and returns a
  dictionary containing `__citation__` contents for all:

    ```python
    >>> import astroML
    >>> import citationpep
    >>> for pkg, cite in citation().items():
    ...     print(pkg, cite)
    ...
    astroML @INPROCEEDINGS{astroML,
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
    citationpep This is a demo citation!
    ```
