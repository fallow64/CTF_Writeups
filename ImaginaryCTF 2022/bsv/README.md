# bsv
This challenge was from Imaginary CTF 2022.

The description is:
>  just made my own file format. It's called BSV, for BEE-separated-values! See if you can recover my secret flag.
> 
> Note: You will need to add the {} of the flag yourself. Please make the flag all lowercase. Flag format: ictf{[a-z0-9_]*}

One file was attached, `flag.bsv`:
```
BEEAccordingBEEtoBEEallBEEknownBEE BEE BEElawsBEEofBEEaviationBEEthereBEEisBEEnoBEE BEE BEEwayBEEaBEEbeeBEEshouldBEEbeBEEableBEEtoBEEfly.BEE BEEItsBEEwingsBEEareBEEtooBEEsmallBEEtoBEEgetBEEitsBEE BEEfatBEElittleBEEbodyBEEoffBEEtheBEEground.BEETheBEEbeeBEE BEE BEEofBEEcourseBEE BEE BEE BEE BEE BEEfliesBEEanywayBEE BEEbecauseBEEbeesBEEdon'tBEEcareBEEwhatBEEhumansBEEthinkBEEisBEE (etc... you get the point)
```
This was just a .csv file, except that the commas were replaced with `"BEE"`.

If you replace the `BEE`s with commas, rename the file to have a `.csv` extension, open it up in some editor, and apply some fancy formatting, you get:
![half-distorted text containing flag](https://i.imgur.com/Ae06yl9.png)

I stared at this so long trying to find out what the last few letters are, but then I realized that the rows shifted to the right some, and it was fine at the start but progressively stacked to make it unreadable. So after fixing it, I got this:

![text containing flag](https://i.imgur.com/HQ1iEZ9.png)

The challenge description stated that you needed to add the `{}` and that all the letters were lowercase, so the final flag was:

```
ictf{buzz_buzz_b2f13a}
```