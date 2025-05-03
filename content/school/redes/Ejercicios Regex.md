---
creation date: 2025-04-25 18:09
modification date: Friday 25th April 2025 18:09:17
title: Ejercicios Regex
---
## Lesson 4: Excluding specific characters
In some cases, we might know that there are specific characters that we don't want to match too, for example, we might only want to match phone numbers that are _not_ from the area code 650.

To represent this, we use a similar expression that _excludes specific characters_ using the _square brackets_ and the _^_ (_hat_). For example, the pattern _[^abc]_ will match any _single_ character _except for_ the letters a, b, or c.

With the strings below, try writing a pattern that matches only the live animals (hog, dog, but not bog). Notice how most patterns of this type can also be written using the technique from the last lesson as they are really two sides of the same coin. By having both choices, you can decide which one is easier to write and understand when composing your own patterns.

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250425183144.png)

## Lesson 5: Character ranges
We just learned how to create a pattern that matches or excludes specific characters -- but what if we want to match a character that can be in a sequential range characters? Do we have no choice but to list them all out?

Luckily, when using the square bracket notation, there is a shorthand for matching a character in list of _sequential characters_ by using the _dash_ to indicate a character range. For example, the pattern _[0-6]_ will only match any single digit character from zero to six, and nothing else. And likewise, _[^n-p]_ will only match any single character _except_ for letters n to p.

Multiple character ranges can also be used in the same set of brackets, along with individual characters. An example of this is the alphanumeric _\w_ metacharacter which is equivalent to the character range _[A-Za-z0-9_]_ and often used to match characters in English text.

In the exercise below, notice how all the match and skip lines have a pattern, and use the bracket notation to match or skip each character from each line. Be aware that patterns are _case sensitive_ and _a-z differs_ from _A-Z_ in terms of the characters it matches (lower vs upper case).

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250425183430.png)

## Lesson 6: Catching some zzz's

_Note: Some parts of the repetition syntax below isn't supported in all regular expression implementations._

We've so far learned how to specify the range of characters we want to match, but how about the number of _repetitions_ of characters that we want to match? One way that we can do this is to explicitly spell out exactly how many characters we want, eg. _\d\d\d_ which would match exactly three digits.

A more convenient way is to specify how many repetitions of each character we want using the _curly braces_ notation. For example, _a{3}_ will match the a character exactly three times. Certain regular expression engines will even allow you to specify a range for this repetition such that _a{1,3}_ will match the a character no more than 3 times, but no less than once for example.

This quantifier can be used with any character, or special metacharacters, for example _w{3}_ (three w's), _[wxy]{5}_ (five characters, each of which can be a w, x, or y) and _.{2,6}_ (between two and six of _any_ character).

In the lines below, the last string with only one z isn't what we would consider a proper spelling of the slang "wazzup?". Try writing a pattern that matches only the first two spellings by using the curly brace notation above.
![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250425183940.png)

## Lesson 7: Mr. Kleene, Mr. Kleene

A powerful concept in regular expressions is the ability to match an arbitrary number of characters. For example, imagine that you wrote a form that has a donation field that takes a numerical value in dollars. A wealthy user may drop by and want to donate $25,000, while a normal user may want to donate $25.

One way to express such a pattern would be to use what is known as the _Kleene Star_ and the _Kleene Plus_, which essentially represents either _0 or more_ or _1 or more_ of the character that it follows (it always follows a character or group). For example, to match the donations above, we can use the pattern _\d*_ to match any number of digits, but a tighter regular expression would be _\d+_ which ensures that the input string has at least one digit.

These quantifiers can be used with any character or special metacharacters, for example _a+_ (one or more a's), _[abc]+_ (one or more of any a, b, or c character) and _.*_ (zero or more of _any_ character).

Below are a few simple strings that you can match using both the star and plus metacharacters.

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250425184204.png)

## Lesson 8: Characters optional
As you saw in the previous lesson, the Kleene star and plus allow us to match repeated characters in a line.

Another quantifier that is really common when matching and extracting text is the _?_ (question mark) metacharacter which denotes _optionality_. This metacharacter allows you to match either zero or one of the preceding character or group. For example, the pattern _ab?c_ will match either the strings "abc" or "ac" because the b is considered optional.

Similar to the dot metacharacter, the question mark is a special character and you will have to escape it using a slash _\?_ to match a plain question mark character in a string.

In the strings below, notice how the the plurality of the word "file" depends on the number of files found. Try writing a pattern that uses the optionality metacharacter to match only the lines where one or more files were found.

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250425185118.png)

## Lesson 9: All this whitespace
When dealing with real-world input, such as log files and even user input, it's difficult not to encounter whitespace. We use it to format pieces of information to make it easier to read and scan visually, and a single space can put a wrench into the simplest regular expression.

The most common forms of whitespace you will use with regular expressions are the _space_ (_␣_), the _tab_ (_\t_), the _new line_ (_\n_) and the carriage return (_\r_) (useful in Windows environments), and these special characters match each of their respective whitespaces. In addition, a _whitespace_ special character _\s_ will match _any_ of the specific whitespaces above and is extremely useful when dealing with raw input text.

In the strings below, you'll find that the content of each line is indented by some whitespace from the index of the line (_the number is a part of the text to match_). Try writing a pattern that can match each line containing whitespace characters between the number and the content. Notice that the whitespace characters are just like any other character and the special metacharacters like the star and the plus can be used as well.

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250425185816.png)

