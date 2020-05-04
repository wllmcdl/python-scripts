Meta characters (need to be escaped \)
.[{()\^$|?*+

Snippets
^  -----------  Matches the beginning of a line
$  -----------  Matches the end of a line
.  -----------  Matches any character except new line
\s -----------  Matches whitespace (space, tab, newline)
\S -----------  Matches any non-whitespace char
\d -----------  Matches a digit (equal [0-9])
\D -----------	Matches any char that's not a digit (equals to [^0-9])
\b -----------	word boundary
\b -----------	not a word boundary 
*  -----------  Repeats a character zero or more times
*? -----------  Repeats a char zero or more times (non-greedy)
+  -----------  Repeats a char one or more times
+? -----------  Repeats a char one or more times (non-greedy)
[aeiou]  -----  Matches a single char in the listed set
[^XYZ]   -----  Matches a single char not in the listed set
[a-z0-9] -----  The set of chars can include a range
(  -----------  Indicates where string extraction is to start
)  -----------  Indicates where string extraction is to end
\w -----------	Word character equal to [a-zA-Z0-9_]
\W -----------	Not a word character equal to [^a-zA-Z0-9_]
a{3} ---------  Will match the a character exactly three times
a{m,n} -------  Will match the a character m to n times
(?:...)  -----  Match everything enclosed
(?=...)  -----  Positive lookahead
(?!...)  -----  Negative lookahead
(a|b)	 -----	match either a or b
?  -----------  Matches between zero and one times, as many times as possible, giving back as needed

Character Set
[]  - matches characters in brackets
[^] - matches characters not in brackets
|   - Or
()  - group

Quantifiers
*     - 0 or more
+     - 1 or more
?     - 0 or more
{3}   - exact number
{3,4} - range of numbers (minimum, maximum)


########## Sample Regexs ##########
# match emails
[a-z0-9._]+@[a-z-_]+[a-z.]+ 

####################################################################################################

####################################################################################################
Example 1 <-> 'Caio: caio@gmail.com'
# a string that has characters from a-z @ sign and character from a-z and a . after @ 
Get all the characters from a to z lowercase once ([a-z]) from one to unlimited number of times (+) until we reach the character @ then after @ get all the characters from a to z lowercase and a dot . character once ([a-z]) from one to unlimited number of times (+) until we reach the end another character that wasn't specified.

[a-z]+@[a-z.]+ -> this expression matches caio@gmail.com

[a-z] 	-> match a single character between a to z lower case characters
+	-> match between one and unlimited times
@	-> match the character @ literally
[a-z.]	-> match a single character between a to z lower case characters and a . Character
+	-> match between one and unlimited times until line terminators

# quantifiers -> ? * + {}

####################################################################################################

Reads, give me...
a? 	== zero or one of a
a* 	== zero or more of a
a+ 	== one or more of a
a{3}	== exactly 3 of a
a{3,} 	== 3 or more of a (aaa)
a{3,6}	== between 3 and 6 of a (aaa...aaaaaa)

####################################################################################################

####################################################################################################
Example 2 <-> '<div>simple div</div>'

<.+?> -> this expression matches <div> </div> (reads, matches any and all the chars between the < > chars)

<	== matches the character < literally
.	== matches any character 
+?	== found once stop
>	== matches the character > literally (and is the end of the expression)

Example 2.1
<	== matches the character < literally
.	== matches any character 
+	== match between one and unlimited times until line terminators (/n)
>	== (when it finds the line terminator it searches for the last character specified to end the match. In this case the char >) matches the character > literally

<.+> -> this expression finds <div>simple div</div>

####################################################################################################

####################################################################################################
Python <-> import re

# returns a true/false depending on whether the string matches the regex
re.search('regex', string_to_aplly_regex)

# allow the matching string to be extracted returns a list
re.findall('regex', string_to_aplly_regex)
####################################################################################################
