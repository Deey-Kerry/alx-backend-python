#!/usr/bin/env python3
"""Annotate function’s parameters and return values"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """Annotates list of tuples"""
    return [(i, len(i)) for i in lst]
