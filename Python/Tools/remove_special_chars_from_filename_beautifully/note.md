Personal file rename script for annoying filenames. Takes my downloads folder and adjusts filenames to remove internet bloat and illegal characters

### TODO
- [x] multi-part extensions like .tar.gz
- [x] 2 files turning into the same name
    - [x] if identical, remove the copy instead of renaming it
    - [x] if different files, same name, flag problem and wait for user to intervene
- [ ] add preview before making changes



### Replace separators
Replace
```
： 
```

(these are all different characters, even if they look the same)
```
 ｜ 
```

With
```
 - 
```



### Remove question marks
(not a regular question mark, special character)

RegEx v2 match
abstract: question is followed by special characters or end of file
```
(？)(\s*\S|$)
```
replace
```
$2
```


RegEx v2 match
abstract: question is followed by regular text
```
(？)\s(\w+)
```
replace
```
 - $2
```


### Replace hashes
(it's not a regular hash, but a special character)
#### Remove number markings
(`#94` -> `94`)
RegEx v2 match
```
#(\d+)
```
replace
```
$1
```



#### Remove hashtags at the end of filename
(`title #music #tutorial` -> `title`)
RegEx v2 match
abstract: whitespace, hash, text that's not a number
```
\s#\D+
```
replace (leave empty)
```

```

