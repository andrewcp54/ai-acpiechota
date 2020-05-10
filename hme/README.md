# HME Recognition
I had a hard time deciding exactly **what** I wanted to do for my final.

I toyed back and forth with creating some sort of game--like checkers or snake, and having the A.I. be pitted again the user or utilizing a neural network for some sort of detection and classifion scheme. But, after seeing what some of the other students have done, I think I want to go the route of image detection, namely with Kera and Tensorflow.

After looking through loads of tutorials and the like for image detection, I've decided to try to attempt to get a neural network to recognize digits, letters and some mathematical symbols, simultaneously. I've found out that I am attempting to recongize Handwritten Mathematical Expression (HME for short). 

The goal of this project would be for the network to be able to distinguish between number or symbol, or letter.

I know there are going to be obvious problems w/ this project (like `0 vs O`, or `1 vs l vs ln` , or `{ vs ( vs 3` , etc) however, I would like to try to get as accurate as I can. My plan is to handwrite some examples and the main goal isn't really sentences, but for example, I'd like the network to be able to tell the difference between the alpha symbol `(α)` and the letter `(a)`.  

The largest dataset I could find was [CROHME](https://www.isical.ac.in/~crohme/), which is generally used in competitions for this sort of thing. 