## Lesson 10: Starting and ending
So far, we've been writing regular expressions that partially match pieces across all the text. Sometimes this isn't desirable, imagine for example we wanted to match the word "success" in a log file. We certainly don't want that pattern to match a line that says "Error: unsuccessful operation"! That is why it is often _best practice to write as specific regular expressions as possible_ to ensure that we don't get false positives when matching against real world text.

One way to tighten our patterns is to define a pattern that describes both the _start and the end of the line_ using the special _^_ (_hat_) and _$_ (_dollar sign_) metacharacters. In the example above, we can use the pattern _^success_ to match _only_ a line that begins with the word "success", but not the line "Error: unsuccessful operation". And if you combine both the hat and the dollar sign, you create a pattern that matches the whole line completely at the beginning and end.

Note that this is different than the hat used inside a set of bracket _[^...]_ for excluding characters, which can be confusing when reading regular expressions.

Try to match each of the strings below using these new special characters.

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250425190234.png)


## Lesson 11: Match groups

Regular expressions allow us to not just match text but also to _extract information for further processing_. This is done by defining _groups of characters_ and capturing them using the special parentheses _(_ and _)_ metacharacters. Any subpattern inside a pair of parentheses will be _captured_ as a group. In practice, this can be used to extract information like phone numbers or emails from all sorts of data.

Imagine for example that you had a command line tool to list all the image files you have in the cloud. You could then use a pattern such as 

`^(IMG\d+\.png)$`

Go ahead and try to use this to write a regular expression that matches only the filenames (not including extension) of the PDF files below.

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250425191344.png)

## Lesson 12: Nested groups
When you are working with complex data, you can easily find yourself having to extract multiple layers of information, which can result in nested groups. Generally, the results of the captured groups are in the order in which they are defined (in order by open parenthesis).

Take the example from the previous lesson, of capturing the filenames of all the image files you have in a list. If each of these image files had a sequential picture number in the filename, you could extract both the filename and the picture number using the same pattern by writing an expression like _^(IMG(\d+))\.png$_ (using a nested parenthesis to capture the digits).

The nested groups are read from left to right in the pattern, with the first capture group being the contents of the first parentheses group, etc.

For the following strings, write an expression that matches _and captures_ both the full date, as well as the year of the date.

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250425192311.png)

## Lesson 13: More group work
As you saw in the previous lessons, all the quantifiers including the star _*_, plus _+_, repetition _{m,n}_ and the question mark _?_ can all be used within the capture group patterns. This is the only way to apply quantifiers on sequences of characters instead of the individual characters themselves.

For example, if I knew that a phone number may or may not contain an area code, the right pattern would test for the existence of the whole group of digits _(\d{3})?_ and not the individual characters themselves (which would be wrong).

Depending on the regular expression engine you are using, you can also use non-capturing groups which will allow you to match the group but not have it show up in the results.

Below are a couple different common display resolutions, try to capture the width and height of each display.

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250425193033.png)

## Lesson 14: It's all conditional
As we mentioned before, it's always good to be precise, and that applies to coding, talking, and even regular expressions. For example, you wouldn't write a grocery list for someone to _Buy more .*_ because you would have no idea what you could get back. Instead you would write _Buy more milk_ or _Buy more bread_, and in regular expressions, we can actually define these conditionals explicitly.

Specifically when using groups, you can use the _|_ (_logical OR, aka. the pipe_) to denote _different possible sets of characters_. In the above example, I can write the pattern "Buy more (milk|bread|juice)" to match only the strings Buy more milk, Buy more bread, or Buy more juice.

Like normal groups, you can use any sequence of characters or metacharacters in a condition, for example, ([cb]ats*|[dh]ogs?) would match either cats or bats, or, dogs or hogs. Writing patterns with many conditions can be hard to read, so you should consider making them separate patterns if they get too complex.

Go ahead and try writing a conditional pattern that matches only the lines with small fuzzy creatures below.

![Image Description](/darthpedro-obsidian/images/Pasted%20image%2020250425193414.png)

## Lesson 15: Other special characters
This lesson will cover some extra metacharacters, as well as the results of captured groups.

We have already learned the most common metacharacters to capture digits using _\d_, whitespace using _\s_, and alphanumeric letters and digits using _\w_, but regular expressions also provides a way of specifying the opposite sets of each of these metacharacters by using their upper case letters. For example, _\D_ represents any _non-digit_ character, _\S_ any _non-whitespace_ character, and _\W_ any _non-alphanumeric_ character (such as punctuation). Depending on how you compose your regular expression, it may be easier to use one or the other.

Additionally, there is a special metacharacter _\b_ which matches the boundary between a word and a non-word character. It's most useful in capturing entire words (for example by using the pattern _\w+\b_).

One concept that we will not explore in great detail in these lessons is _back referencing_, mostly because it varies depending on the implementation. However, many systems allow you to reference your captured groups by using _\0_ (usually the full matched text), _\1_ (group 1), _\2_ (group 2), etc. This is useful for example when you are in a text editor and doing a search and replace using regular expressions to swap two numbers, you can search for "(\d+)-(\d+)" and replace it with "\2-\1" to put the second captured number first, and the first captured number second for example.

Below are a number of different strings, try out the different types of metacharacters or anything we've learned in the previous lessons and continue on when you are ready.
