Handle the most common words only

[Relevant XKCD](https://xkcd.com/1133/)

    This project was inspired by [Up Goer 5](https://xkcd.com/1133/)'s ability to express [rocket science in 1000 words](https://www.explainxkcd.com/wiki/index.php/1133:_Up_Goer_Five#Explanation)

    I'd like to take `1000` more as a staring point and find out how few words can express how much code, because I reckon code is easier than rocket science

Definitions
    The `popularity index` of a word is it's index in a list of all words sorted by popularity in a context.
    The `poplarity sum` of a text is the sum of the `popularity index` of each unique word in the text.

Hypothesis
    A text with a lower `popularity sum` is easier to code
    A code with a lower `popularity sum` is better code

ToDo
    Website with simple choices for "better code" vs "worser code"
