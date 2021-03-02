from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class MRTRipsinStation(MRJob):

  def mapper1(self, _, line):
    yield (line[6],1)
    yield (line[10],1)

  def reducer1(self, key, values):
    yield (key, sum(counts))
    
if __name__ == '__main__':
MRTRipsinStation.run()
