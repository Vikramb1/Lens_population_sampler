#!/usr/bin/env python

"""Tests for `vdf_sampler` package."""


import unittest
from click.testing import CliRunner

from vdf_sampler import vdf_sampler
from vdf_sampler import cli
import numpy as np

class TestVdf_sampler(unittest.TestCase):
    """Tests for `vdf_sampler` package."""

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
        self.assertEqual(np.sum((100 <= samples) & (samples <= 200)), 1000)
    