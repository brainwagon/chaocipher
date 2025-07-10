# chaocipher

This is an implementation of Byrne's "chaocipher". 

I believe that I learned of this cipher from [this page](https://ciphermysteries.com/2010/07/03/the-chaocipher-revealed)
and then spent a few sleepless nights working on an implementation and some basic cryptanalysis of it.

There is this cool Youtube animation that demonstrates how it works.

<iframe width="560" height="315" src="https://www.youtube.com/embed/BPI3P-ikWCk?si=f0GLWaXaYi4AcHKs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Moshe Rubin published a [Clearing House for information on the Chaocipher](http://chaocipher.com/), and had some links to work that 
I did on my blog back then.  It was haphazard and I never reached a good conclusion, other than the Exhibit 1 appeared
to have a typo in it, and I never recovered Exhibit 2.  

Here are updated links to my blog posts on the subject:

- [The Chaocipher revealed! from Cipher Mysteries](https://brainwagon.org/blog/the-chaocipher-revealed-from-cipher-mysteries/)
- [An implementation of Byrnes' Chaocipher](https://brainwagon.org/blog/an-implementation-of-byrnes-chaocipher/) where this code originated, now updated for Python 3
- [Visual inspection of Chaocipher Output Implies Weakness](https://brainwagon.org/blog/visual-inspection-of-chaocipher-output-implies-weakness/), where I found that passing 2000 A's as input (a chosen plaintext attack) resulted in outputs with very short periodicity, which does not speak well to its strength
- [Progress on the Chaocipher](https://brainwagon.org/blog/progress-on-the-chaocipher/) which I don't seem to have the code for anymore (I'll dig and see if I can find it and add it to this archive)
- [More on the Chaocipher](https://brainwagon.org/blog/more-on-chaocipher/) where I made some headway on deciphering
Exhibit 1.  I'm not sure whether the bug mentioned in this has been fixed in this Python code.  I did manage to decode a significant part of Exhibit 1.
- [Typos in Exhibit 1](https://brainwagon.org/blog/typos-in-exhibit-1/) highlighted the problems I found in Exhibit 1. 
- [Crazy Optimization of the Chaocipher](https://brainwagon.org/blog/crazy-optimization-of-chaocipher/)

I'll try to dig through my old disks and post related code here.

## Usage

'''python3 chaocipher.py -d cipher.txt'''
