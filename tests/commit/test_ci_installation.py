from unittest import TestCase

import unifyml
from unifyml.backend._backend import init_installed_backends


class TestCIInstallation(TestCase):

    def test_detect_tf_torch_jax(self):
        backends = init_installed_backends()
        names = [b.name for b in backends]
        self.assertIn('PyTorch', names)
        self.assertIn('Jax', names)
        self.assertIn('TensorFlow', names)

    def test_verify(self):
        unifyml.verify()