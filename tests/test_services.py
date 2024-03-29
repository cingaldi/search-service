from src import services

import unittest
import pytest


class CategoriesServiceTestCase(unittest.TestCase):

    def test_getBase(self):

        service = services.CategoriesService ()

        result = service.getBase()
        assert result is not None
        assert result[0]["name"] == "Classical Music"

    def test_getFiltered(self):
        service = services.CategoriesService ()

        result = service.getFiltered("Products & Services")
        assert result is not None
        assert result[0]["name"] == "Cars"

class PsychographicsServiceTestCase(unittest.TestCase):

    def test_getBase(self):

        service = services.PsychographicsService ()

        result = service.getBase()

        assert result is not None
        assert result[0]["value"] == "Ads web"

    def test_getFiltered(self):
        service = services.PsychographicsService ()

        result = service.getFiltered("Music")

        assert result is not None
        assert result[0]["value"] == "Background beats"


if __name__ == '__main__':
    unittest.main()