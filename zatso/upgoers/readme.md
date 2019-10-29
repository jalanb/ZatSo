# Upgoers

[Relevant XKCD](https://xkcd.com/1133/)

This project was inspired by [Up Goer 5](https://xkcd.com/1133/)'s ability to express [rocket science](https://www.explainxkcd.com/wiki/index.php/1133:_Up_Goer_Five#Explanation) in 1000 words, and will try find out how few words can express how much [code](https://github.com/jalanb/zatso).

This projet was also inspired by some of [The Zen Of Python](https://en.wikipedia.org/wiki/Zen_of_Python), by [Tim Peters](https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer))

1. Beautiful is better than ugly.
1. Simple is better than complex.
1. Readability counts.
1. There should be one obvious way to do it.
1. Now is better than never.
1. Easy to explain may be a good idea.
1. Namespaces are one honking great idea!


## Definitions
The `rank` of a word is it's index in a list of all words sorted descendingly by popularity in a context.

The `rank` of a text is the sum of the ranks of each unique word in the text.

## Hypotheses
	
* `code` is easier than `rocket science`
* Text with a lower `rank` is easier to code
* Code with a lower `rank` is better code

