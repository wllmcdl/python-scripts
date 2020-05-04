# Regex  
   
##### Meta characters ( *need to be escaped* `\` )  
`.[{()\^$|?*+`  
   
##### Snippets  
`^` --- *Matches the beginning of a line*  
`$` --- *Matches the end of a line*  
`.` --- *Matches any character except new line*  
`\s` --- *Matches whitespace (space, tab, newline)*  
`\S` --- *Matches any non-whitespace char*  
`\d` --- *Matches a digit (equal [0-9])*  
`\D` --- *Matches any char that's not a digit (equals to [^0-9])*  
`\b` --- *Word boundary*  
`\b` --- *Not a word boundary*  
`*?` --- *Repeats a char zero or more times (non-greedy)*  
`+?` --- *Repeats a char one or more times (non-greedy)*  
`[aeiou]` --- *Matches a single char in the listed set*  
`[^XYZ]` --- *Matches a single char not in the listed set*  
`[a-z0-9]` --- *The set of chars can include a range*  
`\w` --- *Word character equal to [a-zA-Z0-9_]*  
`\W` --- *Not a word character equal to [^a-zA-Z0-9_]*  
`a{3}` --- *Will match the a character exactly three times*  
`a{m,n}` --- *Will match the a character m to n times*  
`(?:...)` --- *Match everything enclosed*  
`(?=...)` --- *Positive lookahead*  
`(?!...)` --- *Negative lookahead*  
`(a|b)` ---	*Match either a or b*  
   
##### Character Set  
`[]` --- *matches characters in brackets*  
`[^]` --- *matches characters not in brackets*  
`|` --- *Or*  
`()` --- *group*   
   
##### Quantifiers  
`?`     --- *zero or one as many times as possible, giving back as needed*  
`*`     --- *Repeats a character zero or more times*  
`+`     --- *Repeats a character one or more times*  
`{m}`   --- *exact number of elements (a{3} reads as exactly 3 of a)*  
`{m,}`  --- *range from m to infinite elements (a{3,} reads 3 or more of a)*  
`{m,n}` --- *range from m to n elements (a{3,6} reads between 3 and 6 of a)*  
   
##### Regex on Python  
`re.search('regex', aString)` --- *Returns true/false depending on whether the string matches the regex*  
`re.findall('regex', aString)` --- *Allow the matching string to be extracted returns a list*  