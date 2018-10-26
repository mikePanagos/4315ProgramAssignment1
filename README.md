# 4315ProgramAssignment1
cosc2991 1354098 Fabian Ornelas
cosc2992 1293866 Michael Panagos


Main file is infinitearithmetic.py.
file_maker.py contains a function that recursively retrieves every line in the selected input file and returns a list of lines.

The program begins with executing recurseList where it goes through the list of equations looks to see it its + or * then solves it accordingly and pushes it to a new list.

The function mathAdd handles addition by first splitting the operands into nodes containing the indicated amount of digits. Then recursively adds the first node of each list to each other while considering any carry digits that may carry on to new nodes.

The function mathMult handles multiplication by multiplying the contents of 1 node with a selected digit of the other set of nodes until all nodes have been recursively gone through.

The function assemble takes sets of nodes and assembles them together to form the resulting string, which is then used to be outputted on to the terminal.
