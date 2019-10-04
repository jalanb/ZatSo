Handle the 1000 most common words

Given

    [Relevant XKCD](https://xkcd.com/1133/)

    This project was inspired by [Up Goer 5](https://xkcd.com/1133/)'s ability to express [rocket science in 1000 words](https://www.explainxkcd.com/wiki/index.php/1133:_Up_Goer_Five#Explanation)


When
    Code is easier than rocket science

Then
    A forest of upgoers ahould be able to handle codes

Hypothesis
    Given that the `popularity index` of a word is it's index in a list of all words sorted by popularity in a context
    Given that the `puplarity sum` of a text is the sum of the `popularity index` of each unique word in the text.
    I'd guess that a text with a lower `popularity sum` is easier to code automatically
