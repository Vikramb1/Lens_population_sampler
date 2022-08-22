===========
VDF sampler
===========


.. image:: https://img.shields.io/pypi/v/lens_population_sampler.svg
        :target: https://pypi.org/project/lens-population-sampler/

.. image:: https://img.shields.io/travis/vikramb1/lens-population-sampler.svg
        :target: https://travis-ci.com/vikramb1/lens-population-sampler
        
.. image:: https://readthedocs.org/projects/lens-population-sampler/badge/?version=latest
        :target: https://lens-population-sampler.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Python package to sample from a velocity dispersion function of ellictical galaxies in the local universe


* Free software: MIT license
* Documentation: https://lens-population-sampler.readthedocs.io.

Example
-------

.. code-block:: python

        # import package
        from lens_population_sampler import vdf_sampler

        # produces 1000 samples with velocity dispersion between 100 and 200. The approximation uses 500 bins.
        samples = vdf_sampler.sample_vdf(100, 200, resolution = 500, size = 1000)
        print(samples)

Credits
-------

This package uses the function derived from analysing the velocity dispersions of ellictical galaxies using the Sloan Digital Sky Survey in (`Choi, Park, & Vogeley (2007)  <https://ui.adsabs.harvard.edu/abs/2007ApJ...658..884C/abstract>`_).  

This package uses a modified class from hierArc_, created by `Simon Birrer`_.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _hierArc: https://github.com/sibirrer/hierArc
.. _`Simon Birrer`: https://github.com/sibirrer
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
