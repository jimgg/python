import pstats
import sys
p = pstats.Stats(sys.argv[1])
p.sort_stats('cumtime').print_stats(30)
# p.sort_stats('time').print_stats(30)
