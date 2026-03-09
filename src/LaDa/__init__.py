"""LaDa: Lightweight data access for LAMMPS dump files.

This package exposes a small API for streaming frames from LAMMPS dump files.
"""

from .parsers import iter_dump_frames

__all__ = ["iter_dump_frames"]
