#!/usr/bin/env python

"""Tests for `lens_population_sampler` package."""


import unittest
from click.testing import CliRunner

from lens_population_sampler import vdf_sampler
from lens_population_sampler import cli
from skypy.galaxies.redshift import redshifts_from_comoving_density
from astropy.cosmology import LambdaCDM
from astropy import units
import matplotlib.pyplot as plt
import numpy as np

class TestVdf_sampler(unittest.TestCase):
    """Tests for `lens_population_sampler` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'vdf_sampler.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_sample_drawing(self):
        samples = vdf_sampler.sample_vdf(100, 200, size = 1000)

        # check that samples are within bounds
        self.assertEqual(np.sum((100 <= samples) & (samples <= 200)), 1000)
    
    def test_volume_rendering(self):
        # set up cosmology
        H0 = 75
        Om = 0.5
        Ol = 0.5
        x_min = 100
        x_max = 200
        cosmo = LambdaCDM(H0=H0, Om0=Om, Ode0=Ol)
        redshift = np.arange(0.0, 2.001, 0.5)

        # use the function defined above to compute the integral between 100 and 105
        density = vdf_sampler.compute_integral_vdf(x_min,x_max)
        # define area of the sky to be considered
        sky_area = 0.01 * units.steradian

        # sample galaxies over full sky without Poisson noise
        z_gal = redshifts_from_comoving_density(redshift, density, sky_area, cosmo, noise=False)
        sigma_v = vdf_sampler.sample_vdf(x_min, x_max, size = z_gal.shape[0])
        self.assertTrue(np.sum((0 <= z_gal) & (z_gal <= 2)), z_gal.shape[0])
