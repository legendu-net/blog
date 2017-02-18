UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2014-01-28 00:26:01
Slug: pig-questions
Title: Pig Questions
Category: Programming
Tags: programming, pig, big data, tips

**Things on this page are fragmentary and immature notes/thoughts of the author. It is not meant to readers but rather for convenient reference of the author and future improvement.**
 

1. How to find records that do not match a pattern? Can we use NOT?

2. Does pig ignore files with name starting with undersore and dot when loading files?

3. difference between COUNT and COUNT_STAR?, count seems wierd, check it
from the documentation, a record might not be count even if the field passed to count is not null
because the first filed might be null

4. it seems that pig doesn't require the join key to be unique?
or does it require at least 1 uniqueness?

5. use of dot and ::?

6. UDFs in java, must be static?

7. intuitively streaming won't be as fast as registering a Java or Python code,
why do we still use it?

8. what happens if schema has fewer fields than files?
omitted?

9. how to combine two sets horizontally wihout using join?
because I just want to do a matrix like cbind.

10. can we remove a record (first or last) from a sorted relation?

11. next record?

12. row number?
rank operator can achieve this

13. which is more efficient, pig or hive?
