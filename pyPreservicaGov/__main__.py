"""
pyPreservica.Gov auto run module

author:     James Carr
licence:    Apache License 2.0

"""

from pyPreservicaGov import PreservicaGov

if __name__ == "__main__":
    preservica = PreservicaGov()
    preservica.harvest()
