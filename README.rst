======
Carsus
======

Carsus is a package to manage atomic datasets. It can read data from a variety of
sources and output them to file formats readable by radiative transfer codes.

.. image:: https://codecov.io/gh/tardis-sn/carsus/branch/master/graph/badge.svg?token=wzEPZc4JYv
    :target: https://codecov.io/gh/tardis-sn/carsus
    :alt: Coverage

.. image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
    :target: http://www.astropy.org
    :alt: Powered by Astropy Badge

.. image:: https://github.com/tardis-sn/carsus/actions/workflows/docs-build.yml/badge.svg
    :target: https://tardis-sn.github.io/carsus
    :alt: docs

.. image:: https://github.com/tardis-sn/carsus/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/tardis-sn/carsus/actions/workflows/tests.yml
    :alt: tests

.. image:: https://badges.gitter.im/Join%20Chat.svg
    :target: https://gitter.im/tardis-sn/carsus
    :alt: Join Chat
|

.. _carsuscredits:

******************************
Credits & Publication Policies
******************************

|DOI_BADGE|

We provide CARSUS as a free, open-source tool. If you are using it, please
adhere to a few policies and acknowledge the CARSUS Team.

Publication Policies
====================

If you use CARSUS for any publications or presentations, please acknowledge
it. Please cite `Kerzendorf et al. 2021 <https://ui.adsabs.harvard.edu/abs/2021ascl.soft03021K>`_ in the text and add the
following paragraph to the Acknowledgement section:

.. parsed-literal::

   This research made use of \\textsc{carsus}, a community-developed atomic data management
    tool for astrophysical modeling \\citep{|CITATION|}. The development of
    \\textsc{carsus} received support from the Google Summer of Code initiative and contributions
    from the open-source community. \\textsc{carsus} makes extensive use of Astropy and Pandas.

Citation
========

If you publish work that uses CARSUS, please include the following BibTeX entry:

.. code-block:: bibtex

    @software{2021ascl.soft03021K,
       author = {{Kerzendorf}, Wolfgang and {Mishin}, Mikhail and {P{\'a}ssaro}, Ezequiel and
                 {Eweis}, Youssef and {Selsing}, Jonatan and {Sim}, Stuart},
        title = "{Carsus: Atomic database for astronomy}",
 howpublished = {Astrophysics Source Code Library, record ascl:2103.021},
         year = 2021,
        month = mar,
          eid = {ascl:2103.021},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021ascl.soft03021K},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
    }

.. |CITATION| replace:: misha_mishin_2024_14546688

.. |DOI_BADGE| image:: https://img.shields.io/badge/DOI-10.5281/zenodo.misha_mishin_2024_14546688-blue
                 :target: https://doi.org/10.5281/zenodo.misha_mishin_2024_14546688

.. code-block:: bibtex

    @software{misha_mishin_2024_14546688,
      author       = {Misha Mishin and
                      Ezequiel Pássaro and
                      yeganer and
                      Joshua Shields and
                      Wolfgang Kerzendorf and
                      Atharva Arya and
                      Andrew and
                      Shreyas Singh and
                      Christian Vogl and
                      Shikha Rathi and
                      Youssef15015 and
                      Jonatan Selsing and
                      ssim and
                      Andreas Flörs and
                      Ayushi Daksh and
                      KasukabeDefenceForce and
                      Laureano Martinez and
                      Luke Shingles and
                      The Gitter Badger and
                      Atul Kumar},
      title        = {tardis-sn/carsus: Carsus v2024.12.23},
      month        = dec,
      year         = 2024,
      publisher    = {Zenodo},
      version      = {release-2024.12.23},
      doi          = {10.5281/zenodo.14546688},
      url          = {https://doi.org/10.5281/zenodo.14546688},
    }

*******
License
*******

.. image:: https://img.shields.io/conda/l/conda-forge/tardis-sn
    :target: https://github.com/tardis-sn/tardis/blob/master/licenses/LICENSE.rst

.. image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
    :target: http://www.astropy.org
|

This project is Copyright (c) TARDIS Collaboration and licensed under
the terms of the BSD 3-Clause license. This package is based upon
the `Astropy package template <https://github.com/astropy/package-template>`_
which is licensed under the BSD 3-clause license. See the licenses folder for
more information.

