"""
Copyright 2016 William La Cava

This file is part of the FEW library.

The FEW library is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

The FEW library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
the FEW library. If not, see http://www.gnu.org/licenses/.

"""
from few.population import ind, Pop, init, make_program
# unit tests for population methods.
def test_pop_shape():
    """ make sure correct population size is returned. """
    # pop = Pop(0)
    # assert len(pop) == 0
    pop = Pop(10)
    assert len(pop.programs) == 10
    print("pop.X.shape",pop.X.shape)
    assert pop.X.shape == (1,10)
    assert pop.E.shape == (1,10)


    pop = Pop(73)
    assert len(pop.programs) == 73
    assert pop.X.shape == (1,73)
    assert pop.E.shape == (1,73)

    pop = Pop(73,5)
    assert len(pop.programs) == 73
    assert pop.X.shape == (5,73)
    assert pop.E.shape == (5,73)
