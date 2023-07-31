## tries

<br>

* tries, also called prefix tree, are a variant of n-ary tree in which characters are stored in each node.
* each trie node represents a string (a prefix) and each path down the tree represents a word. note that not all the strings represented by trie nodes are meaningful.
* the root is associated with the empty string.
* the * nodes (null nodes) are often used to indicate complete words (usually represented by a special type of child) or a boolean flag that terminates the parent node.
* a node can have anywhere from 1 through alphabet_size + 1 child.
* can be used to store the entire english language for quick prefix lookup (O(k), where k is the length of the string). they are also widely used on autocompletes, spell checkers, etc.
* tries structures can be represented by arrays and maps or trees.

<br>

### insertion

<br>

* similar to a bst, when we insert a value to a trie, we need to decide which path to go depending on the target value we insert.
* the root node needs to be initialized before you insert strings.

<br>

### search

<br>

* all the descendants of a node have a common prefix of the string associated with that node, so it should be easy to search if there are any words in the trie that starts with the given prefix.
* we go down the tree depending on the given prefix, once we cannot find the child node, the search fails.
* we can also search for a specific word rather than a prefix, treating this word as a prefix and searching in the same way as above.
* if the search succeeds, we need to check if the target word is only a prefix of words in the trie or if it's exactly a word (for example, by adding a boolean flag).

<br>