UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Summary on Random Number Generators
Date: 2012-07-24 00:00:00
Tags: WELL, RNG, statistics, SFMT, dimension, MT
Category: Statistics
Slug: summary-random-number-generators
Author: Ben Chuanlong Du

<img src="http://dclong.github.io/media/rng/random-number-generator.png" height="200" width="240" align="right"/>

The most popular pseudo random number generator (PRNG) currently is Mersenne Twister. 
Mersenne Twister has many different versions, among which the MT19937 
is the most widely used one. 
The period of MT19937 is extreemly long ($2^{19937}-1$)
and is equidistributed for generating vectors up to dimension 623. 
The MT19937 generate 32 bits random numbers. 
Combining two random blocks, one can generate 64 bits random numbers.
This is often implemented together with the 32 bit version, 
and usually call MT19937_64.
The MT19937_64 is equidistributed for generating vectors up to dimension 311.
A more modern family of random number generators than Mersenne Twister 
is the WELL random number generators, which have better equidistribution 
property and are better to escape the zeroland (initialization 
array contains many zero bits). 
However, the speed of the WELL generators is about 0.6 to 0.7 compared to the Mersenne Twister generators. 
Also the WELL random number generators has a large inner state 
(e.g., the WELL44497b uses about 33kb for its inner state while the MT19937 uses only about 2.5kb). 
This is usually not a problem on modern computers, 
but if you use lots of random number generators at the same time or if the code is run on a embedded device, 
it might worth considering the consume of memories of these generators. 
Among different versions of WELL generators, WELL19937c and WELL44497b are commonly used. 
SIMD-oriented Fast Mersenne Twister is an improved version of Mersenne Twister. 
It uses parallelism of modern CPUs and is about twice faster than mersenne Twister. 
SFMT also has better equidistribution property than Mersenne Twister, but not as good as WELL.
SFMT recovers from 0-excess initial state faster than Mersenne Twister, but not faster than WELL.
It is likely that SFMT replaces Mersenne Twister and becomes the next popular number generator. 
