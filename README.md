# self-pruning-spanning-tree
A demo of a connectivity subgraph extraction algorithm

## Concept

The idea is to just run two spanning trees. The first starts at all the source nodes and builds out a subgraph of paths going out of those nodes. The trick is that it stores this subgraph with all the edges backwards. Then you feed *that* graph into the same algorithm, with the targets as your sources. The output is a directed subgraph of just the part of the original graph that describes all possible paths from your sources to your sinks.

## Background

I came up with this algorithm to solve a few different problems a few times. My previous employer said it wasn't worth copywriting or patenting or whatever, and I ended up needing it again at my new job, so I decided to put it out there in case someone else needs it.

I'm sure there are fancy ways to measure performance, but I found it not only gave me the answer to "are these nodes connected to these other nodes" faster than anything I could find in popular graph theory libraries, but it also gave me a complete connectivity subgraph as a side-effect. Which is handy for situations where you care about everything that could be between two sets of points.

I don't know if this is already an algorithm someone else came up with. I'll bet someone with an important name put it in a book I'll never read. But whether or not I was the first, I came up with this and I think it's neat, and I wanted to share. I just hope someone finds it as useful as I have!
