# Frog catching Insects Problem #

## Problem Statement ##

You are given:

    A list of frogs' locations.
    A corresponding list of tongue sizes for each frog.
    A list of insect locations.

### The  $i^{th}$ frog catches the  $j^{th}$ insect if (insect<sub>j</sub> - frog<sub>i</sub>) <= tongue<sub>i</sub> ###

### Find the output  a list of integers where the $i^{th}$ element represents the number of insects caught by the $i^{th}$ frog. ###

## Constraints ##

Each frog's tongue size is a positive integer (0 < N < 10<sup>5</sup>).

All locations (frogs and insects) are integers.

Insects may fall into the catch range of multiple frogs.