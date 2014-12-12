Pynalysis
=========

A framework for macroscopic algorithm runtime analysis.

The standard method of analysing algorithms in the base Python library is via profiling([cProfile](https://docs.python.org/2/library/profile.html#module-cProfile)). Profiling attempts to analyze a given algorithm and its bottlenecks. It provides very fine grain detail on a specific function/program and its execution time on a specific data set over multiple occurences.

This is extremely helpful. But sometimes you want to see not just multiple occurrences with the same data set, but multiple occurrences as the data set grows larger and larger. Potentially one may use **cProfile** to perform this, but it quickly becomes clear that **cProfile** (and other profilers) were not designed to perform this way.

The aim of this framework is to give a higher level view of an algorithm. Ignoring the exact specifics that **cProfile** and other profilers might use, and instead focusing on the growth within a given rate.

IN DEVELOPMENT
