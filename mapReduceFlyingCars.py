# write an algorithm and program to find all violators.
# Assume input is a HUGE file (10 billion cars
# logging "VIN,timestamp,x,y,z" every 10 milliseconds all-the-time
import sys


def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split(",")

        # This is the place for some defensive programming
        # what if there are not exactly 5 fields in that line?
        if len(data) == 5:

        # this next line is called 'multiple assignment' in Python
        # this is not really necessary, we could access the data
        # with data[2] and data[5], but we do this for conveniency
        # and to make the code easier to read
            VIN, timestamp, x, y, z = data

        # Now print out the data that will be passed to the reducer
             print
             "{0}\t{1}".format(VIN, cost)


test_text = """2013-10-09\t13:22\tMiami\tBoots\t99.95\tVisa
2013-10-09\t13:22\tNew York\tDVD\t9.50\tMasterCard
2013-10-09 13:22:59 I/O Error
^d8x28orz28zoijzu1z1zp1OHH3du3ixwcz114<f
1\t2\t3"""


# reducer code

def reducer():
    salesTotal = 0
    oldKey = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        thisKey, thisSale = data

        if oldKey and oldKey != thisKey:
            print
            "{0}\t{1}".format(oldKey, salesTotal)

            salesTotal = 0
        oldKey = thisKey
        salesTotal += float(thisSale)
    if oldKey != None:
        print
        "{0}\t{1}".format(oldKey, salesTotal)

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__